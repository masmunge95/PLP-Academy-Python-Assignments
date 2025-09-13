import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
import hashlib

# Define constants at the module level for better readability and maintenance
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
DEFAULT_FOLDER = "Fetched_Images"

def extract_and_save_images(url, folder=DEFAULT_FOLDER):
    """
    Extracts images from a webpage and saves them to a folder.
    Creates a name from the image URL or generates a unique one if needed.
    """
    try:
        # Use a Session object to persist headers and improve performance
        with requests.Session() as session:
            session.headers.update({'User-Agent': USER_AGENT})

            # Create the directory to save images if it doesn't exist
            os.makedirs(folder, exist_ok=True)

            # Fetch the webpage content
            response = session.get(url, timeout=10)
            response.raise_for_status()  # Raise an HTTPError for bad responses

            # Parse the HTML content
            soup = BeautifulSoup(response.text, 'html.parser')

            for img_tag in soup.find_all('img'):
                # Get the image URL from 'src' or 'data-src' attributes
                img_url = img_tag.get('src') or img_tag.get('data-src')

                if not img_url:
                    continue

                # Handle relative URLs by converting them to absolute URLs
                absolute_img_url = urljoin(url, img_url)

                # Skip "data:image/..." URIs, which are embedded directly in the HTML
                if absolute_img_url.startswith('data:'):
                    print(f"  -> Skipping embedded image (data URI)")
                    continue

                # Determine the image name
                image_name = get_image_name(img_tag, absolute_img_url)

                # Final check to ensure a valid filename was generated
                if not image_name:
                    print(f"  -> Skipping image (could not generate a valid filename for URL: {absolute_img_url})")
                    continue

                # Download the image using the same session
                download_image(session, absolute_img_url, os.path.join(folder, image_name))

    except requests.exceptions.HTTPError as e:
        print(f"\n[ERROR] HTTP Error for {url}: {e.response.status_code} {e.response.reason}. Please check the URL.")
    except requests.exceptions.ConnectionError:
        print(f"\n[ERROR] Connection Error: Could not connect to {url}. Check your network or the URL.")
    except requests.exceptions.Timeout:
        print(f"\n[ERROR] Timeout Error: The request to {url} timed out.")
    except requests.RequestException as e:
        print(f"\n[ERROR] An unexpected error occurred while fetching {url}: {e}")

def get_image_name(img_tag, url):
    """
    Tries to get a meaningful image name from HTML attributes.
    If none is found, generates a unique name.
    """
    # 1. Look for 'alt' or 'title' attributes
    name = img_tag.get('alt') or img_tag.get('title')
    if name:
        # Sanitize the name to be file-system friendly
        name = "".join(c for c in name if c.isalnum() or c in (' ', '.', '_')).rstrip()
        # Ensure the name is not just spaces or empty
        if name and name.strip():
            # Get the file extension from the URL
            ext = os.path.splitext(urlparse(url).path)[1]
            return f"{name}{ext}"

    # 2. Get the name from the URL itself
    # Use urlparse and os.path.basename for a more reliable way to get the filename
    name_from_url = os.path.basename(urlparse(url).path)
    if name_from_url:
        # Sanitize the name to ensure it's a valid filename
        sanitized_name = "".join(c for c in name_from_url if c.isalnum() or c in ('.', '_', '-')).rstrip()
        if sanitized_name:
            return sanitized_name

    # 3. If all else fails, create a unique name using a hash
    unique_hash = hashlib.sha1(url.encode('utf-8')).hexdigest()[:10]
    return f"{unique_hash}.jpg" # Default to .jpg if extension cannot be determined

def download_image(session, url, filename):
    """Downloads an image from a URL and saves it to a file."""
    try:
        response = session.get(url, stream=True, timeout=10)
        response.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"  -> Downloaded: {os.path.basename(filename)}")
    except requests.exceptions.HTTPError as e:
        print(f"  -> Failed to download {os.path.basename(filename)} (HTTP {e.response.status_code})")
    except requests.RequestException as e:
        print(f"  -> Failed to download {os.path.basename(filename)}: {e}")
    except IOError as e:
        print(f"  -> ERROR saving file {os.path.basename(filename)}: {e}")

def main():
    """Main function to run the image fetcher script."""
    print("--- Welcome to the Image Fetcher ---")
    print("Enter a URL to scrape, or type 'exit' or 'quit' to close the program.")

    while True:
        url = input("\nPlease enter a URL (or 'exit'): ").strip()

        if not url or url.lower() in ['exit', 'quit']:
            print("Exiting program. Goodbye!")
            break

        # A simple check to ensure the URL has a scheme
        if not url.startswith(('http://', 'https://')):
            print(f"URL scheme missing. Prepending 'http://' to '{url}'")
            url = 'http://' + url

        print(f"\nFetching images from: {url}")
        extract_and_save_images(url)
        print("\n--- Task complete. Ready for the next URL. ---")

if __name__ == "__main__":
    main()
