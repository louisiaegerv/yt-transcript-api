from youtube_transcript_api import YouTubeTranscriptApi
import re

def get_video_id(url):
    # Extract video ID from YouTube URL
    pattern = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

def get_transcript(video_id):
    try:
        # Get English transcript by default
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

def format_transcript(transcript):
    # Format the transcript into readable text
    formatted = []
    for entry in transcript:
        formatted.append(f"[{entry['start']:.2f}] {entry['text']}")
    return "\n".join(formatted)

import sys

def main():
    # Read URL from stdin
    url = sys.stdin.read().strip()
    
    if not url:
        print("No URL provided")
        return
    
    video_id = get_video_id(url)
    
    if not video_id:
        print("Invalid YouTube URL")
        return
    
    transcript = get_transcript(video_id)
    if transcript:
        print(format_transcript(transcript))

if __name__ == "__main__":
    main()
