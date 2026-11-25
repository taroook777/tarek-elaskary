#!/usr/bin/env python3
"""Free video generation with LTX-2.5 (video + audio) on the official Hugging Face Space.

Uses your free daily ZeroGPU quota. In the Claude cloud session the proxy injects the
Hugging Face token; elsewhere set HF_TOKEN.

Usage:
  python3 free_video.py "prompt" [--image https://...jpg] [--seconds 5] [--vertical] [--out out/x.mp4]
"""
import argparse, os, shutil
from gradio_client import Client, handle_file

p = argparse.ArgumentParser()
p.add_argument("prompt")
p.add_argument("--image", help="public image URL or local path (image-to-video)")
p.add_argument("--seconds", type=float, default=5)
p.add_argument("--vertical", action="store_true", help="9:16 instead of 16:9")
p.add_argument("--no-enhance", action="store_true")
p.add_argument("--out", default="out/video.mp4")
a = p.parse_args()

w, h = (704, 1216) if a.vertical else (1216, 704)
token = os.environ.get("HF_TOKEN", "proxy-injected")
c = Client("https://lightricks-ltx-2-5.hf.space",
           headers={"Authorization": f"Bearer {token}"}, verbose=False)
video, enhanced = c.predict(
    image_path=handle_file(a.image) if a.image else None,
    prompt=a.prompt, duration_s=a.seconds, width=w, height=h,
    do_enhance=not a.no_enhance, api_name="/run")[:2]
os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
shutil.copy(video, a.out)
print("saved:", a.out)
print("enhanced prompt:", enhanced)
