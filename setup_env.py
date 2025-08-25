#!/usr/bin/env python3
"""
Secure Environment Setup Script
This script helps you create your .env file securely without exposing API keys.
"""

import os
import getpass

def create_env_file():
    """Create a .env file with user input."""
    
    print("Secure Environment Setup")
    print("=" * 40)
    print("This script will help you create your .env file securely.")
    print("Your API keys will NOT be stored in the source code.")
    print()
    
    # Check if .env already exists
    if os.path.exists('.env'):
        print(".env file already exists!")
        overwrite = input("Do you want to overwrite it? (y/N): ").strip().lower()
        if overwrite != 'y':
            print("Setup cancelled.")
            return
    
    print("Enter your API keys (press Enter to skip optional ones):")
    print()
    
    # Required API key
    openai_key = getpass.getpass("OpenAI API Key (required): ").strip()
    if not openai_key:
        print("OpenAI API key is required!")
        return
    
    # Optional API keys
    weather_key = input("OpenWeatherMap API Key (optional): ").strip()
    news_key = input("NewsAPI Key (optional): ").strip()
    stock_key = input("Alpha Vantage API Key (optional): ").strip()
    github_token = input("GitHub API Token (optional): ").strip()
    
    # Configuration options
    print("\nConfiguration Options:")
    model = input("OpenAI Model (default: gpt-4): ").strip() or "gpt-4"
    temperature = input("Temperature (default: 0.1): ").strip() or "0.1"
    max_tokens = input("Max Tokens (default: 1000): ").strip() or "1000"
    weather_units = input("Weather Units (default: imperial): ").strip() or "imperial"
    default_language = input("Default Language (default: es): ").strip() or "es"
    
    # Create .env content
    env_content = f"""# OpenAI Configuration
OPENAI_API_KEY={openai_key}

# Optional API Keys (for enhanced functionality)
"""
    
    if weather_key:
        env_content += f"OPENWEATHER_API_KEY={weather_key}\n"
    else:
        env_content += "# OPENWEATHER_API_KEY=your_openweather_api_key_here\n"
    
    if news_key:
        env_content += f"NEWS_API_KEY={news_key}\n"
    else:
        env_content += "# NEWS_API_KEY=your_news_api_key_here\n"
    
    if stock_key:
        env_content += f"ALPHA_VANTAGE_API_KEY={stock_key}\n"
    else:
        env_content += "# ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key_here\n"
    
    if github_token:
        env_content += f"GITHUB_API_TOKEN={github_token}\n"
    else:
        env_content += "# GITHUB_API_TOKEN=your_github_token_here\n"
    
    env_content += f"""
# Configuration Options
OPENAI_MODEL={model}
OPENAI_TEMPERATURE={temperature}
OPENAI_MAX_TOKENS={max_tokens}
WEATHER_UNITS={weather_units}
NEWS_DEFAULT_COUNTRY=us
REQUEST_TIMEOUT=10
DEFAULT_TARGET_LANGUAGE={default_language}
"""
    
    # Write .env file
    try:
        with open('.env', 'w') as f:
            f.write(env_content)
        
        print("\n.env file created successfully!")
        print("Your API keys are now stored locally and securely.")
        print()
        
        # Verify .gitignore
        if os.path.exists('.gitignore'):
            with open('.gitignore', 'r') as f:
                gitignore_content = f.read()
            
            if '.env' in gitignore_content:
                print(".gitignore is properly configured to exclude .env files")
            else:
                print("Warning: .env is not in .gitignore")
        else:
            print("Warning: .gitignore file not found")
        
        print("\nNext steps:")
        print("1. Test your configuration: python3 config.py")
        print("2. Run the enhanced demo: python3 enhanced_demo.py")
        print("3. Test the full AI agent: python3 main.py")
        
    except Exception as e:
        print(f"Error creating .env file: {e}")

def verify_security():
    """Verify that the setup is secure."""
    print("\nSecurity Verification")
    print("=" * 30)
    
    # Check if .env exists
    if os.path.exists('.env'):
        print(".env file exists")
        
        # Check if it's in .gitignore
        if os.path.exists('.gitignore'):
            with open('.gitignore', 'r') as f:
                gitignore_content = f.read()
            
            if '.env' in gitignore_content:
                print(".env is properly excluded in .gitignore")
            else:
                print(".env is NOT excluded in .gitignore")
        else:
            print(".gitignore file not found")
        
        # Check Git status
        print("\nGit Status Check:")
        os.system('git status')
        
    else:
        print(".env file not found")

if __name__ == "__main__":
    print("AI Agent System - Secure Environment Setup")
    print("=" * 50)
    
    while True:
        print("\nChoose an option:")
        print("1. Create/Update .env file")
        print("2. Verify security setup")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            create_env_file()
        elif choice == '2':
            verify_security()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
