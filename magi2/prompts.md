# MAGI-2 — prompts جاهزة للنسخ واللزق

الأسلوب ده مبني على طريقة الكتابة الرسمية اللي Sand.ai اتدرب عليها الموديل
(`inference/prompt_enhancement/prompts/t2v.md` و `assets/sample_000.txt` في
[SandAI-org/MAGI-2-preview](https://github.com/SandAI-org/MAGI-2-preview)).

## إزاي تستخدمها
1. افتح موقع Sand.ai وسجّل دخول، واختار موديل MAGI-2.
2. انسخ الـ prompt كله بالإنجليزي، من أول `# global_caption` لآخره، والزقه.
3. خلي المدة **10 ثواني** والصوت شغال. الـ prompts مكتوبة على 10 ثواني بالظبط.
4. لو في خانة اسمها "Enhance prompt" اقفلها، لأن الـ prompt متحسّن أصلاً.

## قواعد عشان النتيجة تطلع حلوة
- اكتب كل حاجة بالإنجليزي، ما عدا الكلام اللي الشخصية هتقوله: سيبه بالعربي المصري بين علامات تنصيص.
- وصّف إيه اللي **باين** في الصورة، ومتكتبش إحساس عام زي "فيديو حلو".
- قسّم الـ 10 ثواني لـ 1-3 لقطات بأوقات محددة.
- حدد شكل الشخصية (الشعر والهدوم) واطلب إنه يفضل ثابت.
- اكتب الأصوات كل واحد بتوقيته (خطوات، ريح، كلام).
- الـ prompt الواحد يبقى فيه فعل رئيسي واحد أو اتنين. الحركات الكتير مع بعض بتبوّظ الجسم.

---

## 1) شارع مصري الصبح — بياع فول (واقعي + كلام عربي)

```
# global_caption

core_caption:A 10-second realistic street scene in an old Cairo alley at sunrise, where a ful vendor serves a bowl from his cart and greets the camera with one line in Egyptian Arabic.
format_and_structure:Single continuous take with a slow push-in, ending on a warm medium close-up of the vendor.
visual_design:Naturalistic documentary cinematography, true-to-life color, warm golden sunrise light against cool blue shadows, light dust in the air, shallow depth of field, 35mm lens.
audio_design:Morning street ambience: distant call of vendors, a metal ladle scraping a copper pot, light traffic far away, birds. One spoken line in Egyptian Arabic.

continuity_requirements:Keep the vendor's identity and outfit locked: man in his fifties, short grey beard, white skullcap, beige galabeya with rolled sleeves. | Keep the copper ful pot, the wooden cart and the alley layout fixed in place. | Hands keep five fingers and natural proportions while holding the ladle.

# shot_timeline

time_range_seconds:0.0 | 6.0
shot_caption:Wide-medium shot of the wooden cart with a large copper pot steaming in the golden light. The vendor dips a long metal ladle into the pot, lifts it, and pours the ful into a white ceramic bowl, then drizzles oil over it. Steam rises through the sunbeams.
camera_lighting_and_composition:Eye-level, stabilized slow push-in toward the cart. Low sun from frame left creates rim light on the steam.

time_range_seconds:6.0 | 10.0
shot_caption:The vendor places the bowl on the cart, looks into the camera with a broad smile, raises one hand and says the line. He ends holding a warm smile.
camera_lighting_and_composition:Medium close-up on his face and upper body, warm key light from the left, alley softly blurred behind.

# audio_event_timeline

0.0 | 6.0 : ladle scraping the copper pot and liquid pouring into the bowl, synced with the pour.
6.5 | 9.5 : dialogue, vendor, warm and cheerful: "صباح الفل يا باشا، الفول سخن ومستنيك!"
0.0 | 10.0 : soft morning street ambience and birds.

generation_requirements:No text, no logos, no modern cars in frame. | Photorealistic only; no cartoon or CGI look. | Lip movement synced with the Arabic line.
```

---

## 2) إعلان منتج — زجاجة برفان (Product ad)

```
# global_caption

core_caption:A 10-second luxury product commercial of a dark glass perfume bottle on a black reflective surface, revealed by a splash of water and gold light.
format_and_structure:Two shots: a macro detail shot, then a clean hero shot of the full bottle.
visual_design:High-end commercial look, deep black background, rich gold and amber highlights, high contrast with clean specular reflections, macro lens, ultra sharp.
audio_design:Deep cinematic bass hit, a crisp water splash, and a soft shimmering chime. No dialogue, no music vocals.

continuity_requirements:Keep the bottle geometry fixed: tall rectangular smoked-black glass bottle with a heavy gold cap. | The bottle stays upright and still; only light and water move. | No readable text or brand names on the bottle.

# shot_timeline

time_range_seconds:0.0 | 4.0
shot_caption:Extreme close-up gliding slowly along the edge of the black glass bottle. A thin line of gold light travels across the glass surface, revealing its smooth texture.
camera_lighting_and_composition:Macro slide from left to right, single hard gold light from behind, rest of the frame in deep black.

time_range_seconds:4.0 | 10.0
shot_caption:Cut to a centered hero shot. A crown of clear water splashes up around the base of the bottle in slow motion, droplets catch the gold light, then fall back and settle into a still mirror surface. The bottle stands glowing in the center.
camera_lighting_and_composition:Front-facing, low angle, very slow push-in. Gold rim light on both sides of the bottle, reflection visible on the black surface.

# audio_event_timeline

4.0 | 5.0 : deep bass hit synced with the splash.
4.2 | 6.5 : crisp water splash and falling droplets.
7.0 | 10.0 : soft shimmering chime as the surface becomes still.

generation_requirements:Water physics realistic and slow motion. | No warping of the bottle shape. | No text anywhere in the frame.
```

---

## 3) أنمي — ولد فوق سطح في القاهرة مع الحمام (Anime)

```
# global_caption

core_caption:A 10-second Japanese anime-style scene of a teenage boy on a Cairo rooftop at sunset releasing pigeons from a wooden coop, with the city and minarets glowing behind him.
format_and_structure:Two shots with one clean cut: a medium shot of the boy opening the coop, then a wide shot of the pigeons flying over the skyline.
visual_design:2D Japanese anime film aesthetic, cel shading, warm orange and pink sunset sky, purple shadows, soft glow on the edges, detailed painted background of rooftops, satellite dishes and minarets.
audio_design:Flapping wings, gentle wind, distant city ambience, and a far-away call to prayer echoing softly. No dialogue.

continuity_requirements:Keep the boy's identity locked: about 15 years old, messy black hair, white t-shirt, blue jeans, red sneakers. | Keep the wooden pigeon coop and rooftop layout fixed. | Strictly 2D anime style; never shift to 3D or live action.

# shot_timeline

time_range_seconds:0.0 | 5.0
shot_caption:The boy kneels beside a wooden pigeon coop, smiles, and swings its small door open. Pigeons hop out and burst into the air around him, his hair and shirt moving in the wind of their wings.
camera_lighting_and_composition:Medium shot from slightly low angle, sunset backlight from behind the boy creating a glowing rim on his hair.

time_range_seconds:5.0 | 10.0
shot_caption:Cut to a wide shot. The flock circles over the rooftops of Cairo against the orange sky, the boy small in the lower corner with one hand raised, watching them.
camera_lighting_and_composition:Wide shot, slow upward tilt following the flock, minarets silhouetted on the horizon.

# audio_event_timeline

2.0 | 6.0 : loud fluttering of many wings, synced with the pigeons leaving the coop.
0.0 | 10.0 : soft wind and distant city ambience.
6.0 | 10.0 : faint echoing call to prayer far away.

generation_requirements:Pigeons keep consistent bird anatomy while flying. | No text in the frame. | Keep the 2D anime look in both shots.
```

---

## 4) هوك لصانع محتوى — شاب بيكلم الكاميرا (Talking head، طولي 9:16)

> اختار نسبة **9:16** من الموقع.

```
# global_caption

core_caption:A 10-second vertical social-media hook of a young Egyptian man speaking directly to the camera in a modern home studio, delivering one energetic line in Egyptian Arabic.
format_and_structure:Single continuous vertical 9:16 shot with a subtle handheld feel and a quick punch-in on the last words.
visual_design:Clean modern creator look, soft key light from the front-left, warm practical lamp and purple LED strip in the background, shallow depth of field, natural skin tones.
audio_design:Clear close-mic voice with a small room tone. One spoken line in Egyptian Arabic. No music.

continuity_requirements:Keep the man's identity locked: mid-twenties, short black fade haircut, trimmed beard, black hoodie. | Face proportions stable during speech; lips synced to the words. | Background (lamp, shelf, LED strip) stays in place.

# shot_timeline

time_range_seconds:0.0 | 7.0
shot_caption:The man leans slightly toward the camera, raises his eyebrows, gestures with one open hand, and speaks with energy and confidence.
camera_lighting_and_composition:Vertical medium close-up, chest up, eye level, subject centered, light handheld micro-movement.

time_range_seconds:7.0 | 10.0
shot_caption:Quick smooth punch-in to a close-up as he finishes the line, points at the camera and gives a confident half smile.
camera_lighting_and_composition:Close-up framing the face, same lighting, background softly blurred.

# audio_event_timeline

0.3 | 9.0 : dialogue, man, energetic and confident: "استنى! متقفلش الفيديو… الحاجة اللي هقولهالك دي هتغير طريقتك في الشغل خالص."
0.0 | 10.0 : quiet room tone.

generation_requirements:Lip sync accurate to the Arabic line. | No on-screen text or captions. | Hands keep natural anatomy.
```

---

## 5) طبيعة — درون فوق البحر الأحمر والجبال (Drone)

```
# global_caption

core_caption:A 10-second cinematic drone shot flying low over the turquoise Red Sea toward red desert mountains at golden hour.
format_and_structure:Single continuous forward drone flight that rises at the end to reveal the full landscape.
visual_design:Photorealistic aerial cinematography, crystal clear turquoise water with visible coral reefs, warm red and orange mountains, long golden-hour shadows, natural saturation, smooth stabilized motion.
audio_design:Strong steady wind, gentle waves, and a slow cinematic ambient tone. No dialogue.

continuity_requirements:Keep the coastline, mountain shapes and reef positions stable; nothing pops in or warps. | Water motion realistic and continuous.

# shot_timeline

time_range_seconds:0.0 | 6.0
shot_caption:The drone glides fast and low over clear turquoise water; coral reefs and small fish shadows pass beneath. Small waves sparkle in the sunlight.
camera_lighting_and_composition:Low altitude, camera tilted slightly down, forward motion, sun ahead and slightly right.

time_range_seconds:6.0 | 10.0
shot_caption:The drone rises smoothly and tilts up as it reaches a white sandy shore, revealing a wide range of red desert mountains glowing in golden light under a clear sky.
camera_lighting_and_composition:Continuous rising crane-like move ending in a wide epic composition, horizon in the upper third.

# audio_event_timeline

0.0 | 10.0 : steady wind and soft waves.
6.0 | 10.0 : a slow rising ambient tone synced with the drone rising.

generation_requirements:No people, boats, buildings or text. | Smooth motion without jitter.
```

---

## 6) أكل — طبق كشري (Food close-up)

```
# global_caption

core_caption:A 10-second appetizing food shot of an Egyptian koshary bowl being finished with tomato sauce and crispy fried onions.
format_and_structure:Two shots: an overhead pour shot, then a slow side close-up of the finished bowl.
visual_design:Premium food commercial look, warm soft light, rich reds and golden browns, shallow depth of field, steam visible against a dark background, macro detail.
audio_design:Thick sauce pouring, crunchy fried onions falling, a light sizzle. No dialogue.

continuity_requirements:Keep the bowl fixed: round white ceramic bowl filled with rice, lentils, macaroni and chickpeas. | Food layers stay consistent between the two shots. | Hands, if visible, keep natural anatomy.

# shot_timeline

time_range_seconds:0.0 | 5.0
shot_caption:Top-down shot. A stream of thick red tomato sauce pours onto the center of the koshary, spreading over the rice and lentils, then a handful of crispy golden fried onions falls on top.
camera_lighting_and_composition:Perfect overhead framing, bowl centered, soft light from the top-left.

time_range_seconds:5.0 | 10.0
shot_caption:Cut to a low side angle close-up. Steam rises from the bowl as the camera slowly slides around it, showing the glossy sauce and crunchy onion texture.
camera_lighting_and_composition:Macro, slow 30-degree orbit, warm backlight making the steam glow.

# audio_event_timeline

0.5 | 3.5 : thick sauce pouring sound.
3.5 | 5.0 : crunchy onions falling.
5.0 | 10.0 : soft sizzle and steam.

generation_requirements:No text or logos. | Realistic food textures; no plastic look.
```

---

## Template فاضي تملاه بنفسك

```
# global_caption

core_caption:A 10-second [STYLE] scene of [WHO/WHAT] [DOING WHAT] in [WHERE], [TIME OF DAY].
format_and_structure:[Single continuous take / Two shots with one clean cut at 5.0s].
visual_design:[realistic / 2D anime / 3D Pixar-like / commercial], [colors], [lighting], [lens / depth of field].
audio_design:[ambience], [sound effects], [dialogue language or "No dialogue"].

continuity_requirements:Keep [character] identity locked: [age, hair, clothes]. | Keep [important object] shape fixed. | Keep [style] for the whole clip.

# shot_timeline

time_range_seconds:0.0 | 5.0
shot_caption:[What is visible and what happens, step by step].
camera_lighting_and_composition:[camera angle, movement, light direction].

time_range_seconds:5.0 | 10.0
shot_caption:[...].
camera_lighting_and_composition:[...].

# audio_event_timeline

[start] | [end] : [sound], synced with [visual action].
[start] | [end] : dialogue, [speaker], [tone]: "[الجملة بالعربي]"

generation_requirements:No text in the frame. | [anything that must not happen].
```
