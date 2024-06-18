# YouTube Scraper and Downloader

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
