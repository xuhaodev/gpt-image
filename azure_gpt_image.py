import os
import base64
import requests
from typing import Optional
from dotenv import load_dotenv

load_dotenv()  # reads .env into os.environ

AZURE_API_KEY = os.getenv("AZURE_API_KEY")
BASE_URL = os.getenv("BASE_URL")

HEADERS = {
    "Content-Type": "application/json",
    "api-key": AZURE_API_KEY
}

def generate_image(prompt: str,
                   size: str = "1024x1024",
                   quality: str = "medium",
                   n: int = 1,
                   out_path: str = "generated_image.png") -> str:
    """
    Generate a new image from a text prompt.
    Returns the local path to the saved PNG.
    """
    url = f"{BASE_URL}/generations?api-version=2025-04-01-preview"
    payload = {
        "prompt": prompt,
        "size": size,
        "quality": quality,
        "n": n
    }
    resp = requests.post(url, headers=HEADERS, json=payload)
    resp.raise_for_status()
    b64 = resp.json()["data"][0]["b64_json"]
    img = base64.b64decode(b64)
    with open(out_path, "wb") as f:
        f.write(img)
    return out_path

def edit_image(image_path: str,
               prompt: str,
               mask_path: Optional[str] = None,
               out_path: str = "edited_image.png") -> str:
    """
    Edit an existing image with an optional mask.
    If mask_path is None, the mask field is omitted.
    Returns the local path to the saved PNG.
    """
    url = f"{BASE_URL}/edits?api-version=2025-04-01-preview"
    files = {
        "image": open(image_path, "rb"),
        "prompt": (None, prompt)
    }
    if mask_path:
        files["mask"] = open(mask_path, "rb")

    hdr = {"api-key": AZURE_API_KEY}
    resp = requests.post(url, headers=hdr, files=files)
    resp.raise_for_status()

    b64 = resp.json()["data"][0]["b64_json"]
    img = base64.b64decode(b64)
    with open(out_path, "wb") as f:
        f.write(img)
    return out_path