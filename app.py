import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from openai import OpenAI
import requests
from bs4 import BeautifulSoup

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

# স্ট্যাটিক ফাইল এবং টেমপ্লেট সেটআপ
app.mount("/static", StaticFiles(directory="."), name="static")
templates = Jinja2Templates(directory=".")

KNOWLEDGE_BASE = ""

def scrape_data():
    global KNOWLEDGE_BASE
    urls = ["https://betopiagroup.com/", "https://betopialimited.com/", "https://fireai.agency/"]
    master_text = ""
    for url in urls:
        try:
            res = requests.get(url, timeout=10)
            soup = BeautifulSoup(res.text, 'html.parser')
            for tag in soup(['script', 'style', 'nav', 'footer', 'header']):
                tag.decompose()
            clean_text = " ".join(soup.get_text().split())
            master_text += f"\nSource {url}: {clean_text}\n"
        except:
            continue
    KNOWLEDGE_BASE = master_text[:15000]

@app.on_event("startup")
async def startup_event():
    scrape_data()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(text: str = Form(...)):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": f"You are a helpful voice assistant for Betopia and FireAI. Data: {KNOWLEDGE_BASE}. Keep answers very short."},
                {"role": "user", "content": text}
            ]
        )
        reply = response.choices[0].message.content
        return JSONResponse({"reply": reply})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)