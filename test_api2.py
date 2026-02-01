from youtube_transcript_api import YouTubeTranscriptApi
video_id = "FNJXjiDKO90"

ytt_api = YouTubeTranscriptApi()
fetched_transcript = ytt_api.fetch(video_id)

# is iterable
#for snippet in fetched_transcript:
 #   print(snippet.text)

# indexable
last_snippet = fetched_transcript[-1]
print(last_snippet)

# provides a length
snippet_count = len(fetched_transcript)
print(snippet_count)