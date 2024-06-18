# YouTube Scraper and Downloader
### By Ayoub Abraich
This Python script scrapes video URLs from a YouTube channel and downloads them using yt-dlp, prioritizing the smallest available video and audio formats.

## Features

- **Web Scraping:** Uses Playwright to dynamically load the YouTube page and extract video URLs.
- **Efficient Downloading:** Leverages yt-dlp to download videos, with a custom format selector to choose the smallest combined video and audio streams.
- **Progress Bars:** Provides progress bars during both scraping and downloading for better user experience.
- **Cookie Handling:** Includes functionality to save and load cookies, potentially enabling login-based scraping in the future (not implemented in this version).

## Requirements

- Python 3.7+
- Install the required libraries:
  ```bash
  pip install playwright yt-dlp tqdm
  ```

## How to Use

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Zetrohab/youtube-scraper-downloader.git
   cd youtube-scraper-downloader
   ```

2. **Update Channel URL (Optional):**
   - Open `youtube_scraper_downloader.py` and change the `URL` variable to the target YouTube channel's videos page URL.

3. **Run the script:**
   ```bash
   python youtube_scraper_downloader.py
   ```

   - The script will:
     - Open a headless browser (you won't see it).
     - Navigate to the YouTube channel's videos page.
     - Scroll down to load more videos.
     - Extract video URLs.
     - Download the first 5 videos (you can change the number in the code).

## Notes

- This script is for educational purposes only. Respect YouTube's terms of service and copyright laws. 
- You can adjust the number of videos to download by modifying the slicing in the `for` loop in the main execution block (e.g., `video_urls[:10]` to download the first 10 videos).

## Disclaimer

This project is provided "as is" without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.
