#!/usr/bin/env python3
"""
Demo script that simulates the AI agent workflow.
This shows how the ReAct loop works without requiring an OpenAI API key.
"""

import json
from actions import (
    get_response_time, 
    get_weather_info, 
    calculate_math_expression, 
    get_current_time, 
    search_web
)

def simulate_llm_response(question, system_prompt):
    """
    Simulate LLM responses based on the question and system prompt.
    This demonstrates how the ReAct loop would work.
    """
    
    # Simple rule-based responses for demonstration
    if "response time" in question.lower() or "fast" in question.lower():
        if "learnwithhasan.com" in question:
            return {
                "thought": "I should check the response time for learnwithhasan.com",
                "action": {
                    "function_name": "get_response_time",
                    "function_parms": {"url": "learnwithhasan.com"}
                },
                "pause": True
            }
        elif "google.com" in question:
            return {
                "thought": "I should check the response time for google.com",
                "action": {
                    "function_name": "get_response_time",
                    "function_parms": {"url": "google.com"}
                },
                "pause": True
            }
    
    elif "weather" in question.lower():
        if "london" in question.lower():
            return {
                "thought": "I need to get weather information for London",
                "action": {
                    "function_name": "get_weather_info",
                    "function_parms": {"city": "london"}
                },
                "pause": True
            }
        elif "tokyo" in question.lower():
            return {
                "thought": "I need to get weather information for Tokyo",
                "action": {
                    "function_name": "get_weather_info",
                    "function_parms": {"city": "tokyo"}
                },
                "pause": True
            }
    
    elif "calculate" in question.lower() or "math" in question.lower():
        # Extract simple math expressions
        if "25 * 4 + 10" in question:
            return {
                "thought": "I need to calculate the mathematical expression 25 * 4 + 10",
                "action": {
                    "function_name": "calculate_math_expression",
                    "function_parms": {"expression": "25 * 4 + 10"}
                },
                "pause": True
            }
    
    elif "time" in question.lower() and "now" in question.lower():
        return {
            "thought": "I need to get the current time",
            "action": {
                "function_name": "get_current_time",
                "function_parms": {}
            },
            "pause": True
        }
    
    # Default response for unknown questions
    return {
        "thought": "I don't have a specific action for this question",
        "action": None,
        "pause": False
    }

def execute_function(function_name, function_params):
    """
    Execute the specified function with the given parameters.
    """
    available_actions = {
        "get_response_time": get_response_time,
        "get_weather_info": get_weather_info,
        "calculate_math_expression": calculate_math_expression,
        "get_current_time": get_current_time,
        "search_web": search_web
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

def run_demo_agent(question, system_prompt):
    """
    Run the demo AI agent with the ReAct loop.
    """
    print(f"\nAI Agent Demo")
    print(f"Question: {question}")
    print("=" * 60)
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question}
    ]
    
    max_iterations = 3
    iteration = 0
    
    while iteration < max_iterations:
        iteration += 1
        print(f"\n--- Iteration {iteration} ---")
        
        # Simulate LLM response
        llm_response = simulate_llm_response(question, system_prompt)
        
        print(f"Thought: {llm_response['thought']}")
        
        if llm_response['action']:
            print(f"Action: {json.dumps(llm_response['action'], indent=2)}")
            print("PAUSE")
            
            # Execute the function
            function_name = llm_response['action']['function_name']
            function_params = llm_response['action']['function_parms']
            
            print(f"Executing function: {function_name} with params: {function_params}")
            function_result = execute_function(function_name, function_params)
            print(f"Function result: {function_result}")
            
            # Add the function result to messages for next iteration
            action_response = f"Action_Response: {function_result}"
            messages.append({"role": "assistant", "content": f"Thought: {llm_response['thought']}\nAction: {json.dumps(llm_response['action'])}\nPAUSE"})
            messages.append({"role": "user", "content": action_response})
            
            # Generate final answer based on function result
            if "response time" in question.lower():
                if "learnwithhasan.com" in question:
                    return f"Answer: The response time for learnwithhasan.com is {function_result} seconds."
                elif "google.com" in question:
                    return f"Answer: The response time for google.com is {function_result} seconds."
            elif "weather" in question.lower():
                if "london" in question.lower():
                    return f"Answer: The weather in London is currently {function_result}."
                elif "tokyo" in question.lower():
                    return f"Answer: The weather in Tokyo is currently {function_result}."
            elif "calculate" in question.lower():
                if "25 * 4 + 10" in question:
                    return f"Answer: The calculation 25 * 4 + 10 equals {function_result}."
            elif "time" in question.lower():
                return f"Answer: The current time is {function_result}."
            
        else:
            print("No action needed")
            break
    
    return "Answer: I couldn't process this question with the available functions."

def main():
    """Run the demo with different example questions."""
    print("AI Agent System Demo")
    print("This demo simulates how the ReAct loop works")
    print("=" * 60)
    
    # Example questions
    examples = [
        "What is the response time for learnwithhasan.com?",
        "What's the weather like in London?",
        "Calculate 25 * 4 + 10 and tell me the current time",
        "How fast is google.com?"
    ]
    
    basic_prompt = "You are an AI agent that can think, act, and respond to questions."
    
    for i, question in enumerate(examples, 1):
        print(f"\nExample {i}:")
        result = run_demo_agent(question, basic_prompt)
        print(f"\nFinal Result: {result}")
        print("-" * 60)
    
    print("\nDemo completed!")
    print("\nThis demonstrates the ReAct loop:")
    print("1. Think: Understand the question")
    print("2. Act: Choose and execute a function")
    print("3. Pause: Wait for function result")
    print("4. Respond: Provide final answer based on results")
    print("\nTo run the real AI agent with OpenAI:")
    print("1. Create a .env file with your OPENAI_API_KEY")
    print("2. Run: python main.py")

if __name__ == "__main__":
    main()
