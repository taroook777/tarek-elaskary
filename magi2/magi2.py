#!/usr/bin/env python3
"""Generate videos with Sand.ai MAGI-2 (https://platform.sand.ai/docs).

Usage:
  python3 magi2.py "prompt" [--image ref.png] [--duration 10] [--ratio 16:9] [--out out.mp4]

The key is read from SAND_API_KEY. In the Claude cloud session the proxy injects
the real key, so any placeholder value works there.
"""
import argparse, json, os, sys, time, urllib.request

API = "https://api.sand.ai"
KEY = os.environ.get("SAND_API_KEY", "proxy-injected")


def call(method, path, body=None, headers=None):
    req = urllib.request.Request(API + path, data=body, method=method,
                                 headers={"Authorization": f"Bearer {KEY}", **(headers or {})})
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"HTTP {e.code}: {e.read().decode()}")


def upload(path):
    boundary = "magi2boundary"
    data = open(path, "rb").read()
    body = (f"--{boundary}\r\nContent-Disposition: form-data; name=\"file\"; "
            f"filename=\"{os.path.basename(path)}\"\r\nContent-Type: application/octet-stream\r\n\r\n").encode() \
        + data + f"\r\n--{boundary}--\r\n".encode()
    res = call("POST", "/v1/assets", body, {"Content-Type": f"multipart/form-data; boundary={boundary}"})
    return str(res["id"])


def main():
    p = argparse.ArgumentParser()
    p.add_argument("prompt")
    p.add_argument("--image")
    p.add_argument("--duration", type=int, default=10)
    p.add_argument("--ratio", default="16:9")
    p.add_argument("--no-audio", action="store_true")
    p.add_argument("--out", default="magi2_output.mp4")
    a = p.parse_args()

    parts = [{"type": "text", "text": a.prompt}]
    if a.image:
        parts.append({"type": "reference_image", "image": {"assetId": upload(a.image)}})
    req = {"model": "magi-2", "parts": parts, "duration": a.duration,
           "aspectRatio": a.ratio, "generateAudio": not a.no_audio}
    gen = call("POST", "/v2/generations", json.dumps(req).encode(), {"Content-Type": "application/json"})
    print("generation id:", gen["id"])

    while True:
        g = call("GET", f"/v2/generations/{gen['id']}")
        print("status:", g["status"])
        if g["status"] == "succeeded":
            urllib.request.urlretrieve(g["output"]["videoUrl"], a.out)
            print("saved:", a.out)
            return
        if g["status"] in ("failed", "canceled"):
            sys.exit(f"failed: {g.get('error')}")
        time.sleep(10)


if __name__ == "__main__":
    main()
