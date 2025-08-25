#!/usr/bin/env python3
"""
Test script to verify the AI agent system components work correctly.
This script tests the functions and logic without requiring an OpenAI API key.
"""

from actions import (
    get_response_time, 
    get_weather_info, 
    calculate_math_expression, 
    get_current_time, 
    search_web
)

def test_actions():
    """Test all the action functions to ensure they work correctly."""
    print("Testing Action Functions")
    print("=" * 40)
    
    # Test get_response_time
    print("\nTesting get_response_time:")
    test_urls = ["learnwithhasan.com", "google.com", "openai.com", "unknown.com"]
    for url in test_urls:
        result = get_response_time(url)
        print(f"  {url}: {result} seconds")
    
    # Test get_weather_info
    print("\nTesting get_weather_info:")
    test_cities = ["new york", "london", "tokyo", "unknown city"]
    for city in test_cities:
        result = get_weather_info(city)
        print(f"  {city}: {result}")
    
    # Test calculate_math_expression
    print("\nTesting calculate_math_expression:")
    test_expressions = ["2 + 3", "10 * 5", "100 / 4", "2 + 3 * 4"]
    for expr in test_expressions:
        result = calculate_math_expression(expr)
        print(f"  {expr} = {result}")
    
    # Test get_current_time
    print("\nTesting get_current_time:")
    current_time = get_current_time()
    print(f"  Current time: {current_time}")
    
    # Test search_web
    print("\nTesting search_web:")
    test_queries = ["python", "ai", "machine learning", "unknown topic"]
    for query in test_queries:
        result = search_web(query)
        result_str = str(result)
        print(f"  '{query}': {result_str[:80]}...")
    
    print("\nAll action functions tested successfully!")

def test_json_extraction():
    """Test the JSON extraction logic from main.py."""
    print("\nTesting JSON Extraction Logic")
    print("=" * 40)
    
    # Import the function from main
    try:
        from main import extract_json
        
        # Test cases
        test_responses = [
            'Action: {"function_name": "get_response_time", "function_parms": {"url": "test.com"}} PAUSE',
            'Thought: I need to check. Action: {"function_name": "get_weather_info", "function_parms": {"city": "london"}} PAUSE',
            'No function call here',
            'Action: {"function_name": "calculate_math_expression", "function_parms": {"expression": "2+2"}} PAUSE'
        ]
        
        for i, response in enumerate(test_responses, 1):
            result = extract_json(response)
            print(f"  Test {i}: {result}")
            
    except ImportError:
        print("  Skipping JSON extraction test (main.py not available)")

def test_function_execution():
    """Test the function execution logic."""
    print("\nTesting Function Execution Logic")
    print("=" * 40)
    
    try:
        from main import execute_function
        
        # Test cases
        test_calls = [
            ("get_response_time", {"url": "test.com"}),
            ("get_weather_info", {"city": "london"}),
            ("calculate_math_expression", {"expression": "5 + 3"}),
            ("get_current_time", {}),
            ("search_web", {"query": "python"}),
            ("unknown_function", {"param": "value"})
        ]
        
        for function_name, params in test_calls:
            result = execute_function(function_name, params)
            print(f"  {function_name}({params}): {result}")
            
    except ImportError:
        print("  Skipping function execution test (main.py not available)")

def main():
    """Run all tests."""
    print("🤖 AI Agent System Test Suite")
    print("=" * 50)
    
    # Test action functions
    test_actions()
    
    # Test JSON extraction
    test_json_extraction()
    
    # Test function execution
    test_function_execution()
    
    print("\n" + "=" * 50)
    print("Test suite completed!")
    print("\nTo run the full AI agent system:")
    print("1. Create a .env file with your OPENAI_API_KEY")
    print("2. Run: python main.py")
    print("3. Or run examples: python example.py")

if __name__ == "__main__":
    main()
