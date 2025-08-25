#!/usr/bin/env python3
"""
Configuration file for the Enhanced AI Agent System
Contains API keys, settings, and configuration options for all integrated services.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for the AI Agent System."""
    
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    OPENAI_TEMPERATURE = float(os.getenv("OPENAI_TEMPERATURE", "0.1"))
    OPENAI_MAX_TOKENS = int(os.getenv("OPENAI_MAX_TOKENS", "1000"))
    
    # Weather API Configuration
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
    WEATHER_UNITS = os.getenv("WEATHER_UNITS", "imperial")  # metric, imperial, kelvin
    
    # News API Configuration
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    NEWS_DEFAULT_COUNTRY = os.getenv("NEWS_DEFAULT_COUNTRY", "us")
    NEWS_DEFAULT_CATEGORY = os.getenv("NEWS_DEFAULT_CATEGORY", "general")
    
    # Stock Market API Configuration
    ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
    
    # Web Scraping Configuration
    REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "10"))
    USER_AGENT = os.getenv("USER_AGENT", "AI-Agent-System/1.0")
    
    # Data Analysis Configuration
    MAX_DATA_ROWS = int(os.getenv("MAX_DATA_ROWS", "10000"))
    MAX_DATA_COLUMNS = int(os.getenv("MAX_DATA_COLUMNS", "100"))
    
    # Translation Configuration
    DEFAULT_TARGET_LANGUAGE = os.getenv("DEFAULT_TARGET_LANGUAGE", "es")
    SUPPORTED_LANGUAGES = ["es", "fr", "de", "it", "pt", "ru", "ja", "ko", "zh"]
    
    # GitHub API Configuration
    GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")  # Optional, for higher rate limits
    GITHUB_RATE_LIMIT = int(os.getenv("GITHUB_RATE_LIMIT", "60"))  # requests per hour
    
    # Crypto API Configuration
    CRYPTO_UPDATE_INTERVAL = int(os.getenv("CRYPTO_UPDATE_INTERVAL", "300"))  # 5 minutes
    
    # Sentiment Analysis Configuration
    SENTIMENT_POSITIVE_THRESHOLD = float(os.getenv("SENTIMENT_POSITIVE_THRESHOLD", "0.1"))
    SENTIMENT_NEGATIVE_THRESHOLD = float(os.getenv("SENTIMENT_NEGATIVE_THRESHOLD", "0.1"))
    
    # Website Analysis Configuration
    MAX_WEBSITE_SIZE = int(os.getenv("MAX_WEBSITE_SIZE", "10485760"))  # 10MB
    MAX_ANALYSIS_TIME = int(os.getenv("MAX_ANALYSIS_TIME", "30"))  # seconds
    
    @classmethod
    def validate_config(cls):
        """Validate that required configuration is present."""
        missing_keys = []
        
        if not cls.OPENAI_API_KEY:
            missing_keys.append("OPENAI_API_KEY")
        
        # Optional API keys (system will work with mock data if missing)
        optional_keys = [
            "OPENWEATHER_API_KEY",
            "NEWS_API_KEY", 
            "ALPHA_VANTAGE_API_KEY",
            "GITHUB_API_TOKEN"
        ]
        
        print("Configuration Status:")
        print(f"  OpenAI API Key: {'Set' if cls.OPENAI_API_KEY else 'Missing (Required)'}")
        
        for key in optional_keys:
            value = getattr(cls, key)
            status = "Set" if value else "Missing (Will use mock data)"
            print(f"  {key}: {status}")
        
        if missing_keys:
            print(f"\nRequired configuration missing: {', '.join(missing_keys)}")
            print("Please set these in your .env file")
            return False
        
        print("\nConfiguration validated successfully!")
        return True
    
    @classmethod
    def get_api_status(cls):
        """Get status of all API integrations."""
        status = {
            "openai": bool(cls.OPENAI_API_KEY),
            "weather": bool(cls.OPENWEATHER_API_KEY),
            "news": bool(cls.NEWS_API_KEY),
            "stocks": bool(cls.ALPHA_VANTAGE_API_KEY),
            "github": bool(cls.GITHUB_API_TOKEN)
        }
        return status

# Example .env file template
ENV_TEMPLATE = """
# Required API Keys
OPENAI_API_KEY=your_openai_api_key_here

# Optional API Keys (for enhanced functionality)
OPENWEATHER_API_KEY=your_openweather_api_key_here
NEWS_API_KEY=your_news_api_key_here
ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key_here
GITHUB_API_TOKEN=your_github_token_here

# Configuration Options
OPENAI_MODEL=gpt-4
OPENAI_TEMPERATURE=0.1
OPENAI_MAX_TOKENS=1000
WEATHER_UNITS=imperial
NEWS_DEFAULT_COUNTRY=us
REQUEST_TIMEOUT=10
DEFAULT_TARGET_LANGUAGE=es
"""

def create_env_template():
    """Create a .env.template file for users."""
    try:
        with open(".env.template", "w") as f:
            f.write(ENV_TEMPLATE.strip())
        print("Created .env.template file")
        print("Copy this file to .env and fill in your API keys")
    except Exception as e:
        print(f"Error creating .env.template: {e}")

if __name__ == "__main__":
    # Validate configuration
    Config.validate_config()
    
    # Show API status
    print(f"\nAPI Integration Status:")
    api_status = Config.get_api_status()
    for service, status in api_status.items():
        print(f"  {service.title()}: {'Active' if status else 'Mock Data'}")
    
    # Create .env template if it doesn't exist
    if not os.path.exists(".env.template"):
        create_env_template()
