# Open-Weights AI Video Generation Models and Running Them Free or Cheaply (as of late November 2026)

Method note: WebFetch could not reach any site (DNS blocked for marktechpost.com, vdf.ai, howaiworks.ai), so these notes rest on WebSearch result summaries and live Hugging Face Hub data from the HF MCP tool. Hub data (licenses, dates, downloads, Space tags, inference providers) is primary and reliable. Search summaries are mostly third-party blogs, and conflicts are flagged below.

## 1. Which open models are best (rankings, licenses, audio, resolution, duration)

### Takeaway
As of late November 2026 the open-weights front line is **LTX-2.5 (Lightricks, 22B, audio+video, up to 4K)** and **MiniMax H3 (33B, audio+video, 768p open)**. Behind them come **Kandinsky 6.0 Video (MIT, audio)**, **MAGI-2 Preview (114B MoE, Apache 2.0, audio)** and **HunyuanVideo 1.5 (8.3B)**. **Wan 2.2 (Apache 2.0)** is still the most permissive, lightest and best-supported option. Alibaba has released no open flagship weights after Wan 2.2: Wan 2.5, 2.6 and 3.0 are API-only, and Wan 2.7's status is disputed.

### Cited Findings
**Rankings (Artificial Analysis Video Arena)**
- LTX-2 became the leading open-weights model on Artificial Analysis, surpassing Wan 2.2 A14B in both text-to-video and image-to-video (January 2026) — [Artificial Analysis on X](https://x.com/ArtificialAnlys/status/2012256702788153604); [LTX on X](https://x.com/ltx_model/status/2008862459327865121)
- A MarkTechPost article dated Nov 13, 2026 reportedly ranks the AA-Video-T2V v2.1 (with audio) board with **LTX-2.5 Fast (943) and LTX-2.5 Pro (938) as the open-weights leaders**. It says Wan 2.2 and HunyuanVideo 1.5 are not ranked on the current AA boards. (Seen only as a search summary, not fetched.) — [MarkTechPost](https://www.marktechpost.com/2026/11/13/best-ai-video-generation-models-2026/)
- An older snapshot lists LTX-2 Pro as the top open-weights model at Elo 1197, LTX-2.3 Fast at 1169, and HunyuanVideo-1.5 at AA rank #40 with Elo 1120. Elo values from different board versions should not be compared directly. — [Magic Hour leaderboard](https://magichour.ai/model-leaderboard/image-to-video)
- MiniMax H3 is described as the strongest open-weight model with native sound, but its license is restricted. — [vdf.ai (search summary)](https://vdf.ai/blog/best-local-video-generation-models/); [fuser.studio](https://fuser.studio/articles/best-open-source-video-models)

**LTX-2.5 (Lightricks)**
- HF repo `Lightricks/LTX-2.5` was created 23 Jul 2026 and updated 11 Oct 2026. It is gated, license "other", has about 8.0M downloads and 13.4k likes, and is tagged text/image/audio-to-audio-video, ComfyUI, and 9 languages. It is the #1 trending text-to-video model on HF. — [HF: Lightricks/LTX-2.5](https://hf.co/Lightricks/LTX-2.5)
- 22B parameters, synchronized audio and video, output up to 4K (3840×2176). One source says "Fast up to 4K; Pro up to 1080p". — [explainx.ai](https://explainx.ai/blog/lightricks-ltx-2-5-open-weight-video-audio-model-multishot-22b-2026); [ltx.io model page](https://ltx.io/model/ltx-2-5); [airmore.ai](https://airmore.ai/ai-review/ltx-2-5-review)
- License: LTX-2.x Community License, free for companies under $10M annual revenue. One outlier source claims Apache 2.0, but the HF tag is "other" and the repo is gated. — [innfactory.ai](https://innfactory.ai/en/ai-models/lightricks-ltx/); [HF](https://hf.co/Lightricks/LTX-2.5)
- Official Diffusers repo: `Lightricks/LTX-2.5-Diffusers`. — [HF](https://hf.co/Lightricks/LTX-2.5-Diffusers)

**MiniMax H3**
- HF repo `MiniMaxAI/MiniMax-H3`: 33.1B parameters, license "other", about 20.3M downloads and 7.3k likes, updated 24 Nov 2026. It supports T2V, I2V, V2V and reference-to-audio-video with synchronized audio. Live HF Inference Providers are fal-ai and wavespeed. — [HF: MiniMaxAI/MiniMax-H3](https://hf.co/MiniMaxAI/MiniMax-H3)
- The weights were posted in early August 2026 (sources say Aug 2 or Aug 3; the HF repo was created 28 Jul). Open checkpoints are H3-Base at native 768p, and the 2K upscale stays API-only. Audio is 32 kHz stereo, generated in the same pass. — [MiniMax blog](https://www.minimax.io/blog/minimax-h3); [Runpod](https://www.runpod.io/blog/minimax-h3-the-open-weight-omni-modal-video-model-and-what-it-takes-to-run-it); [atoms.dev](https://atoms.dev/blog/minimax-h3-open-weights-multimodal-video-model)
- **License catch:** a custom license that reportedly excludes the US, EU, UK and South Korea, covering use, hosting and even use of outputs in those territories. Comfy is reportedly the only official reseller of commercial licenses. — [miraflow.ai](https://miraflow.ai/blog/minimax-h3-open-weight-omni-modal-architecture-explained-2026); [comfy.org/minimax-h3](https://comfy.org/minimax-h3/)
- Huge derivative ecosystem: `unsloth/MiniMax-H3-GGUF` (3.7M downloads), the few-step `VideoRebirthAI/hyperflow-h3-flash` (GGUF/INT8/ComfyUI), `larryvrh/MiniMax-H3-Turbo-Lora`, and a pruned `H3-Tiny/MiniMax-H3-Tiny-ComfyUI` (21 Nov 2026). — [HF search: text-to-video trending](https://hf.co/unsloth/MiniMax-H3-GGUF); [HF](https://hf.co/VideoRebirthAI/hyperflow-h3-flash); [HF](https://hf.co/H3-Tiny/MiniMax-H3-Tiny-ComfyUI)

**Alibaba Wan**
- The Wan-AI HF organization's newest repos are Wan2.2-Animate-2-14B (Jul and Aug 2026), Wan-Dancer-14B (Jul 2026), Wan2.2-S2V-14B, and the Wan2.2 T2V-A14B, I2V-A14B and TI2V-5B models. All are Apache 2.0, and **there are no Wan 2.5, 2.6, 2.7 or 3.0 repos**. — [HF: Wan-AI models](https://hf.co/Wan-AI/Wan2.2-TI2V-5B); [HF: Wan2.2-Animate-2-14B](https://hf.co/Wan-AI/Wan2.2-Animate-2-14B)
- Wan 2.5 and 2.6 are hosted-only (Alibaba Cloud Model Studio API and third parties). One Vibedex review claims Wan 2.6 weights exist, which conflicts with the repo evidence. — [howaiworks.ai (summary)](https://howaiworks.ai/blog/alibaba-wan-open-weights-stopped-at-2-2); [wan27.org](https://wan27.org/blog/wan-2-6-open-source-guide); contradicted by [vibedex.ai](https://vibedex.ai/blog/wan-26-review-2026)
- Wan 3.0 (30-second clips, launched Aug 2026) is closed and API-only, with no verified weights. — [The Next Web](https://thenextweb.com/news/alibaba-launches-wan3-video-model-after-share-sale); [WaveSpeed](https://wavespeed.ai/blog/commercial-compliance/is-wan-30-open-source/); [kenerateai](https://kenerateai.com/blogs/is-wan-3-0-open-source)
- Wan 2.7: one roundup calls it Apache 2.0 open with 15s 1080p and audio. Runpod says no public 2.7 weights exist, and another source calls it "partially open". The HF org shows no 2.7 repo. — [Runpod](https://www.runpod.io/articles/guides/wan-2-7-runpod); [vdf.ai (summary)](https://vdf.ai/blog/best-local-video-generation-models/)

**Tencent HunyuanVideo 1.5**
- 8.3B parameters. License "tencent-hunyuan-community" (HF tag "other") with `extra_gated_eu_disallowed: true`, which suggests the EU is excluded. It has 480p/720p step- and sparse-distilled I2V variants and a 1080p super-resolution model. — [HF: tencent/HunyuanVideo-1.5](https://huggingface.co/tencent/HunyuanVideo-1.5); [arXiv 2511.18870](https://arxiv.org/html/2511.18870v2)
- It has no native audio (none of the repo tags mention audio). Live providers are fal-ai and wavespeed. — [HF](https://hf.co/tencent/HunyuanVideo-1.5)
- The derivative `yunyangge/MovieRoll` (12 Nov 2026) does long and streaming video on top of HunyuanVideo-1.5. — [HF](https://hf.co/yunyangge/MovieRoll)

**Sand.ai MAGI-2 Preview**
- Released 5 Aug 2026: 114B MoE with about 6B active parameters, 10-second videos with synchronized audio (T2V and I2V), Apache 2.0, and a roughly 307 GB repo. A distilled variant is "coming soon". — [HF: sand-ai/MAGI-2-preview](https://hf.co/sand-ai/MAGI-2-preview); [GitHub](https://github.com/SandAI-org/MAGI-2-preview); [ComfyUI Wiki](https://comfyui-wiki.com/en/news/2026-08-05-magi-2-preview)
- The only hardware reference is a Chinese report estimating about 0.5 yuan per 10s 1080p video for the distilled version, based on 8×H100 rental prices. That is a cost figure, not an official minimum. — [Sina Finance](https://finance.sina.cn/tech/2026-08-06/detail-inimiqxt4076666.d.html?vt=4)

**Kandinsky (Kandinsky Lab, formerly Sber AI)**
- Kandinsky 6.0 Video was released Oct 6, 2026 under MIT, with code, checkpoints and Diffusers support. It comes in Lite (3B) and Pro (29B; one source says 30.14B) sizes and makes 5s clips with 44 kHz audio including lip-synced speech. A separate VSR model upscales to Full HD. — [arXiv 2610.05608 via hyper.ai](https://hyper.ai/en/papers/2610.05608); [explainx.ai](https://explainx.ai/blog/kandinsky-6-video-open-source-29b-audio-video-mit-license-2026)
- An NVFP4 quantized `kandinskylab/FastKandinsky-6.0-Pro-NVPF4-QAD` (MIT, 30.1B) was posted 29 Oct and updated 25 Nov 2026. Its demo Space is `hugging-apps/fastkandinsky-6-pro`. — [HF](https://hf.co/kandinskylab/FastKandinsky-6.0-Pro-NVPF4-QAD)
- Kandinsky 5.0: Lite 2B and Pro 19B, open weights. — [arXiv 2511.14993](https://arxiv.org/html/2511.14993v2)

**Other notable open models seen on the HF Hub (Nov 2026)**
- `apple/FastFrames-L` and `FastFrames-S` (16 Nov 2026) are fine-tunes of Wan2.1-14B and 1.3B under the restrictive apple-amlr license, which bars commercial use. — [HF](https://hf.co/apple/FastFrames-L)
- `IFM/PAN2` world model (Apache 2.0, Oct 2026), `meituan-longcat/LongCat-Video` (MIT), and the NVIDIA `sana-video2-5b-720p` demo Space. — [HF PAN2](https://hf.co/IFM/PAN2); [HF LongCat](https://hf.co/meituan-longcat/LongCat-Video); [HF Space](https://hf.co/spaces/Efficient-Large-Model/sana-video2-5b-720p-demo)

### Inferences
- For **commercial use without restrictions**, the safest choices are Wan 2.2 (Apache 2.0), MAGI-2 Preview (Apache 2.0, but impractical hardware) and Kandinsky 6.0 (MIT). LTX-2.5 is free under $10M revenue. MiniMax H3 is effectively unusable in the US, EU, UK and South Korea without a paid license. HunyuanVideo 1.5 appears to exclude the EU.
- Open models **with native audio**: LTX-2.5, MiniMax H3, Kandinsky 6.0, MAGI-2. Without audio: Wan 2.2 (except S2V, which is speech-driven), HunyuanVideo 1.5.

### Gaps
- Could not get the live Artificial Analysis open-weights leaderboard numbers (artificialanalysis.ai was not fetched). The Nov 13 MarkTechPost figures come from a search summary only.
- Found nothing current on **Ovi, SkyReels V3, CogVideoX, Mochi or Step-Video** in late 2026. These appear superseded and are not trending on HF. The only data point: on a 4090 Mochi 1 takes about 8 min and HunyuanVideo about 6 min per clip (older figures, [localaimaster](https://localaimaster.com/blog/local-ai-video-generation)).
- The exact durations for LTX-2.5 and MiniMax H3 open checkpoints were not confirmed from model cards. One benchmark generated LTX-2.5 clips of 5, 15 and 20 s (see section 2).

## 2. Hardware: minimum VRAM, quantized versions, ComfyUI, time per clip (consumer GPU and free Colab T4)

### Takeaway
On a free **Colab or Kaggle T4 (16 GB)**, the realistic options are **Wan 2.2 TI2V-5B** (fits in 8 GB with offload; about 12 to 25 min per roughly 4 to 5s clip on a T4), **Kandinsky 5/6 Lite**, low-bit GGUF builds of **LTX-2.5**, and the distilled **HunyuanVideo 1.5** with offload (14 GB minimum). On an **RTX 4090**, distilled LTX-2.5 makes a 5s clip with audio in about 44 s. A 3060 12 GB is tight for LTX-2.5 and needs Q2 or Q3 GGUF plus lots of system RAM.

### Cited Findings
- **Wan 2.2 5B:** the ComfyUI docs say it fits on 8 GB with native offloading. The Q8_0 GGUF is 5.4 GB. The official repo claims a 5s 720p clip in under 9 min on a 4090. On an RTX 3070 Ti, a 5s 720p clip took about 10m52s (fp16) or 11m00s (Q4_K_M). A 480×480, 81-frame Q4 GGUF clip took about 181 s on an 8 GB laptop GPU. — [Runflow](https://www.runflow.io/blog/comfyui-wan-2-2-image-to-video); [alexanderharte.com](https://www.alexanderharte.com/wan-2-2-comfyui-guide/); [wan27.org GGUF guide](https://wan27.org/blog/wan-2-2-gguf-guide)
- **Wan 2.2 on a Colab T4:** an 81-frame GGUF clip takes about 12 to 20 min (12 to 25 min per 4s clip elsewhere). The 5B model runs on a T4, while the 14B crashed partway. — [wan27.org](https://wan27.org/blog/wan-2-2-comfyui-workflow-guide); [AICU note.com](https://note.com/aicu/n/n072491018e0c?hl=en)
- **Wan 2.2 14B:** a 720p guide targets a single 24 GB GPU. — [localaimaster](https://localaimaster.com/blog/wan-video-generation-guide); [localaimaster VRAM by GPU](https://localaimaster.com/blog/wan-vram-requirements-by-gpu)
- **LTX-2.5 VRAM:** estimates conflict. One source says 16 GB minimum, the official site lists 32 GB+ VRAM and 32 GB RAM, and another says 32 GB with FP8. — [innfactory](https://innfactory.ai/en/ai-models/lightricks-ltx/); [ltx.io](https://ltx.io/model/ltx-2-5); [airmore](https://airmore.ai/ai-review/ltx-2-5-review)
- **LTX-2.5 GGUF:** `unsloth/LTX-2.5-GGUF` (about 596k downloads, ComfyUI) and `Abiray/LTX-2.5-Distilled-GGUF`. On a 3060 12 GB, Q4_K_M reportedly does not fit, Q3_K_M is about 12.9 GB, and Q2_K plus a Q2 encoder fits 12 GB at low quality. Another report gives a 10s, roughly 0.5 MP clip in about 180 s on a 3060 12 GB with 96 GB system RAM. — [HF unsloth](https://hf.co/unsloth/LTX-2.5-GGUF); [HF Abiray](https://huggingface.co/Abiray/LTX-2.5-Distilled-GGUF); [openclawdc](https://openclawdc.com/blog/can-i-run-ltx-2-5-locally/); [ahmetbalaman](https://ahmetbalaman.com/en/blog/ltx-2-5-requirements-vram-speed-en/)
- **LTX-2.5 on a 4090** (distilled pipeline, CPU offload, FP8): 5s clips in about 43.7 to 43.9 s, 15s in about 56 to 59 s, 20s in about 68 s. — [ltx-ai.com review](https://ltx-ai.com/blog/ltx-2-5-review-local-audiovisual-video-generation)
- **Older 4090 comparison:** LTX-Video about 90 s, Wan 2.2 about 4.5 min, HunyuanVideo about 6 min, Mochi 1 about 8 min per clip. A 3060 12 GB takes 7 to 9 min per LTX-Video clip. — [localaimaster](https://localaimaster.com/blog/local-ai-video-generation)
- **HunyuanVideo 1.5:** 14 GB minimum with offloading (PyPI), e.g. an RTX 4080. ComfyUI docs say 24 GB for quality. Wan2GP claims as low as 6 GB. FP8 build: `unsloth/HunyuanVideo-1.5-720p-FP8`. Native ComfyUI support is documented. — [PyPI hyvideo](https://pypi.org/project/hyvideo-fork/); [ComfyUI docs](https://docs.comfy.org/tutorials/video/hunyuan/hunyuan-video-1-5); [HF FP8](https://huggingface.co/unsloth/HunyuanVideo-1.5-720p-FP8)
- **Kandinsky 6.0:** reportedly peaks at 13.7 GiB VRAM in HD at a 16 GB preset, and Pro needs about 58 GiB of system RAM (single source). The Lite download is about 27.8 GB. ComfyUI has a Kandinsky 5 tutorial. — [creativeainews](https://www.creativeainews.com/articles/kandinsky-6-open-audio-video-16gb-gpu-ram-2026/); [ComfyUI docs Kandinsky 5](https://docs.comfy.org/tutorials/video/kandinsky/kandinsky-5)
- **MiniMax H3:** GGUF, INT8 (W4A8/W6A8) and pruned "Tiny" ComfyUI builds exist, plus few-step Turbo, Flash and Hyperflow distillations. It has official Comfy support. — [HF unsloth](https://hf.co/unsloth/MiniMax-H3-GGUF); [HF hyperflow](https://hf.co/VideoRebirthAI/hyperflow-h3-flash); [comfy.org](https://comfy.org/minimax-h3/); [Spheron deploy guide](https://www.spheron.network/blog/deploy-minimax-h3-gpu-cloud/)
- **MAGI-2 Preview:** about 307 GB of weights, so it is datacenter-only (multi-H100). — [HF](https://hf.co/sand-ai/MAGI-2-preview); [Sina](https://finance.sina.cn/tech/2026-08-06/detail-inimiqxt4076666.d.html?vt=4)

### Inferences
- **Free Colab T4:** Wan 2.2 5B (GGUF Q8 or fp16 with offload) is the most proven. The T4 has no FP8 or bf16 tensor-core speedups, so FP8 checkpoints will be slow or need casting. Colab's limited system RAM (about 12 GB) is likely the bottleneck for LTX-2.5 and Kandinsky 6 Pro, which need heavy CPU offload.
- **Kaggle (2×T4 or P100):** ComfyUI uses one GPU per job by default, so the second T4 mainly helps run two jobs in parallel. This is an inference and was not verified.
- **Modal and Lightning AI credits** can rent A100 or H100 time. At roughly a minute per clip for LTX-2.5 distilled on a high-end GPU, $30 of credit would plausibly cover dozens of clips (inference, not measured).

### Gaps
- No verified free-tier limits were retrieved for Colab, Kaggle (30h/week), Lightning AI or Modal ($30/month) in Nov 2026. Those figures come from the task brief and are unconfirmed.
- No measured T4 timings for LTX-2.5, MiniMax H3 or Kandinsky 6.

## 3. Free Hugging Face Spaces (ZeroGPU) and gradio_client and MCP callability

### Takeaway
Many Spaces exist for every major open model, and several official or popular ones carry the **`mcp-server` tag**, which means Claude can call them as MCP tools through the HF MCP server, or from Python with `gradio_client`. Free accounts get only a few minutes of ZeroGPU per day, charged to the caller.

### Cited Findings
- **Official or popular video Spaces with the `mcp-server` tag** (HF Hub): `Lightricks/LTX-2.5` (official, updated 11 Oct 2026), `Lightricks/ltx-video-distilled` (1.6k likes), `Upsampler/wan-2-2-14b-image-to-video`, `TencentARC/scope-camera-video-generation` (Wan 2.2), `vml12/wan-video-studio`, `numanajmal0/wan-video-api`, `CAMOMAIL/Dream-wan2-2-fp8da-aoti-preview-2_first-last_video`, `DeepRat/LTX-Video-ZeroGPU-Optimized`, `Efficient-Large-Model/sana-video2-5b-720p-demo`, `hugging-apps/t3-video-4k`, `hugging-apps/qwen-video-edit` (editing), and `huggingface-projects/ai-video-composer` (ffmpeg composer). — [HF Space LTX-2.5](https://hf.co/spaces/Lightricks/LTX-2.5); [HF ltx-video-distilled](https://hf.co/spaces/Lightricks/ltx-video-distilled); [HF Upsampler Wan](https://hf.co/spaces/Upsampler/wan-2-2-14b-image-to-video); [HF TencentARC](https://hf.co/spaces/TencentARC/scope-camera-video-generation)
- **Other model Spaces (no mcp-server tag seen):** `multimodalart/Hunyuan-Video-1-5`, `hugging-apps/minimax-h3-flashgen-4step`, `Pika-Labs/pika-h3-flex`, `akshat2512/MiniMax-H3-video-generator`, `hugging-apps/fastkandinsky-6-pro`, `multimodalart/ltx2-audio-to-video`, and `victor/LongCat-Video-Avatar-1.6`. — [HF MiniMax-H3 card (demo spaces)](https://hf.co/MiniMaxAI/MiniMax-H3); [HF Hunyuan card](https://hf.co/tencent/HunyuanVideo-1.5); [HF Kandinsky](https://hf.co/kandinskylab/FastKandinsky-6.0-Pro-NVPF4-QAD)
- **ZeroGPU quota:** reported as 5 min/day for free accounts and 40 min/day for PRO (sources conflict). The quota is consumed by the **caller**, and a pre-check fails the call if remaining time is less than requested. Real projects hit "You have exceeded your free ZeroGPU quota". — [mcpservers.org huggingface-zerogpu](https://mcpservers.org/agent-skills/huggingface/huggingface-zerogpu); [HF forum](https://discuss.huggingface.co/t/zero-gpu-limit-reached-even-through-failed-attempts/177659); [GitHub PR](https://github.com/zikrofficial-X/Zikr/pull/257)
- The official HF MCP server connects to Hub discovery and to Gradio Spaces as tools. — [HF blog](https://huggingface.co/blog/building-hf-mcp)
- The community `hf-assets-mcp` MCP server generates assets through free HF Spaces. — [GitHub](https://github.com/IvanGlazyrin/hf-assets-mcp)

### Inferences
- Any Gradio Space is callable with `gradio_client` (`Client("Lightricks/LTX-2.5").predict(...)`) using an HF token. The endpoint names must be read from the Space's "Use via API" page, which was not verified per Space. At about 5 free GPU-minutes per day, expect only a handful of short clips daily. HF PRO ($9/month, price not verified here) raises this to about 40 min.

### Gaps
- Did not verify which of these Spaces currently run on ZeroGPU and which on paid hardware, or their current running status.

## 4. Cheap hosted inference prices (fal, Replicate, WaveSpeed)

### Takeaway
Open models cost roughly **$0.01 to $0.12 per second of video** on hosted APIs, so a 5s clip runs about $0.05 to $0.60. WaveSpeed is cheapest on fast variants, fal is cheapest on mainstream routes, and Replicate is usually pricier.

### Cited Findings
- **LTX-2.5 Pro on fal:** about $0.12/s at 720p (third-party). The older LTX-2 Pro on fal's own page is $0.06/s at 1080p, $0.12/s at 1440p and $0.24/s at 2160p. — [techsy.io](https://techsy.io/en/blog/best-ai-video-providers); [fal.ai LTX-2](https://fal.ai/models/fal-ai/ltx-2/text-to-video)
- **Wan 2.2 A14B on fal:** about $0.10/s. WaveSpeed Wan 2.2 Ultra Fast is about $0.01/s. Wan 2.5 (closed) on fal costs $0.05/s at 480p, $0.10/s at 720p and $0.15/s at 1080p. — [genrates.com fal](https://genrates.com/providers/fal); [ofox.ai](https://ofox.ai/blog/fal-vs-wavespeed-vs-atlascloud-video-api-2026/)
- **MiniMax H3 on fal:** Max Turbo is about $0.04/s ($0.028 before Nov 15) and Max (768p) about $0.08/s. — [techsy.io](https://techsy.io/en/blog/best-ai-video-providers)
- **HunyuanVideo 1.5:** fal is $0.075/s (480p only, up to 121 frames). WaveSpeed is about $0.02/s at 480p and $0.04/s at 720p. — [teamday.ai](https://www.teamday.ai/blog/fal-ai-pricing-2026); [ofox.ai](https://ofox.ai/blog/fal-vs-wavespeed-vs-atlascloud-video-api-2026/)
- **Replicate video:** roughly $0.07 to $0.25/s depending on model. fal is reportedly 20 to 40% cheaper on shared Wan models. — [teamday.ai comparison](https://www.teamday.ai/blog/ai-image-video-api-providers-comparison-2026); [aireiter](https://aireiter.com/blog/fal-ai-review-2026)
- HF Inference Providers route MiniMax H3 and HunyuanVideo 1.5 to fal-ai and wavespeed, billed through an HF account. — [HF MiniMax-H3](https://hf.co/MiniMaxAI/MiniMax-H3); [HF Hunyuan](https://hf.co/tencent/HunyuanVideo-1.5)

### Inferences
- The cheapest paid route for a 5s clip is WaveSpeed Wan 2.2 Ultra Fast at about $0.05, or HunyuanVideo 1.5 at 480p at about $0.10. The cheapest route with native audio is likely MiniMax H3 Turbo on fal at about $0.20 per 5s.

### Gaps
- Prices come from third-party aggregators and change often. Vendor pages for fal, Replicate and WaveSpeed were not fetched directly. No Replicate per-model price for LTX-2.5 or MiniMax H3 was found.

## 5. Connecting video models to Claude (MCP servers or REST)

### Takeaway
There are three working routes: (1) the **fal MCP server** (remote, API-key header, over 1,000 models, pay per run), (2) the **official Replicate remote MCP server** (covers the whole HTTP API), and (3) the **Hugging Face MCP server**, which exposes `mcp-server`-tagged Gradio Spaces such as `Lightricks/LTX-2.5` as tools and spends the caller's free ZeroGPU quota. A simple Python REST script (fal_client, replicate, gradio_client or huggingface_hub InferenceClient) also works from Claude Code.

### Cited Findings
- The fal.ai MCP server is hosted remotely, authenticated with an API-key header, gives access to over 1,000 models, and charges pay per run from fal credits. Replicate has an official remote MCP server covering every operation in its HTTP API. — [aituber.app](https://aituber.app/blog/best-mcp-servers-ai-video-generation/); [videoany.io](https://videoany.io/guides/best-image-generator-mcp-servers-claude)
- The HF MCP server connects Claude to Hub search and Gradio Spaces. Video generation there runs on ZeroGPU and draws on the caller's quota. — [HF blog](https://huggingface.co/blog/building-hf-mcp); [agentman.ai](https://agentman.ai/agentskills/connections/mcp-server/hugging-face)
- Gradio Spaces tagged `mcp-server` (e.g. `Lightricks/LTX-2.5`, `Lightricks/ltx-video-distilled`, the Wan 2.2 Spaces listed in section 3) expose MCP endpoints. — [HF Space search (mcp-server filter)](https://hf.co/spaces/Lightricks/ltx-video-distilled)
- The community `hf-assets-mcp` server wraps free HF Spaces for asset generation. — [GitHub](https://github.com/IvanGlazyrin/hf-assets-mcp)

### Inferences
- A practical zero-cost stack is Claude, then the HF MCP server, then the `Lightricks/LTX-2.5` Space (audio and video), limited to a few clips a day. A low-cost stack is Claude, then the fal MCP server, then LTX-2.5, MiniMax H3 Turbo or Wan 2.2 at roughly $0.05 to $0.60 per clip. Video jobs are asynchronous on fal and Replicate (submit, poll, then fetch a URL), so a REST script has to poll.
- A self-hosted ComfyUI on Colab, Kaggle or Modal can also be wrapped as an MCP tool (ComfyUI has an HTTP API), but this was not researched in depth.

### Gaps
- Did not verify exact install URLs or package names for the fal MCP and Replicate MCP servers, or whether a ComfyUI MCP server is maintained. Primary docs were not reachable.
