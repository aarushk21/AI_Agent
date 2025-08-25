import json
import re
import os
from openai import OpenAI
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

# Create an instance of the OpenAI class (will be initialized when needed)
openai_client = None

def generate_text_with_conversation(messages, model="gpt-3.5-turbo"):
    """
    Generate text using OpenAI API with conversation context.
    """
    global openai_client
    
    # Initialize OpenAI client if not already done
    if openai_client is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            return "Error: OPENAI_API_KEY not found in environment variables"
        openai_client = OpenAI(api_key=api_key)
    
    try:
        response = openai_client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.1,  # Lower temperature for more consistent function calling
            max_tokens=1000
        )
        return response.choices[0].message.content
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

def run_ai_agent(user_question, system_prompt=basic_system_prompt, model="gpt-3.5-turbo"):
    """
    Run the AI agent with the ReAct loop.
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
        
        # Generate response from LLM
        response = generate_text_with_conversation(messages, model)
        print(f"LLM Response: {response}")
        
        # Check if response contains PAUSE (indicating function execution needed)
        if "PAUSE" in response:
            # Extract function call
            json_function = extract_json(response)
            
            if json_function:
                function_name = json_function.get("function_name")
                function_params = json_function.get("function_parms", {})
                
                print(f"Executing function: {function_name} with params: {function_params}")
                
                # Execute the function
                function_result = execute_function(function_name, function_params)
                print(f"Function result: {function_result}")
                
                # Add the function result to messages for next iteration
                function_result_message = f"Action_Response: {function_result}"
                messages.append({"role": "assistant", "content": response})
                messages.append({"role": "user", "content": function_result_message})
            else:
                print("No valid function call found in response")
                break
        else:
            # No PAUSE found, agent has provided final answer
            print("Final answer received!")
            break
    
    return response

def test_basic_agent():
    """
    Test the basic AI agent with a simple question.
    """
    print("=== Testing Basic AI Agent ===")
    question = "What is the response time for learnwithhasan.com?"
    result = run_ai_agent(question, basic_system_prompt)
    print(f"\nFinal Result: {result}")

def test_advanced_agent():
    """
    Test the advanced AI agent with multiple functions.
    """
    print("\n=== Testing Advanced AI Agent ===")
    question = "What is the weather like in London and what time is it now?"
    result = run_ai_agent(question, advanced_system_prompt)
    print(f"\nFinal Result: {result}")

def test_seo_auditor():
    """
    Test the SEO Auditor AI agent.
    """
    print("\n=== Testing SEO Auditor AI Agent ===")
    question = "Is the website learnwithhasan.com fast enough for good SEO?"
    result = run_ai_agent(question, seo_auditor_prompt)
    print(f"\nFinal Result: {result}")

def test_financial_analyst():
    """
    Test the Financial Analyst AI agent.
    """
    print("\n=== Testing Financial Analyst AI Agent ===")
    question = "What is the current stock price of Apple and any recent business news?"
    result = run_ai_agent(question, financial_analyst_prompt)
    print(f"\nFinal Result: {result}")

def test_data_scientist():
    """
    Test the Data Scientist AI agent.
    """
    print("\n=== Testing Data Scientist AI Agent ===")
    question = "analyze this data: [{\"name\": \"Alice\", \"age\": 28, \"score\": 85}, {\"name\": \"Bob\", \"age\": 32, \"score\": 92}]"
    result = run_ai_agent(question, data_scientist_prompt)
    print(f"\nFinal Result: {result}")

def interactive_mode():
    """
    Run the AI agent in interactive mode.
    """
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
            model_choice = input("Select model (1: gpt-4, 2: gpt-3.5-turbo, 3: gpt-4-turbo): ").strip()
            if model_choice == "1":
                model = "gpt-4"
            elif model_choice == "2":
                model = "gpt-3.5-turbo"
            elif model_choice == "3":
                model = "gpt-4-turbo"
            else:
                model = "gpt-4"
                print("Using default model: gpt-4")
            
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

if __name__ == "__main__":
    # Check if OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key:")
        print("OPENAI_API_KEY=your_api_key_here")
        print("\nYou can still test the system components without an API key:")
        print("python test_system.py")
        exit(1)
    
    print("🤖 Enhanced AI Agent System Initialized!")
    print("Make sure you have set your OPENAI_API_KEY in the .env file")
    print()
    
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
        print("Make sure your OpenAI API key is valid and you have sufficient credits.")
