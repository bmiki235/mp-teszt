#!/usr/bin/env python3
"""
X (Twitter) videó letöltő script.

Használat:
    python3 download_x_video.py <X_VIDEO_URL>

Példa:
    python3 download_x_video.py https://x.com/irishman787878/status/2043810517421060417

Követelmény:
    pip install yt-dlp
"""

import sys
import subprocess


def download_video(url):
    """
    Letölti a megadott X/Twitter videót a legjobb minőségben.

    @param {str} url - Az X/Twitter poszt URL-je
    @returns {None}
    @raises {SystemExit} - Ha a letöltés sikertelen
    """
    try:
        subprocess.run(
            [
                "yt-dlp",
                "-f", "best[ext=mp4]/best",
                "-o", "%(title)s.%(ext)s",
                "--no-playlist",
                url,
            ],
            check=True,
        )
        print("\nLetöltés sikeres!")
    except FileNotFoundError:
        print("Hiba: a yt-dlp nincs telepítve.")
        print("Telepítsd: pip install yt-dlp")
        sys.exit(1)
    except subprocess.CalledProcessError:
        print("Hiba: a letöltés sikertelen.")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Használat: python3 download_x_video.py <X_VIDEO_URL>")
        print("Példa:    python3 download_x_video.py https://x.com/user/status/123")
        sys.exit(1)

    download_video(sys.argv[1])
