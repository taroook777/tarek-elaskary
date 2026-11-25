# AI Video Generation API Pricing (as of late November 2026)

Research date: 2026-11-25. Method: WebSearch only. WebFetch could not reach any host from this session (ai.google.dev and invideo.io failed DNS resolution), so no official pricing page was opened directly. Every number below comes from search-result snippets. Most are from third-party blogs or aggregators that cite official pages. Numbers marked **[UNVERIFIED]** come from a single secondary source or conflict with other sources. Per-clip figures marked "calc" are my own arithmetic (per-second rate × clip length).

## Official API prices per model (USD per second, 5s and 10s clips)

### Takeaway
Among direct first-party APIs, the cheapest 720p routes are Luma Ray 3.2 (about $0.06/s), PixVerse V6 (about $0.04/s silent) and Gemini Omni 1.2 Flash ($0.07/s with audio, GA since 5 Nov 2026). Mid-range: Kling 3.0 ($0.084–0.168/s), Runway Gen-4.5 ($0.12/s), Wan ($0.10–0.15/s) and Seedance 2.0 (about $0.15/s at 720p). Veo 3.1 Standard is the premium option at $0.40/s. The Sora API and Sora app are both shut down, and the Veo 3.1 Fast/Lite Gemini API previews may also be retired.

### Summary table (official / first-party list prices)

| Model | Res / audio | $/s | 5s clip (calc) | 10s clip (calc) | Status / confidence |
|---|---|---|---|---|---|
| Google Veo 3.1 Standard (Gemini API) | 720p/1080p, audio incl. | 0.40 | 2.00 | 4.00 (max 8s → $3.20) | Multiple secondary sources agree |
| Veo 3.1 Standard | 4K | 0.60 | 3.00 | — | same |
| Veo 3.1 Fast | 720p / 1080p / 4K | 0.10 / 0.12 / 0.30 | 0.50 / 0.60 | 8s: 0.80 / 0.96 | May have been retired on the Gemini API on 2026-10-22 **[UNVERIFIED]** |
| Veo 3.1 Lite | 720p / 1080p | 0.05 / 0.08 | 0.25 / 0.40 | 8s: 0.40 / 0.64 | same retirement caveat |
| Gemini Omni 1.2 Flash (Google) | 720p, audio | 0.07 | 0.35 | 0.70 (15s max → 1.05) | Google blog, GA on 2026-11-05 |
| Gemini Omni 1.1 Flash (previous) | 360p/720p/1080p/4K | 0.034 / 0.101 / 0.152 / 0.304 | — | — | Secondary source; 1.2 rates for non-720p resolutions not confirmed |
| OpenAI Sora 2 | 720p | 0.10 | 0.50 | 1.00 | **API shut down 2026-09-24** (historical) |
| Sora 2 Pro | 720p / 1024p / 1080p | 0.30 / 0.50 / 0.70 | 1.50 / 2.50 / 3.50 | 3.00 / 5.00 / 7.00 | Historical; batch was 50% off |
| Kling 3.0 (official, $0.14/unit) | 720p silent / audio | 0.084 / 0.126 | 0.42 / 0.63 | 0.84 / 1.26 | Secondary sources; prepaid minimum $700 |
| Kling 3.0 | 1080p silent / audio | 0.112 / 0.168 | 0.56 / 0.84 | 1.12 / 1.68 | same |
| Kling 3.0 | 4K | 0.42 | 2.10 | 4.20 | same |
| Seedance 2.0 (BytePlus ModelArk, token-billed) | 720p / 1080p | ~0.151 / ~0.374 | 0.76 / 1.87 | ~1.51 / ~3.74 | $7.00–7.70 per 1M tokens; conflicting $4.30–4.70 figure **[UNVERIFIED]** |
| Seedance 2.5 | 480–720p / 1080p | $10.70 / $11.70 per 1M tokens (~52% above 2.0) | — | — | Secondary |
| MiniMax Hailuo 2.3 | 768p / 1080p | per clip | 6s 768p $0.28 (~$0.047/s); 6s 1080p $0.49 (~$0.082/s) | 768p 10s $0.56 | Official MiniMax docs (via search snippet); possibly moved to "Legacy" **[UNVERIFIED]** |
| Hailuo 2.3 Fast | 768p / 1080p | per clip | 6s 768p $0.19; 6s 1080p $0.33 | 768p 10s $0.32 | same |
| Runway Gen-4.5 (API, $0.01/credit) | — | 0.12 (12 cr/s) | 0.60 | 1.20 | Secondary, consistent |
| Runway Gen-4 Turbo | — | 0.05 | 0.25 | 0.50 | Secondary |
| Runway Aleph 2.0 (editing) | — | 0.28 | 1.40 | 2.80 | Secondary; 56-credit minimum |
| Luma Ray 3.2 (API, per clip) | 540p / 720p / 1080p | 0.03 / 0.06 / 0.24 | 720p $0.30; 1080p $1.20 | 1080p $3.60 ($0.36/s) | Secondary; 10s pricing inconsistent with per-second rate |
| PixVerse V6 (225 credits = $1) | 720p silent / audio | ~0.04 / ~0.053 | 0.20 / 0.27 | 0.40 / 0.53 | Secondary, dated 2026-11-09 |
| PixVerse V6 | 1080p silent / audio | ~0.08 / ~0.102 | 0.40 / 0.51 | 0.80 / 1.02 | same |
| Alibaba Wan 2.7 (Model Studio intl.) | 720p / 1080p | 0.10 / 0.15 | 0.50 / 0.75 | 1.00 / 1.50 | Snippet attributes to Wan 2.7; Wan 2.6 rate unclear |
| Vidu Q3 (ShengShu) | — | no official figure found | — | — | Aggregators only (see below) |
| Sand.ai MAGI-2 | 1080p | 0.08 (brief's figure) | 0.40 | 0.80 | **[UNVERIFIED]**: no source found; Sand.ai price shows "N/A" |

### Cited Findings
- Veo 3.1 on the Gemini API: Standard $0.40/s at 720p/1080p and $0.60/s at 4K; Fast $0.10/$0.12/$0.30 (720p/1080p/4K); Lite $0.05/$0.08 (720p/1080p, no 4K). Audio is included and failed generations are not billed — [BenchLM](https://benchlm.ai/media-pricing/veo); [hooked.so](https://www.hooked.so/compare/veo-3-pricing); [8frame](https://www.8frame.co/blog/veo-3-1-price-comparison-2026); [CloudZero](https://www.cloudzero.com/blog/veo-3-pricing/)
- 8s clip costs: Lite $0.40 (720p) / $0.64 (1080p); Fast $0.80 / $0.96 — [GlobalGPT](https://www.glbgpt.com/hub/how-much-is-veo-3-1-subscription-cost/)
- Outlier: veo3gen.app claims Gemini API Veo costs $0.75/s. This conflicts with every other source — [veo3gen](https://www.veo3gen.app/blog/veo-3-1-pricing-plans)
- Google reportedly scheduled the Gemini API previews of Veo 3.1 Fast and Lite to shut down on 2026-10-22, with Gemini Omni Flash as the replacement. Single source, not confirmed — [Sera Studio](https://serastudio.app/en/insights/veo-3-1-fast-vs-lite)
- Gemini Omni 1.2 Flash: 30% price cut to $0.07/s for 720p, GA on 2026-11-05, native 15-second clips — [Google blog](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemini-omni-1-2-flash/); [eesel](https://www.eesel.ai/blog/gemini-omni-1-2-flash-pricing); [xenospectrum](https://xenospectrum.com/en/gemini-omni-flash-video-pricing/)
- Gemini Omni 1.1 Flash: about $0.10/s at 720p ($17.50 per 1M video output tokens); $0.0338 (360p), $0.1014 (720p), $0.152 (1080p), $0.304 (4K), audio included — [eesel 1.1](https://www.eesel.ai/blog/gemini-omni-1-1-flash-pricing); [Treza Labs](https://www.trezalabs.com/blog/gemini-omni-1-1-flash-api-pricing-through-a-pipeline)
- OpenAI's model page says the Sora 2 models and Videos API shut down on 2026-09-24 — [OpenAI Sora 2 Pro model page](https://developers.openai.com/api/docs/models/sora-2-pro); [eesel "final rates after the shutdown"](https://eesel.ai/blog/sora-2-in-the-api-pricing)
- Last Sora rates: sora-2 $0.10/s (720p); sora-2-pro $0.30 (720p), $0.50 (1024p), $0.70 (1080p); batch at half price — [BenchLM Sora (2026-09-11)](https://benchlm.ai/media-pricing/sora); [Activepieces](https://www.activepieces.com/blog/sora-2-api-pricing-per-second-and-per-plan-in-2026.md). fal listed Sora 2 Pro 1080p at $0.50/s instead — [fal](https://fal.ai/models/fal-ai/sora-2/text-to-video/pro)
- Kling official API: $0.14 per unit, prepaid 5,000 units for $700 (valid 180 days); 3.0 costs 0.8 units/s at 1080p silent ($0.112), 1.2 units/s with audio ($0.168), 3 units/s at 4K ($0.42); 720p $0.084 silent / $0.126 with audio — [aireiter](https://aireiter.com/blog/kling-api-pricing); [seedrouter](https://seedrouter.ai/blog/kling-3-0-api-pricing); [chinamodelapi](https://chinamodelapi.com/news/kling-3-0-api)
- Seedance 2.0 on BytePlus ModelArk: about $7.00 per 1M tokens (480p/720p), $7.70 (1080p); about $0.1512/s at 720p and $0.3742/s at 1080p; 5s clip $0.76 at 720p and $1.87 at 1080p. Tokens = W×H×24fps×s/1024 — [ArgoLink](https://argolink.io/en/blog/seedance-2-0-api-pricing); [ManyMotions](https://manymotions.com/blog/seedance-2-0-api). Conflict: Picassoia gives $4.30/$4.70 without video input and $7.00/$7.70 with video input — [Picassoia](https://blog.picassoia.com/seedance-api-pricing-key-byteplus-access-and-docs)
- Seedance 2.5 costs $10.70 per 1M tokens (480/720p) and $11.70 (1080p), about 52% above 2.0 — [techforum.ca](https://techforum.ca/articles/seedance-2-5-pricing-vs-seedance-2-0); [dev.to useapi](https://dev.to/useapi/seedance-20-api-pricing-the-cheapest-ways-to-run-it-compared-4kno)
- MiniMax Hailuo 2.3 pay-as-you-go: $0.28 (768p 6s), $0.56 (768p 10s), $0.49 (1080p 6s). Fast: $0.19, $0.32, $0.33 — [MiniMax pricing docs](https://platform.minimax.io/docs/guides/pricing-video); [Puter (Nov 2026)](https://developer.puter.com/tutorials/minimax-api-pricing/)
- Runway API: $0.01/credit, separate from app credits; Gen-4.5 12 cr/s, Gen-4 Turbo 5 cr/s, Aleph 2.0 28 cr/s (56-credit minimum). One source says the Gen-4.5 rate dropped from 25 to 12 cr/s in June 2026 — [videomake.ai](https://videomake.ai/blog/runway-ml-pricing); [aipresso](https://aipresso.com/blog/runway-pricing); [8frame](https://www.8frame.co/blog/runway-pricing-explained)
- Luma Ray 3.2 API: billed per clip; 5s 720p $0.30, 5s 1080p $1.20, 10s 1080p $3.60; tracker lists $0.03/$0.06/$0.24 per second (540/720/1080p), checked 2026-10-14; HDR+EXR 5s 1080p $3.60 — [aivideoatlas](https://aivideoatlas.com/pricing/luma/); [Picassoia Luma](https://blog.picassoia.com/luma-api-pricing-ray-3-2-api-docs-and-cost); [developersdigest](https://www.developersdigest.tech/models/video-generation/luma)
- PixVerse API: 225 credits = $1 (as of 2026-11-09); V6 uses 9 cr/s at 720p and 18 cr/s at 1080p silent, 12 and 23 cr/s with audio — [vidcost](https://vidcost.com/api/pixverse-api/); [Atlas Cloud PixVerse API](https://www.atlascloud.ai/blog/guides/pixverse-api)
- Alibaba Model Studio (international): $0.10/s at 720p and $0.15/s at 1080p (snippet ties these rates to Wan 2.7); Wan 2.6 Singapore pricing in CNY is about 0.73/s at 720p — [Alibaba Cloud Model Studio pricing](https://www.alibabacloud.com/help/en/model-studio/model-pricing); [aliyun wan2.6-t2v](https://help.aliyun.com/en/model-studio/wan2-6-t2v); [therundown Wan 2.6](https://www.therundown.ai/tools/wan-2-6)
- MAGI-2: Sand.ai's own API price is listed "N/A" by AnotherWrapper; Pixazo resells Magi 2.0 at $0.10/s for 720p; open weights are on HF under Apache 2.0 — [AnotherWrapper](https://anotherwrapper.com/tools/llm-pricing/video-models/magi-2-preview); [Pixazo](https://www.pixazo.ai/models/magi); [HF](https://huggingface.co/sand-ai/MAGI-2-preview)

### Inferences
- The cheapest high-quality official route with audio at 720p is Gemini Omni 1.2 Flash at $0.07/s ($0.35 per 5s). With Veo 3.1 Lite possibly retired on the Gemini API, Omni Flash appears to be Google's budget option. Veo 3.1 Lite on Vertex may still exist; this was not checked.
- Kling's official API needs a $700 prepaid minimum, so a solo creator would likely use an aggregator instead (fal, Kie or WaveSpeed match or beat the official rate).
- Seedance's token billing makes 1080p about 2.5× the cost of 720p. A creator should render at 720p and upscale if cost matters.

### Gaps
- Could not open any official pricing page directly (WebFetch blocked). Veo, Kling, BytePlus, Runway, Luma and PixVerse numbers come from secondary sources.
- Whether Veo 3.1 Fast/Lite is still served on the Gemini API or Vertex after 2026-10-22 is unconfirmed.
- No official Vidu Q3 price was found. MAGI-2's "$0.08/s at 1080p" figure from the brief was not found in any source.
- Gemini Omni 1.2 Flash prices at 1080p and 4K are unconfirmed.
- No Volcengine (China) CNY Seedance price was found.

## Aggregator prices: cheapest route per model

### Takeaway
No single aggregator is cheapest for everything. Kie.ai is usually lowest for Kling (about 10% below official). Replicate is reported cheapest for Seedance 2.5 at 720p, and Runware is cheapest at 480p. Atlas Cloud undercuts on PixVerse, Vidu and Luma. fal, Replicate and WaveSpeed price Veo 3.1 identically. Replicate is about 2× fal for Kling.

### Cited Findings
- Kling 3 (standard, silent, per second): fal and WaveSpeed at $0.084 (official parity), Replicate $0.168, Kie $0.0755 — [dev.to 6-seller table (Nov 2026)](https://dev.to/alex_uberllm/seedance-kling-and-veo-31-api-prices-per-second-compared-across-6-sellers-november-2026-287o) (a near-identical copy exists under another author, so it is not independent confirmation)
- Kie Kling 3.0: 720p 15.1 credits/s ($0.0755) silent, 22.7 credits/s ($0.1135) with audio; Kie claims about 10% below official — [Kie.ai](https://kie.ai/kling-3-0)
- Krea Kling 3.0: std $0.1764/s, pro $0.2352/s, 4K $0.441/s (marked up) — [Krea](https://www.krea.ai/blog/kling-3-0-api-access-guide-pricing-code-examples-for-multi-shot-ai-video)
- Atlas Cloud Kling 3.0 starts at $0.126/s ("~30% reduced") — [Atlas Cloud](https://www.atlascloud.ai/blog/tips/kling-3.0-review-features-pricing-ai-alternatives)
- Seedance 2.5 at 720p (per second): Replicate ~$0.23, Kie $0.315, WaveSpeed $0.36, fal ~$0.47 — [kinovi](https://kinovi.ai/blogs/fal-ai-alternatives); [cellcog](https://cellcog.ai/blog/seedance-2-5-pricing/). Runware at about $0.10/s for 480p is among the lowest — [infrabase](https://infrabase.ai/blog/image-video-generation-apis-compared)
- fal and Higgsfield charge about 2× the BytePlus token rate for Seedance 2.0 at 720p — [ArgoLink](https://argolink.io/en/blog/seedance-2-0-api-pricing)
- Fal is cheaper than Replicate for Kling; Replicate is cheaper for Seedance — [teamday fal vs Replicate (Nov 2026)](https://www.teamday.ai/blog/fal-ai-vs-replicate-comparison)
- Veo 3.1: fal, Replicate and WaveSpeed all list $0.20/s without audio and $0.10/s for Fast; Lite 720p about $0.03–0.05. Vertex matches Replicate for Veo 3.1 with audio. One source says fal dropped Veo on 2026-11-17 **[UNVERIFIED]** — [teamday providers](https://www.teamday.ai/blog/ai-image-video-api-providers-comparison-2026)
- Vidu Q3 aggregator prices: Atlas Cloud Turbo from $0.034/s, standard $0.07/s; CometAPI $0.056/s (360p) and $0.1232/s (720p/1080p); GPU.ai $0.098/s; APIXO Turbo $0.04/0.06/0.08 and Standard $0.07–0.16 by resolution — [Atlas Cloud Vidu Q3](https://www.atlascloud.ai/blog/guides/vidu-q3-api-guide); [CometAPI](https://www.cometapi.com/models/vidu/vidu-q3/); [GPU.ai](https://gpu.ai/models/gpuai/vidu-q3); [APIXO](https://apixo.ai/models/vidu-q3)
- PixVerse V6 on Atlas Cloud: flat $0.025/s (below official ~$0.04) — [Atlas Cloud PixVerse V6](https://www.atlascloud.ai/blog/tips/pixverse-v6-review)
- Luma on Atlas Cloud: pay-as-you-go from $0.03/s — [Atlas Cloud Luma Ray 3.2](https://www.atlascloud.ai/models/luma-ray-3.2)
- Seedance 2.0 Fast is listed at $0.09/s by some resellers; one gateway lists doubao-seedance-2.0-fast at $0.131/s at 720p — [CometAPI video pricing](https://www.cometapi.com/ai-video-api-pricing/); [Atlas Cloud cheapest APIs](https://www.atlascloud.ai/blog/tips/cheapest-ai-video-generation-api-2026)
- OpenRouter lists video models, including Sora 2 Pro and Wan 2.6, so it now does offer video generation; prices were not visible in the snippets — [OpenRouter Wan 2.6](https://openrouter.ai/alibaba/wan-2.6); [OpenRouter Sora 2 Pro](https://openrouter.ai/openai/sora-2-pro/pricing)
- Fal Kling 3.0 is about $0.029/s in one comparison. This conflicts with the $0.084 figure in the 6-seller table **[UNVERIFIED]** — [CometAPI](https://www.cometapi.com/ai-video-api-pricing/)

### Cheapest-route summary (720p unless noted; inference from findings above)
| Model | Cheapest found | $/s | 5s / 10s (calc) |
|---|---|---|---|
| Kling 3.0 std silent | Kie.ai | 0.0755 | 0.38 / 0.76 |
| Kling 3.0 with audio | Kie.ai | 0.1135 | 0.57 / 1.14 |
| Seedance 2.5 720p | Replicate | ~0.23 | 1.15 / 2.30 |
| Seedance (480p) | Runware | ~0.10 | 0.50 / 1.00 |
| Seedance 2.0 720p | BytePlus direct | ~0.15 | 0.76 / 1.51 |
| Veo 3.1 Fast | fal / Replicate / WaveSpeed (parity) | 0.10 | 0.50 / (8s max) 0.80 |
| PixVerse V6 | Atlas Cloud | 0.025 | 0.13 / 0.25 |
| Vidu Q3 Turbo | Atlas Cloud | 0.034 | 0.17 / 0.34 |
| Luma Ray 3.2 | Atlas Cloud / Luma direct | 0.03–0.06 | 0.15–0.30 / 0.30–0.60 |
| Gemini Omni 1.2 Flash | Google direct | 0.07 | 0.35 / 0.70 |
| Hailuo 2.3 Fast 768p | MiniMax direct | ~0.032 | (6s) 0.19 / 0.32 |

### Inferences
- For a script-based creator, Kie.ai (Kling) and Replicate or Runware (Seedance) look cheapest. fal offers the widest catalog at roughly official parity.
- Aggregator prices change weekly with promotions; re-check before committing.

### Gaps
- No pricing data found for EvoLink, Together AI video or Higgsfield API per-second rates. OpenRouter video prices were not shown in snippets.
- WaveSpeed and Runware coverage is thin (single-source).

## Consumer subscription plans and effective cost per clip

### Takeaway
Subscriptions can be cheaper per clip than APIs at high volume (Kling Standard about $0.13 per 720p clip; Flow/Google AI Pro about $0.40 per Veo Fast clip), but credits expire each cycle and the plans are not scriptable. Sora as a consumer product has been discontinued since 2026-04-26.

### Cited Findings
- Kling: Standard $10/mo for 660 credits (another source: $6.99 first month, then $8.80), Pro $37 for 3,000, Premier $207 for 18,000; a 720p Kling 3.0 clip costs about 10 credits; Kling 4.0 1080p 5s costs 118 credits; credits expire each cycle — [scenemakers](https://scenemakers.club/guides/ai-video-tool-prices); [camclo3d](https://camclo3d.com/blog/kling-ai-pricing)
- Hailuo: Standard $14.99 for 1,000 credits, Pro $54.99 for 4,500, Master $119.99 for 10,500, Max $216 for 27,000 with unlimited Hailuo 2.3/2.0/1.0 (another source says Max is $184) — [Atlas Cloud Hailuo pricing](https://www.atlascloud.ai/blog/tips/hailuo-ai-pricing-cost); [Higgsfield blog](https://higgsfield.ai/blog/best-affordable-ai-video-generators)
- Higgsfield: Starter $19/mo for 270 credits, Plus $59 ($47 yearly) for 1,200, Ultra $129 ($99 yearly) for 3,000; free plan has 0 credits; Veo Fast 8s about 20–32 credits — [Krea on Higgsfield](https://www.krea.ai/blog/what-is-higgsfield-ai-pricing-free-plan-and-alternatives-in-2026); [saascrmreview](https://saascrmreview.com/higgsfield-ai-review/); [perchanceai](https://perchanceai.art/blogs/higgsfield-ai-pricing)
- Google AI / Flow credits: AI Plus $4.99 for 200, AI Pro $19.99 for 1,000, AI Ultra $99.99 for 10,000 or $199.99 for 25,000; Veo 3.1 Fast about 20 credits, Quality about 100, Lite 10 credits (5 on Ultra) for 720p; 50 daily credits in Flow — [scenemakers](https://scenemakers.club/guides/ai-video-tool-prices)
- Runway app credits are separate from API credits; in-app Gen-4.5 is about 60 credits per 5s per one source — [aipresso](https://aipresso.com/blog/runway-pricing); [camclo3d Runway](https://camclo3d.com/blog/runway-pricing)
- Sora: "As of April 26, 2026, the Sora product is no longer available"; a September 2026 OpenAI forum reply says there is no timeline to restore video creation for Pro users — [OpenAI "Sora is here" page](https://openai.com/index/sora-is-here/); [OpenAI community](https://community.openai.com/t/allow-video-creation-sora-for-pro-users/1391063.md)

### Inferences (calc)
- Kling Standard: $10 / 660 credits ≈ $0.015/credit, so a 10-credit 720p clip costs about $0.15 (cheaper than any API). A Kling 4.0 1080p 5s clip (118 credits) costs about $1.79.
- Google AI Pro: $19.99 / 1,000 credits ≈ $0.02/credit, so a Veo Fast clip (about 20 credits) costs about $0.40, a Quality clip (about 100) about $2.00 and a Lite clip about $0.20. On Ultra $99.99 / 10,000 ≈ $0.01/credit, so Fast is about $0.20 and Lite about $0.05.
- Higgsfield Plus: $59 / 1,200 ≈ $0.049/credit, so a Veo Fast 8s clip (20–32 credits) costs about $0.98–1.57. That is more expensive than the Gemini API.
- Hailuo Max "unlimited" plans can make the effective cost per clip close to zero for heavy users (fair-use limits are unknown).

### Gaps
- Exact current credit costs per model and resolution inside each app are inconsistent across sources.
- No data found on Runway consumer plan prices for Nov 2026, Kling credits for 3.0 at 1080p, or ChatGPT video generation (appears absent).

## Resolution and audio differences

### Takeaway
Audio typically adds 30–50% (Kling +50%, PixVerse +33%). Moving from 720p to 1080p ranges from free (Veo Standard) through +20% (Veo Fast) and +33% (Kling silent) to 2–4× (Seedance about 2.5×, Luma 4×, PixVerse 2×).

### Cited Findings
- Veo 3.1: Standard is the same price at 720p and 1080p ($0.40), 4K is +50%; Fast 720→1080p +20%; audio is included in Gemini API prices; aggregators list Veo 3.1 without audio at $0.20/s (half) — [BenchLM](https://benchlm.ai/media-pricing/veo); [teamday](https://www.teamday.ai/blog/ai-image-video-api-providers-comparison-2026)
- Kling 3.0: 720p $0.084 → 1080p $0.112 silent; audio +50% ($0.126 / $0.168); 4K $0.42 — [aireiter](https://aireiter.com/blog/kling-api-pricing)
- Seedance 2.0: 720p ~$0.151/s vs 1080p ~$0.374/s (token count scales with pixels) — [ArgoLink](https://argolink.io/en/blog/seedance-2-0-api-pricing)
- PixVerse V6: 720p 9 → 1080p 18 credits/s; audio 12 / 23 credits/s — [vidcost](https://vidcost.com/api/pixverse-api/)
- Luma Ray 3.2: 540p $0.03, 720p $0.06, 1080p $0.24 per second — [aivideoatlas](https://aivideoatlas.com/pricing/luma/)
- Hailuo 2.3: 768p 6s $0.28 vs 1080p 6s $0.49 (+75%) — [MiniMax docs](https://platform.minimax.io/docs/guides/pricing-video)
- Omni 1.1 Flash: 360p $0.034, 720p $0.101, 1080p $0.152, 4K $0.304 — [Treza Labs](https://www.trezalabs.com/blog/gemini-omni-1-1-flash-api-pricing-through-a-pipeline)

### Inferences
- The most cost-efficient strategy is to generate at 720p and upscale separately. The exception is Veo 3.1 Standard, where 1080p costs no more than 720p.

### Gaps
- Audio-off pricing on the official Gemini API (if offered) was not confirmed.
- 480p rates for most models other than Seedance/Runware were not found.

## Simple REST APIs with API keys (scriptable from Claude)

### Takeaway
All of the major aggregators (fal, Replicate, WaveSpeed, Kie.ai, Runware, Atlas Cloud, OpenRouter) and most first-party APIs (Gemini API, Runway, Luma, MiniMax, Alibaba Model Studio, PixVerse) use bearer-key REST with an asynchronous submit-then-poll job pattern. The friction is in account setup, not the API: Kling's $700 prepaid minimum, BytePlus/Volcengine region and enterprise onboarding, and Vertex's GCP project setup. Consumer apps (Kling, Hailuo, Higgsfield web, Flow) are not scriptable with their subscription credits.

### Cited Findings
- Runway's developer portal sells credits at $0.01 with no subscription; API credits are separate from app credits — [videomake.ai](https://videomake.ai/blog/runway-ml-pricing)
- Kling API requires prepaid unit packages starting at $700 / 5,000 units — [aireiter](https://aireiter.com/blog/kling-api-pricing)
- MiniMax offers pay-as-you-go video pricing on its platform docs — [MiniMax](https://platform.minimax.io/docs/guides/pricing-video)
- Seedance is accessed through BytePlus ModelArk with token billing; key and access guides exist — [Picassoia](https://blog.picassoia.com/seedance-api-pricing-key-byteplus-access-and-docs)
- Vidu Q3 is served via async single-endpoint APIs on resellers — [reapi](https://reapi.ai/models/viduq3)
- OpenRouter has video model endpoints (Wan 2.6, Sora 2 Pro listing) — [OpenRouter](https://openrouter.ai/alibaba/wan-2.6)
- Sora API is shut down (not usable) — [OpenAI](https://developers.openai.com/api/docs/models/sora-2-pro)

### Inferences
- The easiest single key for a creator is fal or Replicate (broad catalog, pay-as-you-go, simple REST, official-parity pricing for most models). Kie.ai is a good budget key for Kling. Google's Gemini API key (AI Studio) is the simplest first-party option for Veo and Omni Flash.

### Gaps
- Higgsfield API, EvoLink and Together video API details were not found.
- Rate limits and concurrency per provider were not researched.
