# YouTube Transcript API

A Python service that fetches and formats YouTube video transcripts.

---

## Deploying to Vercel (Recommended for Public Use)

This project can be deployed as a serverless API on [Vercel](https://vercel.com/) for public access.

### Steps

1. Push your code to a GitHub/GitLab repository.
2. [Sign up for Vercel](https://vercel.com/signup) and connect your repository.
3. Vercel will auto-detect the `/api/transcript.py` serverless function.
4. Ensure your `requirements.txt` and `vercel.json` are present (see repo).
5. Deploy! Your API will be available at:

```
POST https://your-vercel-project.vercel.app/api/transcript
```

**Request body:**

```json
{
  "url": "YouTube video URL"
}
```

**Response:**

```json
{
  "transcript": "[0.00] ...transcript text..."
}
```

---

## Features

- Extract transcripts from YouTube videos
- Format transcripts with timestamps
- REST API endpoint for easy integration
- Error handling and logging

## Requirements

- Python 3.7+ (local) or Python 3.9 (Vercel, see vercel.json)
- youtube_transcript_api

_For local FastAPI server only:_

- fastapi
- uvicorn

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the API Server Locally (FastAPI, for development only)

Start the API server:

```bash
python transcript_api.py
```

The API will be available at: http://localhost:8000

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

_For local FastAPI server only:_

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
