# Python Image Fetcher

A command-line tool to easily scrape and download all images from a given webpage.

## Description

This project provides a robust Python script that fetches a webpage, parses its HTML to find all image tags, and downloads the linked images to a local folder. It's designed to be user-friendly and resilient, handling common web scraping challenges like relative URLs, embedded images, and network errors.

## Features

-   **Interactive CLI**: Runs in a loop, allowing you to scrape multiple URLs in one session.
-   **Comprehensive Scraping**: Finds images in `src` and `data-src` attributes.
-   **Smart URL Handling**: Automatically converts relative image URLs (e.g., `/images/pic.jpg`) to absolute ones.
-   **Efficient Downloading**: Uses `requests.Session` for connection pooling, making multiple downloads from the same site faster.
-   **Intelligent Naming**: Creates meaningful filenames from image `alt` or `title` tags. Falls back to the original filename or a unique hash if no metadata is available.
-   **Robust Error Handling**: Gracefully handles network errors, bad URLs, and file system issues without crashing.
-   **Skips Embedded Images**: Ignores non-downloadable `data:` URIs to prevent errors.
-   **Filename Sanitization**: Cleans filenames to remove characters that are invalid in most operating systems.

## Prerequisites

-   Python 3.6+
-   `pip` (Python package installer)

## Installation

1.  **Clone the repository or download the files.**

2.  **Install the required packages:**
    A `requirements.txt` file is included for easy installation. From the project directory, run:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the main script from your terminal:

```sh
python Image-fetcher.py
```

The script will then prompt you to enter a URL.

### Example Session

```
--- Welcome to the Image Fetcher ---
Enter a URL to scrape, or type 'exit' or 'quit' to close the program.

Please enter a URL (or 'exit'): example.com
URL scheme missing. Prepending 'http://' to 'example.com'

Fetching images from: http://example.com
  -> Downloaded: iana-logo-pageheader.png

--- Task complete. Ready for the next URL. ---

Please enter a URL (or 'exit'): exit
Exiting program. Goodbye!
```

Downloaded images will be saved in a folder named `Fetched_Images` by default.

## File Descriptions

-   `Image-fetcher.py`: The main, feature-rich script for scraping all images from a webpage. **This is the recommended script to use.**
-   `requirements.txt`: A list of the Python packages required to run the script.
