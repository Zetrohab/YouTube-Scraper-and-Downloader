import asyncio
from playwright.async_api import async_playwright
import time
import json
from tqdm import tqdm
import yt_dlp

# --- Constants ---
COOKIES_FILE = 'cookies.json' 
URL = "https://www.youtube.com/@thinkerview/videos" 

# --- Web Scraping Functions ---

async def save_cookies(page):
    """Saves the current browser cookies to a JSON file."""
    cookies = await page.context.cookies()
    with open(COOKIES_FILE, 'w') as f:
        json.dump(cookies, f)

async def load_cookies(context):
    """Loads cookies from a JSON file into the browser context."""
    try:
        with open(COOKIES_FILE, 'r') as f:
            cookies = json.load(f)
            await context.add_cookies(cookies)
    except FileNotFoundError:
        print("Cookies file not found. Proceeding without loading cookies.")

async def scrape_youtube_videos():
    """Scrapes video URLs from a YouTube channel's videos page."""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True) 
        context = await browser.new_context()

        await load_cookies(context)
        
        page = await context.new_page()
        await page.goto(URL, timeout=60000)  
        time.sleep(5) 

        for _ in range(3):  
            await page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
        
        video_elements = await page.query_selector_all('#thumbnail')
        print(f'Found {len(video_elements)} videos')
        video_urls = []
        for v in tqdm(video_elements):
            try:
                video_urls.append('youtube.com' + await v.get_attribute('href'))
            except:
                pass
        
        await browser.close()
        return list(set(video_urls))  

# --- YouTube Download Functions ---

def format_selector(ctx):
    """Custom format selector for yt-dlp to choose the smallest video+audio."""
    formats = ctx.get('formats')[::-1] 

    sorted_formats = sorted(formats, key=lambda f: f.get('filesize') or float('inf'))

    best_video = next(f for f in sorted_formats if f['vcodec'] != 'none' and f['acodec'] == 'none')
    audio_ext = {'mp4': 'm4a', 'webm': 'webm'}[best_video['ext']]
    best_audio = next(f for f in sorted_formats if (
        f['acodec'] != 'none' and f['vcodec'] == 'none' and f['ext'] == audio_ext))

    yield {
        'format_id': f'{best_video["format_id"]}+{best_audio["format_id"]}',
        'ext': best_video['ext'],
        'requested_formats': [best_video, best_audio],
        'protocol': f'{best_video["protocol"]}+{best_audio["protocol"]}'
    }

def download(urls: str):
    """Downloads a video from a given URL using yt-dlp."""
    ydl_opts = {
        'format': format_selector, 
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([urls])

# --- Main Execution ---

if __name__ == '__main__':
    video_urls = asyncio.run(scrape_youtube_videos()) 
    print(f'Number of videos scraped: {len(video_urls)}')   
    
    for url in tqdm(video_urls[:5]):
        print(f'Downloading: {url}')
        download(url)
