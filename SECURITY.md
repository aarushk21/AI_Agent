# Security Guide for AI Agent System

## **IMPORTANT: Protect Your API Keys**

Your OpenAI API key is **sensitive information** that should never be shared or committed to version control.

## **What NOT to Do**

**Never commit your .env file to GitHub**
**Never share your API key in public repositories**
**Never hardcode API keys in your source code**
**Never post API keys in chat logs or forums**

## **What TO Do**

### 1. **Create Your .env File (Locally Only)**

Create a `.env` file in your project root with this content:

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

### 2. **Verify .gitignore is Working**

The `.gitignore` file should already be configured to exclude:
- `.env` files
- API key files
- Secret files
- Credential files

### 3. **Check Git Status**

Before committing, verify your .env file is not tracked:

```bash
git status
```

You should **NOT** see `.env` in the list of tracked files.

## **Verification Steps**

### Step 1: Check if .env is Tracked
```bash
git ls-files | grep .env
```
**Expected result**: No output (file should not be tracked)

### Step 2: Check Git Status
```bash
git status
```
**Expected result**: `.env` should not appear in any section

### Step 3: Test Configuration
```bash
python3 config.py
```
**Expected result**: Should show your API key is configured

## **Testing Your Secure Setup**

### 1. **Test Configuration**
```bash
python3 config.py
```

### 2. **Test Enhanced Demo**
```bash
python3 enhanced_demo.py
```

### 3. **Test Full AI Agent**
```bash
python3 main.py
```

## **Troubleshooting**

### If .env is Still Tracked

If Git is still tracking your .env file:

```bash
# Remove from Git tracking (but keep the file locally)
git rm --cached .env

# Commit the removal
git commit -m "Remove .env file from tracking"

# Verify it's no longer tracked
git status
```

### If You Accidentally Committed API Keys

**IMMEDIATE ACTION REQUIRED:**

1. **Revoke the API key** in your OpenAI dashboard
2. **Generate a new API key**
3. **Update your local .env file**
4. **Remove from Git history** (if possible)
5. **Force push** to remove from remote repository

## **Environment Variables for Production**

For production deployments, use environment variables instead of .env files:

```bash
# Set environment variables
export OPENAI_API_KEY="your_api_key_here"

# Or in your deployment platform
OPENAI_API_KEY=your_api_key_here
```

## **Mobile/Cloud Development**

### GitHub Codespaces
- Use repository secrets
- Set environment variables in codespace settings

### VS Code Remote
- Use remote environment variables
- Don't sync .env files

### Docker
- Use Docker secrets
- Pass environment variables at runtime

## **Additional Security Measures**

### 1. **API Key Rotation**
- Rotate API keys regularly
- Use different keys for different environments

### 2. **Access Control**
- Limit API key permissions
- Monitor API usage

### 3. **Audit Logs**
- Keep track of API key usage
- Monitor for suspicious activity

## **Security Checklist**

- [ ] `.env` file created locally
- [ ] `.env` file NOT committed to Git
- [ ] `.gitignore` properly configured
- [ ] API key working in local tests
- [ ] Git status shows no .env file
- [ ] Ready to push to GitHub safely

## **Emergency Contacts**

If you accidentally expose your API key:

1. **OpenAI Support**: [OpenAI Help Center](https://help.openai.com/)
2. **GitHub Support**: [GitHub Support](https://support.github.com/)
3. **Revoke Key Immediately**: [OpenAI API Keys](https://platform.openai.com/api-keys)

---

**Remember: Security is everyone's responsibility. Keep your API keys safe!**
