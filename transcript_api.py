from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import os
import logging
from pydantic import BaseModel
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TranscriptRequest(BaseModel):
    url: str

@app.post("/transcript")
async def get_transcript(request: TranscriptRequest):
    try:
        logger.info(f"Received transcript request for URL: {request.url}")
        
        # Call the script using subprocess
        result = subprocess.run(
            ["python", "youtube_transcript.py"],
            input=request.url,
            text=True,
            capture_output=True
        )
        
        if result.returncode != 0:
            error_msg = f"Error fetching transcript: {result.stderr}"
            logger.error(error_msg)
            raise HTTPException(
                status_code=400,
                detail=error_msg
            )
            
        logger.info(f"Successfully fetched transcript for URL: {request.url}")
        
        # Log a preview of the transcript (first 200 chars)
        transcript_preview = result.stdout[:200].replace('\n', ' ')
        if len(result.stdout) > 200:
            transcript_preview += "..."
        logger.info(f"Transcript preview: {transcript_preview}")
        
        return {"transcript": result.stdout}

        # Get the current timestamp
        # current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # logger.info("DEMO MODE: Using demo content at: " + f"[{current_time}]")
        # return {"transcript": "[0.16] " + f"[{current_time}]" + " hey everyone welcome back today I want\n[3.20] to talk about an exciting collaboration\n[5.12] that's creating a buzz perplexity AI\n[7.64] teaming up with Tik Tok if you've ever\n[9.88] wished for a smarter more interactive\n[12.00] way to discover content or learn while\n[14.24] scrolling through your Tik Tok feed this\n[16.36] is something you want to hear about\n[18.16] perplexity AI for those of you who don't\n[20.68] know is like having a superpowered\n[22.88] assistant for finding answers it's\n[25.04] designed to help you search learn and\n[27.52] explore with precision and context\n[30.12] instead of just throwing a bunch of\n[31.56] links at you it gives detailed\n[33.84] well-rounded responses that make digging\n[35.84] into topics so much easier now they've\n[38.88] partnered with Tik Tok one of the\n[40.64] world's most popular platforms for short\n[43.00] form video content it's a match that\n[45.24] brings together the best of AI and\n[47.36] social media here's the cool part Tik\n[50.24] Tok is already great at helping you\n[52.20] discover new trends ideas and creators\n[55.48] but let's be honest sometimes you see a\n[57.68] video and you're left with so many\n[59.52] questions like what's the history behind\n[62.16] this dance or how does this recipe\n[64.64] actually work that's where perplexity AI\n[67.36] steps in this collaboration is about\n[69.76] enhancing how we interact with Tik Tok\n[72.20] giving you instant detailed answers\n[74.36] related to what you're watching for\n[76.28] example imagine watching a Tik Tok about\n[78.84] an unusual science experiment with\n[81.28] perplexity AI you could instantly dive\n[84.20] deeper into the science behind it\n[85.92] without leaving the app or maybe you're\n[88.04] inspired by a travel Vlog and want more\n[90.20] info about the destination perplexity\n[92.40] can give you quick insights like mustsee\n[94.56] spots or the best time to visit it's\n[97.04] like having a research buddy built right\n[99.12] into your Tik Tok experience what's also\n[101.88] exciting is how this collaboration feels\n[104.08] so natural Tik Tok has always been about\n[106.80] quick bite-sized content and perplexity\n[109.68] AI fits right into that flow it doesn't\n[112.20] disrupt your scrolling or take you out\n[114.28] of the moment instead it's there to\n[116.84] enrich your experience whether that's\n[118.92] through better answers deeper context or\n[121.60] just helping you learn something new\n[123.20] while staying entertained this\n[125.12] partnership also highlights a bigger\n[127.00] Trend AI becoming part of our everyday\n[129.76] interactions not as something separate\n[131.88] or intimidating but as a tool that\n[134.08] enhances how we connect with the world\n[136.32] perplexity Ai and Tik Tok are Bridging\n[138.84] the Gap between curiosity and instant\n[141.16] knowledge making learning fun and\n[143.44] accessible let me know in the comments\n[145.48] what you think about this or how you'd\n[147.24] use it don't forget to like subscribe\n[150.32] and stay tuned for more exciting updates\n[152.92] thanks for watching and I'll see you\n[154.76] next time\n"}
        
    except HTTPException as he:
        logger.error(f"HTTP Error {he.status_code}: {he.detail}")
        raise he
    except Exception as e:
        error_msg = f"Internal server error: {str(e)}"
        logger.error(error_msg)
        raise HTTPException(
            status_code=500,
            detail=error_msg
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
