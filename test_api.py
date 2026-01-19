#!/usr/bin/env python3
"""
Simple test script to verify the API server is working.
"""

import requests
import json
import sys

def test_api_server():
    """Test the transcript API server"""
    print("=" * 60)
    print("Testing API Server")
    print("=" * 60)
    
    url = "http://localhost:8000/transcript"
    test_video_url = "https://www.youtube.com/watch?v=GS67Z0nj15Y"
    
    print(f"\nAPI URL: {url}")
    print(f"Test video: {test_video_url}")
    print("\nNote: Make sure the API server is running!")
    print("Start it with: python transcript_api.py")
    print("\nPress Ctrl+C to cancel if server is not running...")
    
    try:
        print("\nSending POST request...")
        response = requests.post(
            url,
            json={"url": test_video_url},
            timeout=30
        )
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            print("\n✓ SUCCESS: API responded successfully!")
            data = response.json()
            print(f"\nTranscript length: {len(data.get('transcript', ''))} characters")
            
            # Show first few lines of transcript
            transcript = data.get('transcript', '')
            lines = transcript.split('\n')[:5]
            print("\nFirst few lines of transcript:")
            for line in lines:
                print(f"  {line}")
            
            return True
        else:
            print(f"\n✗ ERROR: API returned status {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("\n✗ ERROR: Could not connect to API server")
        print("Make sure the server is running with: python transcript_api.py")
        return False
    except Exception as e:
        print(f"\n✗ ERROR: {str(e)}")
        return False

if __name__ == "__main__":
    success = test_api_server()
    sys.exit(0 if success else 1)
