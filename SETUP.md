# Quick Setup Guide for AI Agents

This guide will help you get your AI agent system up and running quickly!

## Prerequisites

- Python 3.8+ installed
- OpenAI API key (get one from [OpenAI Platform](https://platform.openai.com/api-keys))
- Basic Python knowledge

## Quick Start (5 minutes)

### 1. Install Dependencies

```bash
# Activate your virtual environment
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

# Install required packages
pip install -r requirements.txt
```

### 2. Set Up API Key

Create a `.env` file in your project root:

```bash
# .env file
OPENAI_API_KEY=sk-your-actual-api-key-here
```

**Important**: Replace `sk-your-actual-api-key-here` with your real OpenAI API key!

### 3. Test the System

```bash
# Test without API key (simulation)
python demo.py

# Test system components
python test_system.py

# Run with real OpenAI API
python main.py
```

## What to Try First

### Demo Mode (No API Key Required)
```bash
python demo.py
```
This shows how the ReAct loop works with simulated LLM responses.

### Basic Testing
```bash
python test_system.py
```
This verifies all the action functions work correctly.

### Full AI Agent (Requires API Key)
```bash
python main.py
```
This runs the complete AI agent with OpenAI integration.

## Troubleshooting

### Common Issues

1. **"OPENAI_API_KEY not found"**
   - Make sure you created the `.env` file
   - Check the file is in the project root directory
   - Verify the format: `OPENAI_API_KEY=sk-...`

2. **Import errors**
   - Make sure you're in the virtual environment
   - Run `pip install -r requirements.txt` again

3. **API errors**
   - Verify your OpenAI API key is valid
   - Check you have sufficient API credits
   - Ensure your internet connection works

### Getting Help

- Check the console output for detailed error messages
- Verify all files are in the correct locations
- Make sure your virtual environment is activated

## Next Steps

Once you have the basic system working:

1. **Customize Functions**: Add new actions in `actions.py`
2. **Create New Agents**: Design specialized prompts in `prompts.py`
3. **Integrate Real APIs**: Replace mock functions with actual API calls
4. **Build Applications**: Use the agent in your own projects

## Example Use Cases

- **Website Monitoring**: Check response times and performance
- **Data Analysis**: Process and analyze information
- **Task Automation**: Automate repetitive workflows
- **Content Generation**: Create content with real-time data
- **Decision Support**: Make informed decisions with current information

## Learn More

- [Original Guide](https://learnwithhasan.com/blog/create-ai-agents-with-python/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [ReAct Paper](https://arxiv.org/abs/2210.03629)

---

**Happy coding!**

If you run into issues, check the troubleshooting section above or refer to the main README.md for detailed documentation.
