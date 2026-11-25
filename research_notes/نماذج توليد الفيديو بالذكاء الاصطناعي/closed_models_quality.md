# Leading Closed/Proprietary AI Video Generation Models: Quality Rankings and Capabilities (as of late November 2026)

> Method note: Research date 2026-11-25. WebFetch was blocked for every host tried (artificialanalysis.ai, videogen.io, marktechpost.com, theozard.com), so all findings come from WebSearch results and snippets. Leaderboard numbers below are snippets of Artificial Analysis (AA) pages captured at unknown crawl dates. Different snapshots disagree by a few Elo points. Treat exact ranks and Elo values as approximate and check them against the live AA pages before publishing.

## 1. Artificial Analysis Video Arena leaderboard (T2V / I2V, with and without audio)

### Takeaway
AA now runs versioned boards ("AA-Video-T2V v2.1", "AA-Video-I2V v2.1"). In the most recent snapshots found, **Alibaba Wan 3.0** (closed) leads text-to-video with audio at about **1175 Elo**. Close behind are **Utopai X** (about 1166–1173), **HeyGen Video 1** (about 1156–1160), **MiniMax H3** (about 1158–1163) and **ByteDance Dreamina Seedance 2.5** (about 1155–1158). Image-to-video with audio has been led by **Seedance 2.0 / 2.5**, **Google Gemini Omni Flash** and MiniMax H3. One snapshot shows **MAGI-2** first on I2V at 1164. The top tier sits within roughly 20 Elo points, which is close to a statistical tie. **Veo, Kling and Sora do not appear in the T2V-with-audio top five** in these snapshots.

### Cited Findings
**Text-to-video (with audio), AA-Video-T2V v2.1**
- Snapshot A (main leaderboard page): #1 Wan 3.0, 1175. #2 Utopai X, 1173. MiniMax H3 (768p), 1163. Dreamina Seedance 2.5, 1155. Listed prices: Seedance 2.5 about $34/min, Wan 3.0 about $12/min. — [AA T2V leaderboard](https://artificialanalysis.ai/video/leaderboard/text-to-video)
- Snapshot B (embed version, appears older): #1 Wan 3.0, 1175. Utopai X, 1167. HeyGen Video 1, 1160. MiniMax H3 and Seedance 2.5 tied at 1158. — [AA T2V embed](https://artificialanalysis.ai/embed/text-to-video-leaderboard/leaderboard/text-to-video)
- An AA FAQ snippet also names Wan 3.0 the leader at 1175. The search engine flagged that page as last indexed about 224 days earlier, so the crawl date is unclear. — [AA T2V leaderboard](https://artificialanalysis.ai/video/leaderboard/text-to-video)
- Utopai X was "Released Sep 2026, No API available" and ranked #2 on AA T2V with audio. — [GMI Cloud on X](https://x.com/gmi_cloud/status/2113417234001633532); [AA T2V](https://artificialanalysis.ai/video/leaderboard/text-to-video?amp=&amp=)
- 36Kr reports that Utopai X is built by post-training MiniMax H3 and that access is only through Utopai's PAI platform. It describes Utopai X as a "Global No.1" model with 30s long takes at 1/10 of Seedance's price. — [36Kr](https://eu.36kr.com/en/p/4084870019197572)
- HeyGen Video 1 sits at about 1156–1160 (#3 to #6 depending on the snapshot), with an API price of $2.40/min. One listing says it **leads T2V without audio (1143)**. — [AA T2V](https://artificialanalysis.ai/video/leaderboard/text-to-video?amp=&amp=); [HeyGen blog](https://www.heygen.com/blog/best-video-models)
- MarkTechPost (Nov 13, 2026) reports:
  - Wan 3.0 leads AA T2V with audio at **1175 Elo** at $0.20/sec.
  - MiniMax H3 has T2V Elo **1161 (#3)** and I2V Elo **1133 (#4)** at $0.08/sec.
  - HeyGen Video 1 and **Pika H3 Flex** give "near-frontier Elo for $0.035–$0.04 per second".
  - Teamday instead puts Wan 3.0 at about $0.083/sec, so the price figures conflict.
  — [MarkTechPost](https://www.marktechpost.com/2026/11/13/best-ai-video-generation-models-2026/); [Teamday](https://www.teamday.ai/blog/best-ai-video-models-2026)
- MAGI-2 Preview ranks about #14–#21 on T2V at about 1035–1044 Elo, with its API listed as "Coming soon". — [AA T2V](https://artificialanalysis.ai/video/leaderboard/text-to-video?amp=&amp=)
- Older figure: Magic Hour's leaderboard lists "Dreamina Seedance 2.0 720p" at 1274 in an AA Elo column. That is not on the same scale as the current v2.1 numbers, so it likely comes from an older board version. — [Magic Hour](https://magichour.ai/model-leaderboard/text-to-video)
- VideoGen.io, dated near the research date, says **Gemini Omni Flash leads AA text-to-video**. This contradicts the AA snapshots above and could not be verified. — [VideoGen.io](https://videogen.io/best-ai-video-models)

**Image-to-video, AA-Video-I2V v2.1**
- One snapshot: #1 **MAGI-2**, 1164. #2 **Dreamina Seedance 2.5**, 1160. Gemini Omni Flash 1.2 sits in 17th place. — [AA I2V leaderboard](https://artificialanalysis.ai/video/leaderboard/image-to-video)
- I2V with audio, snapshot including non-current models (older):
  - #1 Seedance 2.0 720p, 1197
  - #2 Gemini Omni Flash, 1192
  - #3 grok-imagine-video-1.5-preview, 1115
  - #5 HappyHorse-1.1, 1108
  - Top open-weights model in that snapshot: LTX-2.3 Fast, 956
  — [AA I2V incl. non-current](https://artificialanalysis.ai/video/leaderboard/image-to-video?include-non-current=true)
- Another I2V-with-audio snapshot: Seedance 2.0 720p, 1191. MiniMax H3, 1184. Gemini Omni Flash, 1181. — [AA I2V open-weights filter](https://artificialanalysis.ai/video/leaderboard/image-to-video?audio-output=false&amp=&open-weights=true)
- invideo (August 2026) gives Seedance 2.0 at 1196 for I2V with audio. — [invideo](https://invideo.io/blog/best-ai-video-model/)
- fal.ai says Seedance 2.0 tops AA I2V. — [fal.ai](https://fal.ai/learn/tools/best-image-to-video-apis-2026)

**Video editing board (context)**
- On AA-Video-Editing v1.1, Gemini Omni Flash 1.2 ranks #2 at 1166 Elo, with a November 2026 release date. — [AA editing](https://artificialanalysis.ai/video/leaderboard/video-editing)

**Other arenas (not AA, for contrast)**
- LLM-Stats says Kling v3 leads its text-to-video board as of Nov 2026. — [LLM-Stats](https://llm-stats.com/leaderboards/best-ai-for-video-creation)
- Arena.ai (formerly LMArena) runs a separate T2V board with 660K+ votes, snapshot dated Nov 8, 2026. — [Arena.ai T2V](https://arena.ai/leaderboard/video/text-to-video)

### Inferences
- The AA T2V-with-audio frontier in late 2026 is crowded. Wan 3.0, Utopai X, HeyGen Video 1, MiniMax H3 and Seedance 2.5 sit within about 20 Elo points, so any of them could be "#1" depending on the snapshot date.
- Closed Chinese labs (Alibaba, ByteDance, MiniMax) dominate the top of the board. Google's entry is now Gemini Omni Flash rather than Veo.
- Kling 4.0 (Oct 2026) may be too new to have settled on the AA board. Its absence from the top five in these snippets may simply reflect crawl timing.

### Gaps
- Could not retrieve a full, dated top-15 list for any of the four views (T2V/I2V × audio/no-audio). AA could not be fetched, and search snippets give only the top 3–6 plus scattered entries.
- AA T2V without audio: only one data point was found (HeyGen Video 1 leading at 1143).
- Ranks and Elo for Kling 4.0, Veo 3.1, Runway Gen-4.5, Grok Imagine 1.5, Vidu Q3, PixVerse V6, Luma Ray3.2 and Pika H3 Flex on the current v2.1 boards were not found.

## 2. Per-model capabilities (latest version, release, audio, lip sync, duration, resolution, I2V, references, aspect ratios)

### Takeaway
By late 2026 native audio is standard among frontier models. The exceptions are Runway Gen-4.5 (likely silent) and Luma Ray3.2 (contested). Maximum clip length has moved to **30 seconds** for Wan 3.0, Seedance 2.5 and Kling 4.0. **OpenAI Sora has been discontinued** (app shut down Apr 2026, API shut down Sep 2026). **Google has not released Veo 4.** Its newest video model is **Gemini Omni 1.2 Flash** (GA Nov 5, 2026), while Veo 3.1 remains in the docs. Most specs below come from third-party explainers, and many conflict.

### Cited Findings

**ByteDance Seedance 2.5 (Dreamina / Doubao)**
- Release date conflicts across sources:
  - July 31, 2026 per [Gate.AI](https://gate.ai/blog/seedance-2-5-bytedance-specs-pricing-api-use-cases) and [Genape](https://genape.ai/blog/what-is-seedance-2-5)
  - Aug 7, 2026 per [OpenRouter](https://openrouter.ai/blog/insights/seedance-2-5-review/)
  - Unveiled June 23 with launch window July 3 per [Wireflow](https://www.wireflow.ai/seedance-2-1)
- Clips up to 30s per generation (Seedance 2.0 was 15s). Multi-round extension goes beyond 30s. — [MindStudio](https://www.mindstudio.ai/blog/what-is-seedance-2-5); [Miracamp](https://www.miracamp.com/learn/content-creation/seedance-2-5-bytedance)
- Native audio is generated in the same pass. One source claims 10+ languages. — [Gate.AI](https://gate.ai/blog/seedance-2-5-bytedance-specs-pricing-api-use-cases)
- Resolution conflicts across sources:
  - 480p/720p per OpenRouter (Sep 3, 2026)
  - Native 1080p, with a 4K variant mentioned, per [Morphic](https://morphic.com/resources/models/seedance-2-5)
  - Native 4K 10-bit per Wireflow (single source)
- Up to 50 multimodal references, first/last-frame control, and edit/extend. — [Gate.AI](https://gate.ai/blog/seedance-2-5-bytedance-specs-pricing-api-use-cases); [Morphic](https://morphic.com/resources/models/seedance-2-5)

**Google: Gemini Omni Flash (current) and Veo 3.1 (legacy line)**
- Gemini Omni Flash release history:
  - First shown at I/O in May 2026 (10s cap)
  - 1.1 Flash GA on Aug 27, 2026, adding scene extension, first/last-frame interpolation and 4K upscaling
  - **1.2 Flash GA on Nov 5, 2026**, adding 15s clips and multi-turn chat editing, at about $0.07/sec for 720p
  - Rolling out to Flow, Google Vids, Google Ads and the Gemini app for Ultra subscribers. Outputs carry SynthID.
  — [Google blog 1.2](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/); [Google Cloud blog](https://cloud.google.com/blog/products/ai-machine-learning/gemini-omni-1-2-flash-generally-available); [The Next Web](https://thenextweb.com/news/google-gemini-omni-1-2-flash-video-15-seconds-price-cut); [Google blog 1.1](https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/)
- Omni 1.2 audio: "more natural dialogue, clearer lip-sync, distinct multi-speaker conditioning". It generates speech, music and SFX. Duration is 3–15s in 1s steps. Aspect ratios are 16:9 and 9:16 only. Resolution is 360p/720p/1080p/4K (via upscale, per a third-party guide). — [Google blog](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/); [Kie.ai](https://kie.ai/blog/what-is-gemini-omni-1-2-flash); [DeepMind model card](https://deepmind.google/models/model-cards/gemini-omni-1-2-flash/)
- References: the earlier Omni Flash took up to 5 images + 1 video. No 1.2-specific count was found. — [Artlist help](https://help.artlist.io/hc/en-us/articles/37099208586013-Gemini-Omni-Flash)
- invideo testing of Omni Flash (pre-1.2): single-speaker lip sync holds consistently for about 6–7s per clip. — [invideo](https://invideo.io/faq/what-is-gemini-omni-flash-and-what-can-it-do/)
- Veo 4 status:
  - No Veo 4 announced as of October 2026, and I/O 2026 passed without one. — [Zebracat](https://www.zebracat.ai/features/veo-4-video-generator); [Evolink](https://evolink.ai/blog/veo-4-release-date-2026)
  - Veo 3.1 is still listed as current in the Gemini API and Vertex docs. Veo 3.1 Lite launched Mar 31, 2026. — [Evolink](https://evolink.ai/blog/veo-4-release-date-2026); [aisiteflow](https://aisiteflow.agency/blog/google-veo-4-release-date-gemini-omni-flash-2026)
  - Sources disagree on whether Omni "replaces" Veo. — [aireiter](https://aireiter.com/blog/veo-4)
- Veo 3.1 is widely described as the most dependable model for dialogue lip sync (about 120ms accuracy claim, unverified). — [3daistudio](https://www.3daistudio.com/blog/best-ai-video-generator-2026); [pixo](https://pixo.video/blog/seedance-vs-veo-vs-kling)

**Kuaishou Kling 4.0**
- Release history: Kling 4.0 Flash preview on Sep 28, 2026 (top-tier subscribers). The full Kling 4.0 launched globally in Oct 2026, with sources giving Oct 15 or Oct 19. — [Wikipedia](https://en.wikipedia.org/wiki/Kling_AI); [imaginetovideo](https://imaginetovideo.com/blog/kling-ai-4-0-guide-4k-hdr-30-second-video); [wavespeed](https://wavespeed.ai/blog/ai-news/kling-4-0-release-date/)
- Duration and audio:
  - 3–30s native, adjustable in 1s steps, default 10s
  - Flash tier capped at 20s
  - 2-minute extension "coming soon"
  - Stereo audio, with lip sync "across multiple languages, dialects and accents" (9 or 10+ languages depending on source)
  - Audio reference is voice only
  — [explainx](https://www.explainx.ai/blog/kling-4-0-launch-30-second-video-stereo-audio-flash-mcp-cli-2026); [scenemixer](https://scenemixer.com/guides/kling-4-0-new-features/)
- Up to 4K. 10-bit HDR was listed as "coming soon", so its availability is contested. — [imaginetovideo](https://imaginetovideo.com/blog/kling-ai-4-0-guide-4k-hdr-30-second-video)
- Predecessor Kling 3.0 (early 2026): T2V, I2V, multi-shot storyboarding, reference-based generation, native 4K/60fps, 15s. Kling 3.0 Turbo followed on Jun 17, 2026. — [Wikipedia](https://en.wikipedia.org/wiki/Kling_AI); [pexo](https://pexo.ai/blog/what-is-kling-3-0-turbo-3190)

**OpenAI Sora 2 (discontinued)**
- Timeline: OpenAI announced the discontinuation on Mar 24, 2026. The Sora app and sora.com shut down Apr 26, 2026. The API shut down Sep 24, 2026. No successor has been named. — [ChatForest](https://chatforest.com/reviews/sora-2-openai-video-generation-discontinued/); [glbgpt](https://www.glbgpt.com/hub/openai-sora-2-pro-availability-guide/); [Krea](https://www.krea.ai/models/sora2)
- These are secondary sources quoting OpenAI's notices, and the dates are consistent across them. Sora 2 originally launched in Sep–Oct 2025 with native audio and "cameos" (older information). — [NBC News](https://www.nbcnews.com/tech/tech-news/openai-announces-sora-2-ai-video-audio-app-rcna234753)

**Runway Gen-4.5**
- Gen-4.5 has been on the Runway API since Feb 10, 2026. No "Gen-5" was found. — [Runway API changelog](https://docs.dev.runwayml.com/api-details/api_changelog/)
- An October 2026 comparison calls Gen-4.5 silent (no native audio). Another review says audio was added to Gen-4 in May 2026, which conflicts. — [aivideopicks](https://aivideopicks.com/posts/runway-review-2026.html); [Runway docs](https://docs.dev.runwayml.com/guides/models/)
- Runway now hosts third-party models: Wan 3.0, MiniMax H3 and Seedance 2.5. Its own audio-capable release is GWM Worlds 2, a real-time world model at 720p/24fps with 48kHz audio. — [Runway Wan 3.0](https://runway.com/product/models/wan-3.0); [Runway changelog](https://runway.com/changelog)

**MiniMax H3 / Hailuo 3.0**
- Release: Jul 31, 2026, on the API (model ID MiniMax-H3) and in the Hailuo app. There is also an H3 Max tier. — [MiniMax blog](https://www.minimax.io/blog/minimax-h3); [DataNorth](https://datanorth.ai/news/minimax-releases-minimax-h3)
- Native stereo audio at 32kHz. This is new, since Hailuo 2.3 was silent. — [Morphic](https://morphic.com/resources/models/minimax-h3)
- Up to 2K at 24fps, clips of 4–5s up to 15s. — [Morphic](https://morphic.com/resources/models/minimax-h3)
- **Not strictly closed:** base weights were published on Hugging Face in Aug 2026 under a restricted community license. The open weights have a 768p ceiling and exclude the US, EU, UK and South Korea. — [HF blog](https://huggingface.co/blog/ResterChed/minimax-h3-hailuo-3-0); [Yowox](https://yowox.com/posts/ai-video-models-quality-cost-access-diverge-2026/); [LeadWave](https://getleadwave.io/blog/best-ai-video-generators)

**Alibaba Wan 3.0 (closed; earlier Wan flagships were open)**
- Release: public beta Aug 6, 2026, GA Aug 24, 2026. API only, with no open weights. — [llm-stats](https://llm-stats.com/blog/research/wan-3.0-launch); [wireread](https://wireread.com/news/alibaba-launches-wan3-0-video-model-with-30-second-clips)
- Clips of 2–30s or a "smart" length (predecessor Wan2.7-Video was 15s). Native audio is on by default and covers speech, ambience and SFX. Resolution is 480p/720p/1080p. A "Prime" tier exists. — [Morphic](https://morphic.com/resources/models/wan-3-0); [Atlas Cloud](https://www.atlascloud.ai/models/wan-3.0)
- References and document-to-video are supported. — [Fuser](https://fuser.studio/articles/wan-3-0-guide); [Morphic](https://morphic.com/resources/models/wan-3-0)
- Available on Alibaba Cloud Model Studio, Qwen Cloud, Runway and fal, from about $0.05/sec at 480p. — [Atlas Cloud](https://www.atlascloud.ai/models/wan-3.0)

**xAI Grok Imagine Video 1.5**
- Release: preview around May 30–Jun 3, 2026, GA around Jun 16–17, 2026 on the API, grok.com and the apps. — [The Decoder](https://the-decoder.com/xai-updates-grok-imagine-to-1-5-with-image-to-video-generation-at-720p-resolution/); [TechTimes](https://www.techtimes.com/articles/318635/20260618/grok-imagine-video-15-goes-live-xai-tops-ai-video-leaderboard-86-percent-below-sora.htm)
- Audio and speech are generated in the same pass. The fast variant makes 6s 720p clips. One source mentions 1080p T2V GA. Clips can be stitched. — [Kie.ai](https://kie.ai/blog/grok-imagine-video-1-5); [techjacksolutions](https://techjacksolutions.com/ai-brief/ai-video-news-grok-imagine-video-15-launches-25-second-gener/)
- The "#1" and "state-of-the-art" claims come from xAI itself. — [digitalapplied](https://www.digitalapplied.com/blog/grok-imagine-video-1-5-ai-video-marketing-2026-guide)

**HeyGen Video 1 / Utopai X (newer entrants)**
- HeyGen Video 1 was announced in Oct 2026 and claimed #1 on AA T2V at the time. It is now about #3–#6, priced around $0.04/sec. — [HeyGen blog](https://www.heygen.com/blog/best-video-models); [MarkTechPost](https://www.marktechpost.com/2026/11/13/best-ai-video-generation-models-2026/)
- Utopai X (Utopai Studios, Sep 2026): no public API, 30s long takes, a post-trained MiniMax H3. — [36Kr](https://eu.36kr.com/en/p/4084870019197572)

**Pika**
- Pika H3 Flex (Oct 29, 2026): 15s with synchronized audio. Pika 2.5 is still offered. — [LeadWave](https://getleadwave.io/blog/best-ai-video-generators); [Melies](https://melies.co/compare/ai-video-models)

**Luma Ray3.2**
- Released Jun 2026, generating 10s clips. Audio is contested: one source says none, Melies says "Partial". Ray3.14 offers native 1080p and up to 18s modification. — [Melies](https://melies.co/compare/ai-video-models); [Kingy AI](https://kingy.ai/news/best-ai-video-generator-2026/)

**Vidu (Shengshu)**
- Vidu Q3 has native audio, up to 16s, at 720p/1080p. A Q4 Preview is also listed (16s, with audio). — [Melies](https://melies.co/compare/ai-video-models); [LeadWave](https://getleadwave.io/blog/best-ai-video-generators)

**PixVerse V6**
- Released Mar 30, 2026, with native audio, 1–15s clips (one source says 8s) and up to 1080p. — [Atlas Cloud review](https://www.atlascloud.ai/blog/guides/pixverse-v6-review); [invideo PixVerse](https://invideo.io/blog/pixverse-ai-video-generator/)

**Sand.ai MAGI-2 Preview (note: open source, not closed)**
- Released Aug 5, 2026 under Apache 2.0. It is a 114B MoE model with 6B active parameters. — [HF](https://huggingface.co/sand-ai/MAGI-2-preview); [ComfyUI Wiki](https://comfyui-wiki.com/en/news/2026-08-05-magi-2-preview)
- Output: 10s only, with jointly generated audio. Generation runs at 512×896, then a refiner upscales to 1088×1920. Supports T2V and I2V. — [ComfyUI Wiki](https://comfyui-wiki.com/en/news/2026-08-05-magi-2-preview); [aiwiki](https://aiwiki.ai/wiki/magi_2)
- Ranks #1 on AA I2V in one snapshot (1164), but only about #14–21 on T2V. — [AA I2V](https://artificialanalysis.ai/video/leaderboard/image-to-video)

**Midjourney video**
- No 2026 video-model update was found. Midjourney's version history lists V8.2 (Jul 24, 2026) as its stable image model. The V1 video model (mid-2025, older information) had no audio. — [Wikipedia](https://en.wikipedia.org/wiki/Midjourney)

### Inferences
- Effective late-2026 "closed frontier" shortlist: Seedance 2.5, Wan 3.0, Kling 4.0, Gemini Omni 1.2 Flash (plus Veo 3.1), HeyGen Video 1, Utopai X and Grok Imagine 1.5. MiniMax H3 is semi-open.
- Three models reach 30s single generations: Wan 3.0, Seedance 2.5 and Kling 4.0. Google's Omni (15s) and MiniMax H3 (15s) are shorter.
- Runway has pivoted toward hosting other labs' models plus world models, rather than leading on native T2V quality.

### Gaps
- Aspect-ratio lists are missing for most models. Only Omni 1.2 (16:9 and 9:16) was confirmed.
- Exact reference-image limits are missing for Kling 4.0, Wan 3.0 and Omni 1.2.
- No primary-source specs were retrieved for Seedance 2.5 or Kling 4.0, whose resolution and release dates conflict across sources.
- Midjourney video 2026 status is unknown. No Runway Gen-5 was found.

## 3. Arabic dialogue / lip sync

### Takeaway
**No independent, head-to-head Arabic lip-sync test was found.** The only Arabic-specific claims are vendor or marketing statements:
- Seedance 1.5 Pro "only model that handles Arabic reliably" (older)
- Seedance 2.5 and MiniMax H3 Max "documented for native Arabic dialogue"

Kling 4.0 and Gemini Omni claim multilingual lip sync but do not name Arabic in the snippets found.

### Cited Findings
- An aimlapi blog claims Seedance 1.5 Pro is the only model that reliably handles Arabic, Korean and Portuguese lip sync. This refers to an older version. — [aimlapi](https://aimlapi.com/blog/best-ai-video-generators-2026-veo-3-1-kling-sora-2-seedance-more-compared)
- A third-party Arabic video page says Seedance 2.5 and MiniMax H3 Max are documented for native Arabic dialogue. It recommends testing a short line first. — [creativeclaw](https://creativeclaw.co/ai-video-generator/arabic/)
- Seedance 2.0 is credited with native lip sync in 8+ languages, without Arabic confirmed in the snippet. — [Medium / Data Science Collective](https://medium.com/data-science-collective/what-is-the-best-ai-video-model-in-2026-f93f0793657e)
- Kling 4.0 claims lip sync across multiple languages and dialects (9 to 10+). Kling 3.0 is said to handle dialogue in 5 languages, with Arabic not named. — [explainx](https://www.explainx.ai/blog/kling-4-0-launch-30-second-video-stereo-audio-flash-mcp-cli-2026); [pixo](https://pixo.video/blog/seedance-vs-veo-vs-kling)
- Veo 3.1 is described as the most reliable for dialogue lip sync, but no Arabic test is cited. — [3daistudio](https://www.3daistudio.com/blog/best-ai-video-generator-2026)

### Inferences
- Based on vendor claims only, Seedance (ByteDance) and MiniMax are the most likely to handle Arabic speech natively. Veo/Omni and Kling 4.0 are plausible candidates given their multilingual lip-sync claims.
- Dialect handling (Egyptian, Gulf or Levantine versus Modern Standard Arabic) is entirely untested in the public sources found. An in-house test is recommended.

### Gaps
- No benchmark, review or YouTube-style test covering Arabic pronunciation quality, dialect accuracy or viseme alignment was found for any model.

## 4. Strengths and weaknesses per model

### Takeaway
Public qualitative evidence is thin and mostly comes from vendor or SEO blogs. Common themes:
- **Seedance:** reference control and cinematic I2V
- **Veo/Omni:** reliable dialogue lip sync and editing, but limited to 2 aspect ratios with short reliable lip-sync windows
- **Kling:** motion, multi-shot and 4K
- **Wan 3.0:** long 30s clips at low cost
- **Runway Gen-4.5:** silent output
- **Grok Imagine:** speed and price, with self-reported quality claims

### Cited Findings
- Seedance 2.0/2.5: tops AA I2V, "animating stills into cinematic motion with native audio". Up to 50 references. — [fal.ai](https://fal.ai/learn/tools/best-image-to-video-apis-2026); [Gate.AI](https://gate.ai/blog/seedance-2-5-bytedance-specs-pricing-api-use-cases)
- Seedance 2.5 is the most expensive frontier model on AA at about $34/min, versus about $12/min for Wan 3.0. — [AA T2V](https://artificialanalysis.ai/video/leaderboard/text-to-video)
- Gemini Omni: strong on editing (#2 on the AA editing board). Lip sync holds about 6–7s for a single speaker (pre-1.2 test). Only 16:9 and 9:16. — [AA editing](https://artificialanalysis.ai/video/leaderboard/video-editing); [invideo](https://invideo.io/faq/what-is-gemini-omni-flash-and-what-can-it-do/); [Kie.ai](https://kie.ai/blog/what-is-gemini-omni-1-2-flash)
- Kling 3.0/4.0: multi-shot storyboarding, references, 4K/60fps. LLM-Stats ranks Kling v3 first on its own arena. — [Wikipedia](https://en.wikipedia.org/wiki/Kling_AI); [LLM-Stats](https://llm-stats.com/leaderboards/best-ai-for-video-creation)
- Grok Imagine 1.5: fast (6s 720p in about 25s), with claimed "better physics" and pricing 86% below Sora. The quality claims are self-reported. — [TechTimes](https://www.techtimes.com/articles/318635/20260618/grok-imagine-video-15-goes-live-xai-tops-ai-video-leaderboard-86-percent-below-sora.htm); [techjacksolutions](https://techjacksolutions.com/ai-brief/ai-video-news-grok-imagine-video-15-launches-25-second-gener/)
- PixVerse V6: one review lists "real flaws", but the details were not retrieved. — [Atlas Cloud](https://www.atlascloud.ai/blog/guides/pixverse-v6-review)

### Inferences
- For dialogue-heavy Arabic content, the shortlist to test is Seedance 2.5, Kling 4.0, Gemini Omni 1.2 / Veo 3.1 and Wan 3.0, all of which have native audio and at least 15s clips.

### Gaps
- No systematic, independent 2026 comparison was found on physics, character consistency or in-video text rendering (including Arabic script rendering).
