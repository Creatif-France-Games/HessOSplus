import os
import urllib.request

def run(args):
    if not args:
        print("Usage: download <url>")
        return

    url = args[0]
    downloads_dir = os.path.join(os.getcwd(), "downloads")

    # download folder creation if needed
    if not os.path.exists(downloads_dir):
        os.makedirs(downloads_dir)

    try:
        filename = os.path.basename(url)
        destination = os.path.join(downloads_dir, filename)

        print(f"Downloading {url}...")
        urllib.request.urlretrieve(url, destination)
        print(f"Saved to {destination}")

    except Exception as e:
        print(f"Download failed: {e}")
