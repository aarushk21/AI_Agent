# Enhanced AI Agents with Python and LLMs

This project demonstrates how to create **autonomous AI agents** using Python and Large Language Models (LLMs) from scratch, following the guide from [learnwithhasan.com](https://learnwithhasan.com/blog/create-ai-agents-with-python/).

## What's New in This Enhanced Version

- **Real API Integrations**: DuckDuckGo, GitHub, OpenWeatherMap, NewsAPI, Alpha Vantage
- **Advanced Data Analysis**: Pandas, NumPy integration for sophisticated data processing
- **Web Scraping & Analysis**: BeautifulSoup-powered website metadata extraction
- **Financial Data**: Real-time stock prices and cryptocurrency information
- **News & Search**: Latest headlines and web search capabilities
- **Sentiment Analysis**: Text sentiment analysis with scoring
- **Translation Services**: Multi-language text translation
- **Mathematical Analysis**: Expression evaluation with complexity analysis
- **Performance Monitoring**: Website response time and SEO analysis
- **Specialized Agents**: SEO Auditor, Financial Analyst, Data Scientist

## What is an AI Agent?

An AI Agent is an LLM-powered system that can:
- **Think** about user queries using advanced reasoning
- **Act** by calling external functions and APIs
- **Respond** with intelligent answers based on real-time data
- **Learn** from interactions and improve over time

Unlike traditional LLMs that can only generate responses from training data, AI agents can access real-time information, perform complex calculations, and execute sophisticated actions through external functions.

## Project Structure

```
AI_Agent/
├── actions.py              # 13+ sophisticated action functions
├── prompts.py              # 5 specialized agent prompts
├── main.py                # Enhanced AI agent with GPT-4 integration
├── config.py              # Configuration management and API keys
├── enhanced_demo.py       # Comprehensive demo of all capabilities
├── test_system.py         # Test suite for all components
├── example.py             # Simple usage examples
├── requirements.txt       # Enhanced Python dependencies
├── README.md              # This comprehensive guide
├── SETUP.md               # Quick start guide
└── .env                   # Environment variables (create this)
```

## Quick Start (5 minutes)

### 1. Install Dependencies

```bash
# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows

# Install enhanced dependencies
pip install -r requirements.txt
```

### 2. Set Up API Keys

Create a `.env` file in your project root:

```bash
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Optional (for enhanced functionality)
OPENWEATHER_API_KEY=your_weather_api_key
NEWS_API_KEY=your_news_api_key
ALPHA_VANTAGE_API_KEY=your_stock_api_key
GITHUB_API_TOKEN=your_github_token
```

**Tip**: The system works with mock data if optional API keys are missing!

### 3. Test the System

```bash
# Test without API key (all functions work with mock data)
python3 enhanced_demo.py

# Test system components
python3 test_system.py

# Run with real OpenAI API
python3 main.py
```

## How It Works

### The Enhanced ReAct Loop

The AI agent follows an advanced **ReAct** (Reasoning + Acting) pattern:

1. **Thought**: The LLM thinks about the user's question
2. **Action**: The LLM decides which sophisticated function to call
3. **PAUSE**: The LLM waits for the function result
4. **Action_Response**: The function result is provided
5. **Answer**: The LLM provides intelligent analysis based on results

### Real API Integration Example

**User Question**: "What's the current stock price of Apple and analyze the latest business news?"

1. **LLM Response**: 
   ```
   Thought: I need to get Apple's stock price and recent business news.
   Action: {"function_name": "get_stock_price", "function_parms": {"symbol": "AAPL"}}
   PAUSE
   ```

2. **Function Execution**: `get_stock_price("AAPL")` returns real-time data
3. **News Analysis**: `get_news_headlines("business")` returns latest headlines
4. **Final Answer**: Comprehensive analysis combining stock data and news context

## Available Functions

### Web & Performance
- **`get_response_time(url)`**: Real website response time and performance metrics
- **`get_website_info(url)`**: Comprehensive website analysis (SEO, content, structure)
- **`search_web(query)`**: Web search using DuckDuckGo API

### Weather & Time
- **`get_weather_info(city)`**: Real weather data with OpenWeatherMap API
- **`get_current_time(timezone)`**: Current time with timezone conversion

### Financial & Markets
- **`get_stock_price(symbol)`**: Real-time stock prices via Alpha Vantage
- **`get_crypto_price(symbol)`**: Cryptocurrency prices and market data
- **`get_news_headlines(category)`**: Latest news via NewsAPI

### Data & Analysis
- **`perform_data_analysis(data)`**: Advanced data analysis with pandas/NumPy
- **`analyze_text_sentiment(text)`**: Sentiment analysis with scoring
- **`calculate_math_expression(expr)`**: Mathematical analysis with complexity assessment

### Development & Code
- **`get_github_repo_info(repo)`**: GitHub repository analysis
- **`translate_text(text, language)`**: Multi-language translation

## Agent Specializations

### 1. **Basic Agent** 
- Response time analysis only
- Perfect for learning the core concept

### 2. **Advanced Agent**
- Access to all 13+ functions
- Handles complex multi-step queries

### 3. **SEO Auditor Agent**
- Specialized for website optimization
- Combines performance and content analysis

### 4. **Financial Analyst Agent**
- Stock prices, crypto, and business news
- Market analysis and insights

### 5. **Data Scientist Agent**
- Data analysis, sentiment analysis, math
- Statistical insights and processing

## Example Queries

### Website Analysis
- "Analyze the SEO performance of learnwithhasan.com"
- "What's the response time and structure of github.com?"

### Financial Analysis
- "What's the current stock price of Apple and any recent business news?"
- "Get the latest cryptocurrency prices for BTC and ETH"

### Data Science
- "Analyze this dataset: [{'name': 'Alice', 'age': 28, 'score': 85}]"
- "What's the sentiment of this text: 'I love this amazing product!'"

### Research & Search
- "Search for information about machine learning and AI"
- "Get the latest technology news headlines"

## Configuration & Customization

### Environment Variables

```bash
# Core OpenAI Settings
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4
OPENAI_TEMPERATURE=0.1

# API Integrations
OPENWEATHER_API_KEY=your_key
NEWS_API_KEY=your_key
ALPHA_VANTAGE_API_KEY=your_key

# Customization
WEATHER_UNITS=imperial
DEFAULT_TARGET_LANGUAGE=es
REQUEST_TIMEOUT=10
```

### Adding New Functions

1. **Define the function** in `actions.py`
2. **Add it to available actions** in `main.py`
3. **Update system prompts** in `prompts.py`
4. **Test with** `python3 test_system.py`

## Advanced Features

### Model Selection
```python
# Choose from multiple OpenAI models
result = run_ai_agent(question, system_prompt, model="gpt-4")
result = run_ai_agent(question, system_prompt, model="gpt-3.5-turbo")
result = run_ai_agent(question, system_prompt, model="gpt-4-turbo")
```

### Function Chaining
The agent automatically chains multiple functions for complex queries:
- Weather + Time + News for comprehensive analysis
- Stock prices + News + Sentiment for market insights
- Website analysis + Performance + SEO for optimization

### Error Handling
- Graceful fallback to mock data when APIs are unavailable
- Comprehensive error reporting and debugging
- Rate limiting and timeout protection

## Troubleshooting

### Common Issues

1. **"OPENAI_API_KEY not found"**
   - Create `.env` file with your API key
   - Verify the key format: `OPENAI_API_KEY=sk-...`

2. **API rate limits**
   - Check your API provider's rate limits
   - Consider upgrading to paid plans for higher limits

3. **Function execution errors**
   - Check console output for detailed error messages
   - Verify function parameters in the JSON output

### Getting Help

- Run `python3 config.py` to check configuration status
- Use `python3 test_system.py` to verify all components
- Check the console output for detailed error messages

## Next Steps & Extensions

### Immediate Enhancements
1. **Add more APIs**: Integrate with additional services
2. **Custom functions**: Build domain-specific actions
3. **Memory system**: Implement conversation history
4. **Multi-agent coordination**: Coordinate multiple specialized agents

### Advanced Features
1. **Function calling**: Use OpenAI's native function calling
2. **Vector databases**: Add semantic search capabilities
3. **Streaming responses**: Real-time agent responses
4. **Custom models**: Integrate with other LLM providers

### Production Deployment
1. **Docker containerization**: Easy deployment
2. **API endpoints**: RESTful API for the agent system
3. **Authentication**: Secure access control
4. **Monitoring**: Performance and usage analytics

## Use Cases

### Business Applications
- **Market Research**: Stock analysis + news sentiment
- **SEO Optimization**: Website performance + content analysis
- **Competitive Analysis**: Multi-website comparison
- **Content Creation**: Research + sentiment analysis

### Development & DevOps
- **Code Analysis**: GitHub repository insights
- **Performance Monitoring**: Website response times
- **API Testing**: Function execution and validation
- **Documentation**: Automated content generation

### Data Science
- **Data Analysis**: JSON/CSV processing
- **Sentiment Analysis**: Text classification
- **Statistical Analysis**: Mathematical computations
- **Research**: Web search + data synthesis

## Resources & Learning

- [Original Guide](https://learnwithhasan.com/blog/create-ai-agents-with-python/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [BeautifulSoup Guide](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

## Contributing

This project is open for contributions! Areas for improvement:
- Additional API integrations
- New specialized agents
- Enhanced error handling
- Performance optimizations
- Documentation improvements

## License

This project is for educational and commercial use. Feel free to modify and extend it for your own projects.

---

**Ready to build intelligent AI agents? Start with the enhanced demo:**

```bash
python3 enhanced_demo.py
```

**Then dive into the full system:**

```bash
python3 main.py
```

**Happy coding!**
