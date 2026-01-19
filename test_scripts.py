#!/usr/bin/env python3
"""
Test script to verify youtube_transcript.py and transcript_api.py work correctly.
"""

import subprocess
import sys

def test_youtube_transcript():
    """Test the youtube_transcript.py script with a sample URL"""
    print("\n" + "=" * 60)
    print("TEST 1: Testing youtube_transcript.py")
    print("=" * 60)
    
    # Using a popular YouTube video (Rick Astley - Never Gonna Give You Up)
    test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    
    print(f"\nTest URL: {test_url}")
    print("Running: echo 'URL' | python youtube_transcript.py\n")
    
    try:
        result = subprocess.run(
            ["python", "youtube_transcript.py"],
            input=test_url,
            text=True,
            capture_output=True,
            timeout=30
        )
        
        print("STDOUT:")
        print(result.stdout)
        
        if result.stderr:
            print("\nSTDERR:")
            print(result.stderr)
        
        if result.returncode == 0:
            print("\n✓ Test PASSED: Script executed successfully")
        else:
            print(f"\n✗ Test FAILED: Exit code {result.returncode}")
        
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print("\n✗ Test FAILED: Script timed out after 30 seconds")
        return False
    except Exception as e:
        print(f"\n✗ Test FAILED: {str(e)}")
        return False

def test_dependencies():
    """Check if all required dependencies are installed"""
    print("\n" + "=" * 60)
    print("TEST 0: Checking Dependencies")
    print("=" * 60)
    
    required_packages = [
        "youtube_transcript_api",
        "fastapi",
        "uvicorn"
    ]
    
    all_installed = True
    
    for package in required_packages:
        try:
            __import__(package.replace("-", "_"))
            print(f"✓ {package} is installed")
        except ImportError:
            print(f"✗ {package} is NOT installed")
            all_installed = False
    
    if all_installed:
        print("\n✓ All dependencies are installed")
    else:
        print("\n✗ Some dependencies are missing. Run: pip install -r requirements.txt")
    
    return all_installed

def main():
    print("\n" + "=" * 60)
    print("YouTube Transcript API - Test Suite")
    print("=" * 60)
    
    # Test dependencies first
    deps_ok = test_dependencies()
    
    if not deps_ok:
        print("\nPlease install dependencies first:")
        print("pip install -r requirements.txt")
        sys.exit(1)
    
    # Test youtube_transcript.py
    script_ok = test_youtube_transcript()
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Dependencies: {'✓ PASS' if deps_ok else '✗ FAIL'}")
    print(f"youtube_transcript.py: {'✓ PASS' if script_ok else '✗ FAIL'}")
    
    if deps_ok and script_ok:
        print("\n✓ All tests passed!")
        print("\nTo run the API server, execute:")
        print("python transcript_api.py")
        print("\nThen test it with:")
        print('curl -X POST "http://localhost:8000/transcript" -H "Content-Type: application/json" -d \'{"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}\'')
    else:
        print("\n✗ Some tests failed. Please check the output above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
