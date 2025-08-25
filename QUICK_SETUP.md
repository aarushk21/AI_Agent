# Quick Secure Setup Guide

## **Create Your .env File (SECURELY)**

### **Step 1: Create the .env file manually**

In your project directory, create a file named `.env` (exactly that name, with the dot) and add this content:

```bash
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here

# Optional API Keys (for enhanced functionality)
# OPENWEATHER_API_KEY=your_openweather_api_key_here
# NEWS_API_KEY=your_news_api_key_here
# ALPHA_VANTAGE_API_KEY=your_alpha_vantage_api_key_here
# GITHUB_API_TOKEN=your_github_token_here

# Configuration Options
OPENAI_MODEL=gpt-4
OPENAI_TEMPERATURE=0.1
OPENAI_MAX_TOKENS=1000
WEATHER_UNITS=imperial
NEWS_DEFAULT_COUNTRY=us
REQUEST_TIMEOUT=10
DEFAULT_TARGET_LANGUAGE=es
```

### **Step 2: Verify Security**

Run this command to check that your .env file is NOT tracked by Git:

```bash
git status
```

**Expected result**: You should NOT see `.env` in the list of files.

### **Step 3: Test Your Setup**

```bash
# Test configuration
python3 config.py

# Test enhanced demo
python3 enhanced_demo.py

# Test full AI agent
python3 main.py
```

## **Why This is Secure**

1. **`.env` is in .gitignore** - Git will never track this file
2. **Local only** - File exists only on your computer
3. **No hardcoding** - API keys are not in source code
4. **Template provided** - .env.template shows structure without real keys

## **Important Security Notes**

- **DO**: Keep .env file local only
- **DO**: Use .env.template for sharing project structure
- **DON'T**: Commit .env to Git
- **DON'T**: Share API keys in public repositories
- **DON'T**: Post API keys in chat logs or forums

## **Ready to Test!**

Once you've created your .env file, you can:

1. **Test Configuration**: `python3 config.py`
2. **Run Enhanced Demo**: `python3 enhanced_demo.py`
3. **Use Full AI Agent**: `python3 main.py`

Your API keys are now secure and ready to use!
