#!/usr/bin/env python3
"""
Simple example demonstrating the AI Agent system.
This script shows how to use the agent without running the full interactive mode.
"""

import os
from dotenv import load_dotenv
from main import run_ai_agent
from prompts import basic_system_prompt, advanced_system_prompt

# Load environment variables
load_dotenv()

def main():
    """Run a simple example of the AI agent."""
    
    # Check if API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found!")
        print("Please create a .env file with your OpenAI API key:")
        print("OPENAI_API_KEY=your_api_key_here")
        return
    
    print("🤖 AI Agent Example")
    print("=" * 50)
    
    # Example 1: Basic agent with response time
    print("\nExample 1: Basic Agent")
    print("Question: What is the response time for learnwithhasan.com?")
    
    try:
        result = run_ai_agent(
            "What is the response time for learnwithhasan.com?",
            basic_system_prompt
        )
        print(f"Answer: {result}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 2: Advanced agent with multiple functions
    print("\nExample 2: Advanced Agent")
    print("Question: What's the weather like in London and what time is it now?")
    
    try:
        result = run_ai_agent(
            "What's the weather like in London and what time is it now?",
            advanced_system_prompt
        )
        print(f"Answer: {result}")
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 3: Math calculation
    print("\nExample 3: Math Calculation")
    print("Question: Calculate 25 * 4 + 10 and tell me the current time")
    
    try:
        result = run_ai_agent(
            "Calculate 25 * 4 + 10 and tell me the current time",
            advanced_system_prompt
        )
        print(f"Answer: {result}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\nExamples completed!")
    print("\nTo run more examples or use interactive mode, run:")
    print("python main.py")

if __name__ == "__main__":
    main()
