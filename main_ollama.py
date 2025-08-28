#!/usr/bin/env python3
"""
Enhanced AI Agent System using Ollama (Local LLM)
This provides unlimited AI responses without OpenAI quota limits.
"""

import json
import re
import os
from ollama import Client
from dotenv import load_dotenv
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
from prompts import (
    basic_system_prompt, 
    advanced_system_prompt, 
    seo_auditor_prompt,
    financial_analyst_prompt,
    data_scientist_prompt
)

# Load environment variables
load_dotenv()

# Create Ollama client
ollama_client = Client(host='http://localhost:11434')

def generate_text_with_conversation(messages, model="llama3.1:8b"):
    """
    Generate text using Ollama with conversation context.
    """
    try:
        # Convert OpenAI format to Ollama format
        prompt = ""
        for msg in messages:
            if msg["role"] == "system":
                prompt += f"System: {msg['content']}\n\n"
            elif msg["role"] == "user":
                prompt += f"User: {msg['content']}\n\n"
            elif msg["role"] == "assistant":
                prompt += f"Assistant: {msg['content']}\n\n"
        
        prompt += "Assistant: "
        
        # Debug output
        print(f"Debug: Using model: {model}")
        print(f"Debug: Prompt length: {len(prompt)} characters")
        
        response = ollama_client.generate(
            model=model,
            prompt=prompt,
            options={
                'temperature': 0.1,
                'num_predict': 1000
            }
        )
        return response.response
    except Exception as e:
        return f"Error: {str(e)}"

def extract_json(response):
    """
    Extract JSON function calls from the LLM response.
    """
    # Look for JSON patterns in the response - more flexible pattern
    json_pattern = r'\{[^{}]*"function_name"[^{}]*"function_parms"[^{}]*\}'
    matches = re.findall(json_pattern, response)
    
    if matches:
        try:
            # Try to parse the first match
            return json.loads(matches[0])
        except json.JSONDecodeError:
            return None
    
    # If the above pattern doesn't work, try a more general approach
    try:
        # Look for JSON-like structures
        start = response.find('{')
        end = response.rfind('}')
        if start != -1 and end != -1 and end > start:
            json_str = response[start:end+1]
            return json.loads(json_str)
    except (json.JSONDecodeError, ValueError):
        pass
    
    return None

def execute_function(function_name, function_params):
    """
    Execute the specified function with the given parameters.
    """
    available_actions = {
        "get_response_time": get_response_time,
        "get_weather_info": get_weather_info,
        "calculate_math_expression": calculate_math_expression,
        "get_current_time": get_current_time,
        "search_web": search_web,
        "get_stock_price": get_stock_price,
        "get_news_headlines": get_news_headlines,
        "analyze_text_sentiment": analyze_text_sentiment,
        "get_website_info": get_website_info,
        "perform_data_analysis": perform_data_analysis,
        "translate_text": translate_text,
        "get_crypto_price": get_crypto_price,
        "get_github_repo_info": get_github_repo_info
    }
    
    if function_name in available_actions:
        try:
            if function_params:
                result = available_actions[function_name](**function_params)
            else:
                result = available_actions[function_name]()
            return str(result)
        except Exception as e:
            return f"Error executing {function_name}: {str(e)}"
    else:
        return f"Function {function_name} not found"

def run_ai_agent(user_question, system_prompt=basic_system_prompt, model="llama3.1:8b"):
    """
    Run the AI agent with the ReAct loop using Ollama.
    """
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_question}
    ]
    
    max_iterations = 5  # Prevent infinite loops
    iteration = 0
    
    while iteration < max_iterations:
        iteration += 1
        print(f"\n--- Iteration {iteration} ---")
        
        # Generate response from Ollama
        llm_response = generate_text_with_conversation(messages, model)
        print(f"LLM Response: {llm_response}")
        
        # Extract function call
        function_call = extract_json(llm_response)
        
        if function_call and "function_name" in function_call:
            function_name = function_call["function_name"]
            function_params = function_call.get("function_parms", {})
            
            print(f"Executing function: {function_name} with params: {function_params}")
            
            # Execute the function
            result = execute_function(function_name, function_params)
            print(f"Function result: {result}")
            
            # Add assistant and function result to conversation
            messages.append({"role": "assistant", "content": llm_response})
            messages.append({"role": "user", "content": f"Function result: {result}"})
            
        else:
            print("No function call detected, providing final answer")
            print("Final answer received!")
            return llm_response
    
    return "Maximum iterations reached. Please try a simpler question."

def test_basic_agent():
    """Test the basic AI agent."""
    print("\n=== Testing Basic AI Agent ===")
    question = "What is the response time of google.com?"
    result = run_ai_agent(question, basic_system_prompt)
    print(f"Final Result: {result}")

def test_advanced_agent():
    """Test the advanced AI agent."""
    print("\n=== Testing Advanced AI Agent ===")
    question = "What's the weather like in London and what's the current time?"
    result = run_ai_agent(question, advanced_system_prompt)
    print(f"Final Result: {result}")

def test_seo_auditor():
    """Test the SEO auditor agent."""
    print("\n=== Testing SEO Auditor AI Agent ===")
    question = "Analyze the website learnwithhasan.com for SEO metrics"
    result = run_ai_agent(question, seo_auditor_prompt)
    print(f"Final Result: {result}")

def test_financial_analyst():
    """Test the financial analyst agent."""
    print("\n=== Testing Financial Analyst AI Agent ===")
    question = "What are the current stock prices for AAPL and GOOGL?"
    result = run_ai_agent(question, financial_analyst_prompt)
    print(f"Final Result: {result}")

def test_data_scientist():
    """Test the data scientist agent."""
    print("\n=== Testing Data Scientist AI Agent ===")
    question = "Analyze this data: [{'name': 'John', 'age': 30, 'score': 85}]"
    result = run_ai_agent(question, data_scientist_prompt)
    print(f"Final Result: {result}")

def interactive_mode():
    """Interactive mode for user questions."""
    print("\n" + "="*50)
    print("=== AI Agent Interactive Mode ===")
    print("Available modes:")
    print("1. Basic Agent (response time only)")
    print("2. Advanced Agent (multiple functions)")
    print("3. SEO Auditor Agent")
    print("4. Financial Analyst Agent")
    print("5. Data Scientist Agent")
    print("6. Exit")
    
    while True:
        try:
            choice = input("\nSelect mode (1-6): ").strip()
            
            if choice == "1":
                system_prompt = basic_system_prompt
                print("Basic Agent mode selected")
            elif choice == "2":
                system_prompt = advanced_system_prompt
                print("Advanced Agent mode selected")
            elif choice == "3":
                system_prompt = seo_auditor_prompt
                print("SEO Auditor Agent mode selected")
            elif choice == "4":
                system_prompt = financial_analyst_prompt
                print("Financial Analyst Agent mode selected")
            elif choice == "5":
                system_prompt = data_scientist_prompt
                print("Data Scientist Agent mode selected")
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select 1-6.")
                continue
            
            # Model selection
            model_choice = input("Select model (1: llama3.1:8b, 2: llama3.1:70b, 3: mistral:7b): ").strip()
            if model_choice == "1":
                model = "llama3.1:8b"
            elif model_choice == "2":
                model = "llama3.1:70b"
            elif model_choice == "3":
                model = "mistral:7b"
            else:
                model = "llama3.1:8b"
                print("Using default model: llama3.1:8b")
            
            question = input("Enter your question: ").strip()
            if question.lower() in ['quit', 'exit', 'q']:
                break
                
            result = run_ai_agent(question, system_prompt, model)
            print(f"\nFinal Answer: {result}")
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f"Error: {e}")

def show_available_functions():
    """
    Display all available functions and their descriptions.
    """
    print("=== Available Functions ===")
    functions = {
        "get_response_time": "Get website response time and performance metrics",
        "get_weather_info": "Get weather information for a city",
        "calculate_math_expression": "Calculate mathematical expressions with analysis",
        "get_current_time": "Get current time with timezone info",
        "search_web": "Search the web using DuckDuckGo",
        "get_stock_price": "Get real-time stock prices",
        "get_news_headlines": "Get latest news headlines",
        "analyze_text_sentiment": "Analyze text sentiment",
        "get_website_info": "Get comprehensive website information",
        "perform_data_analysis": "Analyze JSON/CSV data",
        "translate_text": "Translate text to different languages",
        "get_crypto_price": "Get cryptocurrency prices",
        "get_github_repo_info": "Get GitHub repository information"
    }
    
    for func, desc in functions.items():
        print(f"• {func}: {desc}")
    print()

def check_ollama_status():
    """Check if Ollama is running and models are available."""
    try:
        models = ollama_client.list()
        print("✅ Ollama is running!")
        print("Available models:")
        for model in models.models:
            print(f"  • {model.model} ({model.size})")
        return True
    except Exception as e:
        print(f"❌ Ollama error: {e}")
        print("Make sure Ollama is running: brew services start ollama")
        return False

if __name__ == "__main__":
    print("🤖 Enhanced AI Agent System with Ollama (Local LLM)")
    print("No API quotas! Unlimited AI responses!")
    print()
    
    # Check Ollama status
    if not check_ollama_status():
        exit(1)
    
    # Show available functions
    show_available_functions()
    
    # Run tests
    try:
        test_basic_agent()
        test_advanced_agent()
        test_seo_auditor()
        test_financial_analyst()
        test_data_scientist()
        
        # Interactive mode
        print("\n" + "="*50)
        interactive_mode()
        
    except Exception as e:
        print(f"Error running agent: {e}")
        print("Make sure Ollama is running and models are downloaded.")
