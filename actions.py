import requests
import time
import json
import asyncio
import aiohttp
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
from PIL import Image
import io
import base64
from bs4 import BeautifulSoup
import re
import os

# API Keys and configurations
WEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "demo_key")
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "demo_key")
STOCK_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY", "demo_key")

def get_response_time(url: str) -> Dict[str, Any]:
    """
    Get real response time and performance metrics for a website.
    """
    try:
        start_time = time.time()
        
        # Add protocol if missing
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        response = requests.get(url, timeout=10, allow_redirects=True)
        end_time = time.time()
        
        response_time = end_time - start_time
        
        # Get additional metrics
        status_code = response.status_code
        content_length = len(response.content) if response.content else 0
        headers = dict(response.headers)
        
        return {
            "response_time": round(response_time, 3),
            "status_code": status_code,
            "content_length": content_length,
            "final_url": response.url,
            "headers": {
                "server": headers.get("server", "unknown"),
                "content_type": headers.get("content-type", "unknown")
            }
        }
    except requests.exceptions.RequestException as e:
        return {"error": str(e), "response_time": None}

def get_weather_info(city: str) -> Dict[str, Any]:
    """
    Get real weather information using OpenWeatherMap API.
    """
    try:
        if WEATHER_API_KEY == "demo_key":
            # Fallback to mock data if no API key
            weather_data = {
                "new york": {"temperature": 72, "condition": "sunny", "humidity": 65, "wind_speed": 8},
                "london": {"temperature": 58, "condition": "cloudy", "humidity": 80, "wind_speed": 12},
                "tokyo": {"temperature": 75, "condition": "rainy", "humidity": 70, "wind_speed": 15},
                "sydney": {"temperature": 68, "condition": "clear", "humidity": 55, "wind_speed": 10}
            }
            city_lower = city.lower().replace(" ", "_")
            return weather_data.get(city_lower, {"temperature": 70, "condition": "unknown", "humidity": 60, "wind_speed": 5})
        
        # Real API call
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": WEATHER_API_KEY,
            "units": "imperial"
        }
        
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        return {
            "temperature": round(data["main"]["temp"]),
            "condition": data["weather"][0]["main"].lower(),
            "humidity": data["main"]["humidity"],
            "wind_speed": round(data["wind"]["speed"]),
            "pressure": data["main"]["pressure"],
            "visibility": data.get("visibility", "unknown"),
            "sunrise": datetime.fromtimestamp(data["sys"]["sunrise"]).strftime("%H:%M"),
            "sunset": datetime.fromtimestamp(data["sys"]["sunset"]).strftime("%H:%M")
        }
        
    except Exception as e:
        return {"error": f"Failed to get weather data: {str(e)}"}

def calculate_math_expression(expression: str) -> Dict[str, Any]:
    """
    Safely evaluate mathematical expressions with detailed analysis.
    """
    try:
        # Only allow safe mathematical operations
        allowed_chars = set('0123456789+-*/(). ')
        if not all(c in allowed_chars for c in expression):
            return {"error": "Invalid characters in expression"}
        
        # Calculate result
        result = eval(expression)
        
        # Analyze the expression
        analysis = {
            "expression": expression,
            "result": result,
            "operations": {
                "addition": expression.count('+'),
                "subtraction": expression.count('-'),
                "multiplication": expression.count('*'),
                "division": expression.count('/'),
                "parentheses": expression.count('(') + expression.count(')')
            },
            "complexity": "simple" if len(expression) < 10 else "moderate" if len(expression) < 20 else "complex"
        }
        
        return analysis
        
    except Exception as e:
        return {"error": f"Calculation error: {str(e)}"}

def get_current_time(timezone: str = "UTC") -> Dict[str, Any]:
    """
    Get current time with timezone information.
    """
    try:
        now = datetime.utcnow()
        
        # Simple timezone conversion (in production, use pytz or zoneinfo)
        timezone_offsets = {
            "UTC": 0, "EST": -5, "PST": -8, "CET": 1, "JST": 9
        }
        
        offset = timezone_offsets.get(timezone.upper(), 0)
        local_time = now + timedelta(hours=offset)
        
        return {
            "utc_time": now.strftime("%Y-%m-%d %H:%M:%S"),
            "local_time": local_time.strftime("%Y-%m-%d %H:%M:%S"),
            "timezone": timezone.upper(),
            "timestamp": int(now.timestamp()),
            "day_of_week": now.strftime("%A"),
            "is_weekend": now.weekday() >= 5
        }
        
    except Exception as e:
        return {"error": f"Time error: {str(e)}"}

def search_web(query: str, max_results: int = 5) -> Dict[str, Any]:
    """
    Perform web search using DuckDuckGo (no API key required).
    """
    try:
        # Use DuckDuckGo instant answer API
        url = "https://api.duckduckgo.com/"
        params = {
            "q": query,
            "format": "json",
            "no_html": "1",
            "skip_disambig": "1"
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        results = {
            "query": query,
            "abstract": data.get("Abstract", "No abstract available"),
            "related_topics": data.get("RelatedTopics", [])[:max_results],
            "answer": data.get("Answer", "No direct answer available"),
            "definition": data.get("Definition", "No definition available"),
            "source": data.get("AbstractSource", "Unknown")
        }
        
        return results
        
    except Exception as e:
        return {"error": f"Search failed: {str(e)}"}

def get_stock_price(symbol: str) -> Dict[str, Any]:
    """
    Get real-time stock price information using Alpha Vantage API.
    """
    try:
        if STOCK_API_KEY == "demo_key":
            # Mock data for demonstration
            mock_prices = {
                "AAPL": {"price": 150.25, "change": 2.15, "change_percent": 1.45},
                "GOOGL": {"price": 2750.80, "change": -15.20, "change_percent": -0.55},
                "MSFT": {"price": 310.45, "change": 5.75, "change_percent": 1.89},
                "TSLA": {"price": 245.60, "change": -8.90, "change_percent": -3.50}
            }
            return mock_prices.get(symbol.upper(), {"price": 100.00, "change": 0.00, "change_percent": 0.00})
        
        # Real API call
        url = "https://www.alphavantage.co/query"
        params = {
            "function": "GLOBAL_QUOTE",
            "symbol": symbol.upper(),
            "apikey": STOCK_API_KEY
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        quote = data.get("Global Quote", {})
        
        if not quote:
            return {"error": "Stock symbol not found"}
        
        return {
            "symbol": quote.get("01. symbol"),
            "price": float(quote.get("05. price", 0)),
            "change": float(quote.get("09. change", 0)),
            "change_percent": quote.get("10. change percent", "0%"),
            "volume": quote.get("06. volume"),
            "market_cap": quote.get("07. market cap", "Unknown")
        }
        
    except Exception as e:
        return {"error": f"Stock data error: {str(e)}"}

def get_news_headlines(category: str = "general", country: str = "us") -> Dict[str, Any]:
    """
    Get latest news headlines using NewsAPI.
    """
    try:
        if NEWS_API_KEY == "demo_key":
            # Mock news data
            mock_news = {
                "technology": [
                    {"title": "AI Breakthrough in Machine Learning", "description": "New algorithm shows promising results"},
                    {"title": "Quantum Computing Milestone", "description": "Researchers achieve quantum supremacy"}
                ],
                "business": [
                    {"title": "Market Rally Continues", "description": "Stocks reach new highs"},
                    {"title": "Tech Company Earnings Beat Expectations", "description": "Strong quarterly results reported"}
                ]
            }
            return {"category": category, "articles": mock_news.get(category, [])}
        
        # Real API call
        url = "https://newsapi.org/v2/top-headlines"
        params = {
            "country": country,
            "category": category,
            "apiKey": NEWS_API_KEY,
            "pageSize": 10
        }
        
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        articles = []
        for article in data.get("articles", []):
            articles.append({
                "title": article.get("title"),
                "description": article.get("description"),
                "source": article.get("source", {}).get("name"),
                "published_at": article.get("publishedAt"),
                "url": article.get("url")
            })
        
        return {
            "category": category,
            "country": country,
            "total_results": data.get("totalResults", 0),
            "articles": articles
        }
        
    except Exception as e:
        return {"error": f"News error: {str(e)}"}

def analyze_text_sentiment(text: str) -> Dict[str, Any]:
    """
    Analyze text sentiment and provide insights.
    """
    try:
        # Simple sentiment analysis (in production, use a proper NLP library)
        positive_words = ["good", "great", "excellent", "amazing", "wonderful", "happy", "love", "like"]
        negative_words = ["bad", "terrible", "awful", "horrible", "sad", "hate", "dislike", "worst"]
        
        text_lower = text.lower()
        words = re.findall(r'\b\w+\b', text_lower)
        
        positive_count = sum(1 for word in words if word in positive_words)
        negative_count = sum(1 for word in words if word in negative_words)
        total_words = len(words)
        
        if total_words == 0:
            return {"error": "No text to analyze"}
        
        positive_score = positive_count / total_words
        negative_score = negative_count / total_words
        neutral_score = 1 - positive_score - negative_score
        
        # Determine sentiment
        if positive_score > negative_score and positive_score > 0.1:
            sentiment = "positive"
        elif negative_score > positive_score and negative_score > 0.1:
            sentiment = "negative"
        else:
            sentiment = "neutral"
        
        return {
            "text_length": len(text),
            "word_count": total_words,
            "sentiment": sentiment,
            "scores": {
                "positive": round(positive_score, 3),
                "negative": round(negative_score, 3),
                "neutral": round(neutral_score, 3)
            },
            "positive_words": positive_count,
            "negative_words": negative_count
        }
        
    except Exception as e:
        return {"error": f"Sentiment analysis error: {str(e)}"}

def get_website_info(url: str) -> Dict[str, Any]:
    """
    Get comprehensive website information including metadata and content analysis.
    """
    try:
        # Add protocol if missing
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract metadata
        title = soup.find('title')
        title_text = title.get_text() if title else "No title found"
        
        meta_description = soup.find('meta', attrs={'name': 'description'})
        description = meta_description.get('content') if meta_description else "No description found"
        
        # Count elements
        headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        images = soup.find_all('img')
        links = soup.find_all('a')
        
        # Extract text content
        text_content = soup.get_text()
        word_count = len(text_content.split())
        
        return {
            "url": url,
            "title": title_text.strip(),
            "description": description.strip(),
            "status_code": response.status_code,
            "content_length": len(response.content),
            "word_count": word_count,
            "headings": {
                "h1": len(soup.find_all('h1')),
                "h2": len(soup.find_all('h2')),
                "h3": len(soup.find_all('h3')),
                "total": len(headings)
            },
            "images": len(images),
            "links": len(links),
            "language": soup.get('lang', 'Unknown'),
            "charset": response.encoding
        }
        
    except Exception as e:
        return {"error": f"Website analysis error: {str(e)}"}

def perform_data_analysis(data_input: str) -> Dict[str, Any]:
    """
    Perform basic data analysis on provided data.
    """
    try:
        # Try to parse as CSV or JSON
        if data_input.strip().startswith('[') or data_input.strip().startswith('{'):
            # JSON data
            data = json.loads(data_input)
            if isinstance(data, list):
                df = pd.DataFrame(data)
            else:
                df = pd.DataFrame([data])
        else:
            # Try CSV
            from io import StringIO
            df = pd.read_csv(StringIO(data_input))
        
        # Basic statistics
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        
        analysis = {
            "data_shape": df.shape,
            "columns": list(df.columns),
            "data_types": df.dtypes.to_dict(),
            "missing_values": df.isnull().sum().to_dict(),
            "summary_stats": {}
        }
        
        # Add statistics for numeric columns
        for col in numeric_columns:
            analysis["summary_stats"][col] = {
                "mean": float(df[col].mean()),
                "median": float(df[col].median()),
                "std": float(df[col].std()),
                "min": float(df[col].min()),
                "max": float(df[col].max())
            }
        
        return analysis
        
    except Exception as e:
        return {"error": f"Data analysis error: {str(e)}"}

def translate_text(text: str, target_language: str = "es") -> Dict[str, Any]:
    """
    Translate text to target language using Google Translate (free tier).
    """
    try:
        # Simple translation using Google Translate (in production, use proper API)
        # This is a mock implementation - replace with real translation service
        
        mock_translations = {
            "es": {
                "hello": "hola",
                "world": "mundo",
                "good morning": "buenos días",
                "thank you": "gracias"
            },
            "fr": {
                "hello": "bonjour",
                "world": "monde",
                "good morning": "bonjour",
                "thank you": "merci"
            },
            "de": {
                "hello": "hallo",
                "world": "welt",
                "good morning": "guten morgen",
                "thank you": "danke"
            }
        }
        
        text_lower = text.lower()
        translations = mock_translations.get(target_language, {})
        
        if text_lower in translations:
            translated = translations[text_lower]
        else:
            # Mock translation by adding language suffix
            translated = f"{text} ({target_language})"
        
        return {
            "original_text": text,
            "translated_text": translated,
            "target_language": target_language,
            "detected_language": "en",
            "confidence": 0.95
        }
        
    except Exception as e:
        return {"error": f"Translation error: {str(e)}"}

def get_crypto_price(symbol: str = "BTC") -> Dict[str, Any]:
    """
    Get cryptocurrency price information.
    """
    try:
        # Mock crypto data (replace with real API like CoinGecko)
        crypto_prices = {
            "BTC": {"price": 45000, "change_24h": 2.5, "market_cap": "850B", "volume": "25B"},
            "ETH": {"price": 3200, "change_24h": -1.2, "market_cap": "380B", "volume": "15B"},
            "ADA": {"price": 1.25, "change_24h": 5.8, "market_cap": "40B", "volume": "2B"},
            "DOT": {"price": 18.50, "change_24h": -0.8, "market_cap": "18B", "volume": "800M"}
        }
        
        symbol_upper = symbol.upper()
        if symbol_upper in crypto_prices:
            return {
                "symbol": symbol_upper,
                **crypto_prices[symbol_upper],
                "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        else:
            return {"error": f"Cryptocurrency {symbol} not found"}
            
    except Exception as e:
        return {"error": f"Crypto price error: {str(e)}"}

def get_github_repo_info(repo_name: str) -> Dict[str, Any]:
    """
    Get GitHub repository information.
    """
    try:
        # GitHub API (no authentication required for public repos)
        url = f"https://api.github.com/repos/{repo_name}"
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        return {
            "name": data.get("name"),
            "full_name": data.get("full_name"),
            "description": data.get("description"),
            "language": data.get("language"),
            "stars": data.get("stargazers_count"),
            "forks": data.get("forks_count"),
            "open_issues": data.get("open_issues_count"),
            "size": data.get("size"),
            "created_at": data.get("created_at"),
            "updated_at": data.get("updated_at"),
            "url": data.get("html_url")
        }
        
    except Exception as e:
        return {"error": f"GitHub API error: {str(e)}"}
