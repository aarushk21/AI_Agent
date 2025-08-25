#!/usr/bin/env python3
"""
Enhanced Demo Script for the AI Agent System
This demonstrates all the new sophisticated functions and real API integrations.
"""

import json
import time
from actions import (
    get_response_time, 
    get_weather_info, 
    calculate_math_expression, 
    get_current_time, 
    search_web,
    get_stock_price,
    get_news_headlines,
    analyze_text_sentiment,
    get_website_info,
    perform_data_analysis,
    translate_text,
    get_crypto_price,
    get_github_repo_info
)

def demo_website_analysis():
    """Demonstrate website analysis capabilities."""
    print("\nWebsite Analysis Demo")
    print("=" * 50)
    
    websites = ["learnwithhasan.com", "github.com", "stackoverflow.com"]
    
    for website in websites:
        print(f"\nAnalyzing {website}:")
        
        # Get response time
        response_data = get_response_time(website)
        if "error" not in response_data:
            print(f"  Response Time: {response_data['response_time']} seconds")
            print(f"  Status Code: {response_data['status_code']}")
            print(f"  Content Length: {response_data['content_length']:,} bytes")
        
        # Get website info
        website_data = get_website_info(website)
        if "error" not in website_data:
            print(f"  Title: {website_data['title']}")
            print(f"  Word Count: {website_data['word_count']:,}")
            print(f"  Headings: {website_data['headings']['total']} total")
            print(f"  Images: {website_data['images']}")
            print(f"  Links: {website_data['links']}")

def demo_financial_data():
    """Demonstrate financial data capabilities."""
    print("\nFinancial Data Demo")
    print("=" * 50)
    
    # Stock prices
    stocks = ["AAPL", "GOOGL", "MSFT", "TSLA"]
    print("\nStock Prices:")
    for stock in stocks:
        stock_data = get_stock_price(stock)
        if "error" not in stock_data:
            print(f"  {stock}: ${stock_data['price']} ({stock_data['change_percent']})")
    
    # Crypto prices
    cryptos = ["BTC", "ETH", "ADA"]
    print("\nCryptocurrency Prices:")
    for crypto in cryptos:
        crypto_data = get_crypto_price(crypto)
        if "error" not in crypto_data:
            print(f"  {crypto}: ${crypto_data['price']:,} ({crypto_data['change_24h']}% 24h)")

def demo_data_analysis():
    """Demonstrate data analysis capabilities."""
    print("\nData Analysis Demo")
    print("=" * 50)
    
    # Sample JSON data
    sample_data = [
        {"name": "Alice", "age": 28, "score": 85, "department": "Engineering"},
        {"name": "Bob", "age": 32, "score": 92, "department": "Marketing"},
        {"name": "Charlie", "age": 25, "score": 78, "department": "Engineering"},
        {"name": "Diana", "age": 35, "score": 95, "department": "Sales"},
        {"name": "Eve", "age": 29, "score": 88, "department": "Engineering"}
    ]
    
    print("Sample Data:")
    for record in sample_data:
        print(f"  {record}")
    
    # Analyze the data
    data_str = json.dumps(sample_data)
    analysis = perform_data_analysis(data_str)
    
    if "error" not in analysis:
        print(f"\nAnalysis Results:")
        print(f"  Data Shape: {analysis['data_shape']}")
        print(f"  Columns: {analysis['columns']}")
        print(f"  Missing Values: {analysis['missing_values']}")
        
        if 'summary_stats' in analysis:
            print(f"\n  Summary Statistics:")
            for col, stats in analysis['summary_stats'].items():
                print(f"    {col}: mean={stats['mean']:.2f}, std={stats['std']:.2f}, range={stats['min']}-{stats['max']}")

def demo_sentiment_analysis():
    """Demonstrate sentiment analysis capabilities."""
    print("\nSentiment Analysis Demo")
    print("=" * 50)
    
    texts = [
        "I absolutely love this amazing product! It's wonderful and fantastic!",
        "This is terrible and awful. I hate it so much.",
        "The product is okay, nothing special but not bad either.",
        "Wow! This is incredible and outstanding! Best purchase ever!",
        "I'm feeling sad and disappointed with this experience."
    ]
    
    for text in texts:
        sentiment_data = analyze_text_sentiment(text)
        if "error" not in sentiment_data:
            print(f"\nText: {text}")
            print(f"  Sentiment: {sentiment_data['sentiment'].upper()}")
            print(f"  Word Count: {sentiment_data['word_count']}")
            print(f"  Scores: Positive={sentiment_data['scores']['positive']:.3f}, "
                  f"Negative={sentiment_data['scores']['negative']:.3f}, "
                  f"Neutral={sentiment_data['scores']['neutral']:.3f}")

def demo_news_and_search():
    """Demonstrate news and search capabilities."""
    print("\nNews and Search Demo")
    print("=" * 50)
    
    # Get news headlines
    print("\nLatest Technology News:")
    tech_news = get_news_headlines("technology")
    if "error" not in tech_news:
        for i, article in enumerate(tech_news['articles'][:3], 1):
            print(f"  {i}. {article['title']}")
            print(f"     {article['description']}")
    
    # Web search
    print("\nWeb Search Results:")
    search_queries = ["artificial intelligence", "machine learning", "data science"]
    for query in search_queries:
        search_results = search_web(query)
        if "error" not in search_results:
            print(f"\n  Query: {query}")
            if search_results['abstract']:
                print(f"  Abstract: {search_results['abstract'][:100]}...")

def demo_github_analysis():
    """Demonstrate GitHub repository analysis."""
    print("\nGitHub Repository Analysis Demo")
    print("=" * 50)
    
    repos = ["openai/openai-python", "pytorch/pytorch", "tensorflow/tensorflow"]
    
    for repo in repos:
        repo_data = get_github_repo_info(repo)
        if "error" not in repo_data:
            print(f"\n{repo}:")
            print(f"  Description: {repo_data['description']}")
            print(f"  Language: {repo_data['language']}")
            print(f"  Stars: {repo_data['stars']:,}")
            print(f"  Forks: {repo_data['forks']:,}")
            print(f"  Open Issues: {repo_data['open_issues']}")

def demo_translation():
    """Demonstrate translation capabilities."""
    print("\nTranslation Demo")
    print("=" * 50)
    
    phrases = ["Hello world", "Good morning", "Thank you", "How are you?"]
    languages = ["es", "fr", "de"]
    
    for phrase in phrases:
        print(f"\nOriginal: {phrase}")
        for lang in languages:
            translation = translate_text(phrase, lang)
            if "error" not in translation:
                print(f"  {lang.upper()}: {translation['translated_text']}")

def demo_math_analysis():
    """Demonstrate mathematical expression analysis."""
    print("\nMathematical Expression Analysis Demo")
    print("=" * 50)
    
    expressions = [
        "2 + 3 * 4",
        "(10 + 5) * 2",
        "100 / 4 + 7 * 3",
        "15 * 2 - 8 / 4 + 6"
    ]
    
    for expr in expressions:
        result = calculate_math_expression(expr)
        if "error" not in result:
            print(f"\nExpression: {expr}")
            print(f"  Result: {result['result']}")
            print(f"  Complexity: {result['complexity']}")
            print(f"  Operations: {result['operations']}")

def demo_weather_and_time():
    """Demonstrate weather and time capabilities."""
    print("\nWeather and Time Demo")
    print("=" * 50)
    
    # Current time in different timezones
    timezones = ["UTC", "EST", "PST", "CET", "JST"]
    print("\nCurrent Time in Different Timezones:")
    for tz in timezones:
        time_data = get_current_time(tz)
        if "error" not in time_data:
            print(f"  {tz}: {time_data['local_time']}")
    
    # Weather information
    cities = ["new york", "london", "tokyo", "sydney"]
    print("\nWeather Information:")
    for city in cities:
        weather_data = get_weather_info(city)
        if "error" not in weather_data:
            print(f"  {city.title()}: {weather_data['temperature']}°F, "
                  f"{weather_data['condition']}, {weather_data['humidity']}% humidity")

def main():
    """Run all demos."""
    print("Enhanced AI Agent System Demo")
    print("This showcases all the new sophisticated functions and real API integrations")
    print("=" * 80)
    
    try:
        # Run all demos
        demo_website_analysis()
        demo_financial_data()
        demo_data_analysis()
        demo_sentiment_analysis()
        demo_news_and_search()
        demo_github_analysis()
        demo_translation()
        demo_math_analysis()
        demo_weather_and_time()
        
        print("\n" + "=" * 80)
        print("All demos completed successfully!")
        print("\nThis demonstrates the enhanced AI agent system with:")
        print("Real API integrations (DuckDuckGo, GitHub)")
        print("Sophisticated data analysis (pandas, numpy)")
        print("Web scraping and analysis (BeautifulSoup)")
        print("Financial data (stocks, crypto)")
        print("News and search capabilities")
        print("Sentiment analysis")
        print("Translation services")
        print("Mathematical expression analysis")
        print("Weather and time information")
        print("Website performance metrics")
        
        print("\nTo run the full AI agent with OpenAI:")
        print("1. Create a .env file with your OPENAI_API_KEY")
        print("2. Run: python3 main.py")
        
    except Exception as e:
        print(f"Error during demo: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
