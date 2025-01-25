# YouTube Transcript API

A FastAPI-based service that fetches and formats YouTube video transcripts.

## Features
- Extract transcripts from YouTube videos
- Format transcripts with timestamps
- REST API endpoint for easy integration
- Error handling and logging

## Requirements
- Python 3.7+
- youtube_transcript_api
- fastapi
- uvicorn

## Installation
1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the API Server
Start the API server:
```bash
python transcript_api.py
```

The API will be available at: http://localhost:8000

### API Endpoint
**POST /transcript**

Request body:
```json
{
    "url": "YouTube video URL"
}
```

Example request:
```bash
curl -X POST "http://localhost:8000/transcript" \
-H "Content-Type: application/json" \
-d '{"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'
```

Example response:
```json
{
    "transcript": "[0.00] Never gonna give you up\n[3.58] Never gonna let you down\n[7.16] Never gonna run around and desert you"
}
```

### Direct Script Usage
You can also use the script directly:
```bash
echo "https://www.youtube.com/watch?v=dQw4w9WgXcQ" | python youtube_transcript.py
```

## Error Handling
The API returns appropriate HTTP status codes:
- 400: Invalid YouTube URL or transcript unavailable
- 500: Internal server error

All errors are logged with timestamps for debugging.

## Development
To run in development mode with auto-reload:
```bash
uvicorn transcript_api:app --reload
```

## Dependencies
- [youtube_transcript_api](https://pypi.org/project/youtube-transcript-api/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
