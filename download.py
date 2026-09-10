#!/usr/bin/env python3
"""
YouTube CLI Downloader
Downloads audio from YouTube in maximum quality.
"""

# Standard library imports
import os
import sys
import traceback

# Third-party imports
import yt_dlp


def download(url: str, output_directory: str = "downloads") -> None:
    """
    Download audio from YouTube in maximum quality.

    Args:
        url (str): YouTube URL.
        output_directory (str): Directory to save downloads. Default: "downloads".
    """

    ydl_opts = {
        "format": "bestaudio[ext=m4a]/bestaudio/best",
        "outtmpl": f"{output_directory}/%(playlist_title)s/%(title)s.%(ext)s",
        "quiet": False,
        "nopostprocessors": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(url, download=True)
        print(f'Downloaded to "{os.path.abspath(output_directory)}"')
    except Exception:
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else input("Paste a YouTube URL: ")
    output_directory = sys.argv[2] if len(sys.argv) > 2 else "downloads"
    download(url, output_directory)
