import json
from youtube_transcript import get_video_id, get_transcript, format_transcript

def handler(request):
    try:
        # Vercel passes the request as a dict with a "body" key (JSON string)
        body = request.get("body")
        if not body:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "No request body"})
            }
        data = json.loads(body)
        url = data.get("url")
        if not url:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "No URL provided"})
            }
        video_id = get_video_id(url)
        if not video_id:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Invalid YouTube URL"})
            }
        transcript = get_transcript(video_id)
        if not transcript:
            return {
                "statusCode": 500,
                "body": json.dumps({"error": "Could not fetch transcript"})
            }
        formatted = format_transcript(transcript)
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"transcript": formatted})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
