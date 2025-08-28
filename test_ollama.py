#!/usr/bin/env python3
"""
Simple test for Ollama integration
"""

from ollama import Client
import time

def test_ollama_basic():
    """Test basic Ollama functionality."""
    print("🧪 Testing Ollama Integration...")
    
    try:
        client = Client(host='http://localhost:11434')
        
        # Test simple generation
        print("Generating simple response...")
        start_time = time.time()
        
        response = client.generate(
            model='llama3.1:8b',
            prompt='Hello! Please respond with just "Hello from Ollama!"',
            options={'temperature': 0.1, 'num_predict': 50}
        )
        
        end_time = time.time()
        print(f"✅ Response received in {end_time - start_time:.2f} seconds!")
        print(f"Response: {response.response}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_ollama_basic()
