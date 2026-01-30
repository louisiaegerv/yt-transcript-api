from youtube_transcript_api import YouTubeTranscriptApi
import re
import json
import sys

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
        # Handle both dict and object types
        if isinstance(entry, dict):
            text = entry['text'].replace('\n', ' ')
            start = entry['start']
        else:
            text = entry.text.replace('\n', ' ')
            start = entry.start
        formatted.append(f"[{start:.2f}] {text}")
    return "\n".join(formatted)

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
    
    # DEBUG: Log the URL and video ID
    print(f"=== DEBUG INFO ===", file=sys.stderr)
    print(f"URL: {url}", file=sys.stderr)
    print(f"Video ID: {video_id}", file=sys.stderr)
    print(f"==================", file=sys.stderr)
    
    transcript = get_transcript(video_id)
    if transcript:
        # DEBUG: Log raw transcript structure
        print(f"\n=== RAW TRANSCRIPT DATA ===", file=sys.stderr)
        print(f"Number of entries: {len(transcript)}", file=sys.stderr)
        print(f"\nFirst 5 entries (raw):", file=sys.stderr)
        for i, entry in enumerate(transcript[:5]):
            print(f"Entry {i}:", file=sys.stderr)
            print(f"  Keys: {list(entry.keys())}", file=sys.stderr)
            print(f"  Data: {json.dumps(entry, indent=2)}", file=sys.stderr)
        
        # Check for entries with missing or unusual keys
        print(f"\n=== CHECKING FOR UNUSUAL ENTRIES ===", file=sys.stderr)
        for i, entry in enumerate(transcript):
            if 'start' not in entry or 'text' not in entry:
                print(f"WARNING: Entry {i} missing required keys:", file=sys.stderr)
                print(f"  {json.dumps(entry, indent=2)}", file=sys.stderr)
            if '\n' in entry.get('text', ''):
                print(f"WARNING: Entry {i} contains newline in text:", file=sys.stderr)
                print(f"  Text: {repr(entry['text'])}", file=sys.stderr)
        
        print(f"\n=== FORMATTED OUTPUT ===", file=sys.stderr)
        formatted = format_transcript(transcript)
        # Log first 10 lines of formatted output
        lines = formatted.split('\n')
        print(f"Total lines in formatted output: {len(lines)}", file=sys.stderr)
        print(f"\nFirst 10 lines of formatted output:", file=sys.stderr)
        for i, line in enumerate(lines[:10]):
            print(f"Line {i}: {repr(line)}", file=sys.stderr)
        
        # Check for lines that don't match expected format
        print(f"\n=== VALIDATING FORMATTED OUTPUT ===", file=sys.stderr)
        pattern = r'^\[(\d+\.\d+)\]\s+(.*?)\s*$'
        invalid_lines = []
        for i, line in enumerate(lines):
            if not re.match(pattern, line):
                invalid_lines.append((i, line))
        
        if invalid_lines:
            print(f"FOUND {len(invalid_lines)} INVALID LINES:", file=sys.stderr)
            for i, line in invalid_lines[:10]:  # Show first 10 invalid lines
                print(f"  Line {i}: {repr(line)}", file=sys.stderr)
        else:
            print("All lines match expected format!", file=sys.stderr)
        
        print(f"=============================\n", file=sys.stderr)
        
        # Output the formatted transcript to stdout
        print(formatted)

if __name__ == "__main__":
    main()
