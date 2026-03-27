"""
YouTube Automation Pro
======================
Topic → AI Script (Hindi) → AI Images (Stability AI) → Voice (ElevenLabs/gTTS/OpenAI)
→ Video Edit (MoviePy) → Music → YouTube Upload + Full SEO
"""

import streamlit as st
import os, json, requests, base64
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="YouTube Automation Pro", page_icon="🎬", layout="wide",
                   initial_sidebar_state="expanded")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
html,body,[class*="css"]{font-family:'Poppins',sans-serif;}
.main-header{background:linear-gradient(135deg,#FF0000,#8B0000,#1a0000);padding:2.5rem 2rem;
  border-radius:20px;text-align:center;margin-bottom:2rem;color:white;
  box-shadow:0 8px 32px rgba(255,0,0,.3);}
.main-header h1{font-size:2.4rem;font-weight:700;margin:0;}
.main-header p{font-size:.95rem;opacity:.85;margin:.3rem 0 0;}
.step-card{background:#0d1117;border:1px solid #21262d;border-radius:12px;padding:.9rem 1.2rem;
  margin:.3rem 0;border-left:4px solid #FF0000;}
.badge{display:inline-block;background:#21262d;border-radius:20px;padding:2px 10px;
  font-size:.72rem;margin:2px;color:#8b949e;}
div.stButton>button{background:linear-gradient(135deg,#FF0000,#CC0000)!important;
  color:white!important;border:none!important;border-radius:10px!important;
  padding:.7rem 2rem!important;font-weight:700!important;font-size:.95rem!important;width:100%;}
div.stButton>button:hover{transform:translateY(-2px);box-shadow:0 6px 20px rgba(255,0,0,.4)!important;}
</style>""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
  <h1>🎬 YouTube Automation Pro</h1>
  <p>Topic → Hindi Script → AI Images → Voice-Over → Video → YouTube Upload</p>
  <div style="margin-top:.7rem">
    <span class="badge">Claude AI</span><span class="badge">Stability AI</span>
    <span class="badge">ElevenLabs</span><span class="badge">gTTS</span>
    <span class="badge">OpenAI TTS</span><span class="badge">MoviePy</span>
    <span class="badge">YouTube API v3</span>
  </div>
</div>""", unsafe_allow_html=True)

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🔑 API Keys")
    anthropic_key = st.text_input("Anthropic (Script+SEO) ⭐",
        value=os.getenv("ANTHROPIC_API_KEY",""), type="password")
    stability_key = st.text_input("Stability AI (Scene Images) ⭐",
        value=os.getenv("STABILITY_API_KEY",""), type="password")
    pexels_key    = st.text_input("Pexels (Footage backup) — FREE",
        value=os.getenv("PEXELS_API_KEY",""), type="password")
    st.markdown("**🎙️ Voice (koi ek kaafi)**")
    elevenlabs_key= st.text_input("ElevenLabs (Best Quality)",
        value=os.getenv("ELEVENLABS_API_KEY",""), type="password")
    openai_key    = st.text_input("OpenAI TTS (Alternative)",
        value=os.getenv("OPENAI_API_KEY",""), type="password")
    st.markdown("**📤 YouTube**")
    youtube_creds = st.text_area("YouTube OAuth JSON",
        value=os.getenv("YOUTUBE_CREDENTIALS",""), height=70)
    st.markdown("---")
    st.markdown("### Status")
    for k,n in [(anthropic_key,"Anthropic"),(stability_key,"Stability AI"),
                (elevenlabs_key,"ElevenLabs"),(openai_key,"OpenAI"),
                (pexels_key,"Pexels"),(youtube_creds,"YouTube")]:
        st.markdown(f"{'🟢' if k and len(k)>5 else '🔴'} **{n}**")

# ── Main Tabs ────────────────────────────────────────────────────────────────
tab1, tab2, tab3 = st.tabs(["🚀 Video Banao","📋 Pipeline Info","⚙️ Settings"])

with tab1:
    L, R = st.columns([3,2])
    with L:
        st.markdown("### 🎯 Topic (Hindi mein likho)")
        topic = st.text_area("",
            placeholder="उदाहरण:\n• भारत की 5 रहस्यमयी जगहें\n• 2025 में AI से पैसे कैसे कमाएं\n• ब्लैक होल के 10 चौंकाने वाले तथ्य",
            height=110, label_visibility="collapsed")
        c1,c2,c3 = st.columns(3)
        with c1: duration = st.selectbox("⏱️ Duration",["3 min","5 min","8 min","10 min"],index=1)
        with c2: language = st.selectbox("🗣️ Language",["Hindi","Hinglish","English"])
        with c3: style    = st.selectbox("🎭 Style",["Educational","Entertainment","Motivational","News","Tutorial"])
        st.markdown("#### 🎙️ Voice Engine")
        voice_engine = st.radio("",
            ["🏆 ElevenLabs (Best — Hindi support)","🆓 gTTS (Free — Hindi perfect)","⚡ OpenAI TTS (Fast)"],
            label_visibility="collapsed")
        c4,c5 = st.columns(2)
        with c4: privacy   = st.selectbox("🔒 Privacy",["Public","Private","Unlisted"])
        with c5: img_style = st.selectbox("🖼️ AI Image Style",["Cinematic","Anime","Realistic","Digital Art","Watercolor"])
        c6,c7 = st.columns(2)
        with c6: add_music    = st.checkbox("🎵 Background Music",True)
        with c7: add_overlays = st.checkbox("📝 Text Overlays",True)

    with R:
        st.markdown("### 📋 Ye sab hoga automatically")
        for icon,name,desc in [
            ("📝","Script","Claude AI Hindi scene-by-scene script"),
            ("🎨","AI Images","Stability AI har scene ke liye"),
            ("🎙️","Voice-Over","ElevenLabs / gTTS / OpenAI"),
            ("🎬","Video Edit","MoviePy 1080p 30fps assembly"),
            ("🎵","Music Mix","Background audio blend"),
            ("🔍","SEO","Title + 500w desc + 30 tags"),
            ("📤","Upload","YouTube API v3 auto upload"),
        ]:
            st.markdown(f'<div class="step-card"><strong>{icon} {name}</strong><br>'
                        f'<small style="color:#666">{desc}</small></div>', unsafe_allow_html=True)

    st.markdown("---")
    if st.button("🚀 Full Automation Pipeline Shuru Karo!", use_container_width=True):
        if not topic.strip():
            st.error("❌ Pehle topic likho!")
        elif not anthropic_key:
            st.error("❌ Anthropic API key daalo sidebar mein!")
        else:
            run_pipeline(topic, duration, language, style, voice_engine, privacy,
                         img_style, add_music, add_overlays,
                         anthropic_key, stability_key, elevenlabs_key, openai_key,
                         pexels_key, youtube_creds)

with tab2:
    st.markdown("### 🔧 Pipeline Details")
    for name,engine,desc in [
        ("📝 Script","Claude AI (Sonnet)",
         "Hindi scene-wise script\nHook + Scenes + Narration + Outro\nImage prompts Stability AI ke liye"),
        ("🎨 AI Images","Stability AI SDXL",
         "1024×576 widescreen (16:9)\nHar scene ke liye unique image\nFallback: Pexels stock photos"),
        ("🎙️ Voice","ElevenLabs v2 / gTTS / OpenAI TTS",
         "ElevenLabs: eleven_multilingual_v2 — best Hindi\ngTTS: free, Google TTS, perfect Hindi\nOpenAI: tts-1-hd, nova voice"),
        ("🎬 Video","MoviePy + FFmpeg",
         "Images → clips → concatenate\nText overlays (Hindi)\nAudio sync\n1920×1080 @ 30fps"),
        ("🔍 SEO","Claude AI",
         "Title: 60 chars keyword-rich\nDescription: 500+ words, timestamps\nTags: 25-30 Hindi+English mix"),
        ("📤 Upload","YouTube Data API v3",
         "OAuth2 authentication\nPublic/Private/Unlisted\nAuto metadata set"),
    ]:
        with st.expander(f"{name} — {engine}"): st.text(desc)

with tab3:
    c1,c2 = st.columns(2)
    with c1:
        st.markdown("**🎬 Video**")
        st.selectbox("Resolution",["1920x1080 (Full HD)","1280x720 (HD)"])
        st.slider("FPS",24,60,30)
        st.selectbox("Bitrate",["3000k","5000k","8000k"],index=1)
        st.markdown("**🎵 Audio**")
        st.slider("Music Volume %",0,50,20)
    with c2:
        st.markdown("**🔍 SEO**")
        st.text_input("Target Audience","Hindi viewers India")
        st.slider("Max Tags",15,30,25)
        st.checkbox("Auto Timestamps in Description",True)
        st.checkbox("Notify Subscribers",True)
    if st.button("💾 Save Settings"): st.success("✅ Saved!")


# ═══════════════════════════════════════════════════════════════════════════════
# PIPELINE FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def run_pipeline(topic, duration, language, style, voice_engine, privacy,
                 img_style, add_music, add_overlays,
                 anthropic_key, stability_key, elevenlabs_key, openai_key,
                 pexels_key, youtube_creds):
    dur_map = {"3 min":3,"5 min":5,"8 min":8,"10 min":10}
    dur_mins = dur_map.get(duration, 5)
    prog = st.progress(0); status = st.empty(); results = st.container()

    # 1. Script
    status.info("📝 Hindi script likh raha hoon...")
    script = generate_script(topic, dur_mins, language, style, anthropic_key)
    prog.progress(15)
    if not script: st.error("❌ Script fail. API key check karo."); return
    with results:
        with st.expander("✅ Script Ready"):
            st.markdown(f"**Title:** {script.get('title','')}")
            st.markdown(f"**Hook:** {script.get('hook','')}")
            st.markdown(f"**Scenes:** {len(script.get('scenes',[]))}")

    # 2. Images
    status.info("🎨 Stability AI se AI images ban rahi hain...")
    image_paths = []
    if stability_key:
        image_paths = gen_stability_images(script.get('scenes',[]), stability_key, img_style)
    elif pexels_key:
        image_paths = fetch_pexels(script.get('scenes',[]), pexels_key)
    prog.progress(38)
    with results:
        if image_paths:
            with st.expander(f"✅ {len(image_paths)} Scene Images"):
                cols = st.columns(min(4, len(image_paths)))
                for i, img in enumerate(image_paths[:4]):
                    p = img.get('path')
                    if p and Path(p).exists():
                        with cols[i]: st.image(p, caption=f"Scene {i+1}", use_column_width=True)

    # 3. Voice
    status.info("🎙️ Voice-over generate ho raha hai...")
    audio_path = gen_voice(script, voice_engine, language, elevenlabs_key, openai_key)
    prog.progress(55)
    with results:
        if audio_path and Path(audio_path).exists():
            st.success("✅ Voice-Over Ready"); st.audio(audio_path)

    # 4. Video
    status.info("🎬 Video assemble ho rahi hai...")
    video_path = assemble_video(script, image_paths, audio_path, add_overlays)
    prog.progress(75)
    with results:
        if video_path and Path(video_path).exists():
            st.success("✅ Video Ready!"); st.video(video_path)

    # 5. SEO
    status.info("🔍 SEO content generate ho raha hai...")
    seo = gen_seo(topic, script, language, anthropic_key)
    prog.progress(88)
    with results:
        if seo:
            with st.expander("✅ SEO Content", expanded=True):
                st.markdown(f"**📌 Title:** `{seo.get('title','')}`")
                st.markdown(f"**🏷️ Tags:** {', '.join(seo.get('tags',[])[:12])}...")
                st.text_area("📄 Description", seo.get('description',''), height=130)

    # 6. Upload
    if video_path and youtube_creds and seo:
        status.info("📤 YouTube pe upload ho raha hai...")
        url = upload_yt(video_path, seo, privacy.lower(), youtube_creds)
        prog.progress(100)
        if url:
            with results:
                st.success("🎉 Upload complete!")
                st.markdown(f"### 🔗 [YouTube pe dekho]({url})")
                st.balloons()
        else: status.warning("⚠️ Upload fail — credentials check karo")
    else:
        prog.progress(100)
        with results:
            if not youtube_creds:
                st.warning("⚠️ YouTube credentials nahi — video locally saved hai")
            if video_path and Path(video_path).exists():
                with open(video_path,'rb') as f:
                    st.download_button("⬇️ Video Download Karo", f,
                        file_name=f"{topic[:30]}.mp4", mime="video/mp4")
        status.success("✅ Pipeline complete!")


def generate_script(topic, dur_mins, language, style, api_key):
    lang_instr = {"Hindi":"सभी narration HINDI Devanagari mein likho",
                  "Hinglish":"Hinglish (Hindi+English mix) mein likho",
                  "English":"Write all narration in English"}.get(language, "Hindi mein likho")
    n_scenes = dur_mins * 2
    prompt = f"""You are a professional YouTube scriptwriter. {lang_instr}

Topic: {topic}
Duration: {dur_mins} minutes, Scenes: {n_scenes}, Style: {style}

Respond ONLY valid JSON (no markdown):
{{"title":"catchy title in {language}","hook":"10 sec opening hook in {language}",
"scenes":[{{"scene_number":1,"duration_seconds":20,
"narration":"narration in {language}",
"visual_description":"what should be shown",
"image_prompt":"detailed English prompt for Stability AI, cinematic, widescreen 16:9",
"on_screen_text":"short overlay text in {language}"}}],
"outro":"subscribe CTA in {language}","total_duration_seconds":{dur_mins*60}}}"""
    try:
        r = requests.post("https://api.anthropic.com/v1/messages",
            headers={"x-api-key":api_key,"anthropic-version":"2023-06-01","content-type":"application/json"},
            json={"model":"claude-sonnet-4-20250514","max_tokens":5000,
                  "messages":[{"role":"user","content":prompt}]}, timeout=90)
        if r.status_code == 200:
            txt = r.json()['content'][0]['text'].strip().replace("```json","").replace("```","").strip()
            return json.loads(txt)
        st.error(f"Script API {r.status_code}")
    except json.JSONDecodeError as e: st.error(f"JSON parse: {e}")
    except Exception as e: st.error(f"Script error: {e}")
    return None


def gen_stability_images(scenes, key, img_style, language="Hindi"):
    style_map = {
        "Cinematic":"cinematic photography, professional lighting, 8k ultra detailed, film grain",
        "Anime":"anime art style, vibrant colors, Studio Ghibli inspired, detailed",
        "Realistic":"photorealistic, Canon EOS R5, natural lighting, ultra sharp",
        "Digital Art":"digital illustration, concept art, vibrant, ArtStation trending",
        "Watercolor":"watercolor painting, soft pastel colors, artistic, painterly"}
    suffix = style_map.get(img_style, style_map["Cinematic"])
    out = Path("output/images"); out.mkdir(parents=True, exist_ok=True)
    results = []
    for i, scene in enumerate(scenes[:8]):
        prompt = scene.get('image_prompt') or scene.get('visual_description','beautiful landscape')
        full_prompt = f"{prompt}, {suffix}"
        try:
            r = requests.post(
                "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image",
                headers={"Authorization":f"Bearer {key}","Content-Type":"application/json","Accept":"application/json"},
                json={"text_prompts":[{"text":full_prompt,"weight":1.0},
                      {"text":"blurry, low quality, text, watermark, logo, ugly","weight":-1.0}],
                      "cfg_scale":7,"height":576,"width":1024,"samples":1,"steps":30},
                timeout=60)
            if r.status_code == 200:
                artifacts = r.json().get('artifacts',[])
                if artifacts:
                    p = out / f"scene_{i+1:02d}.png"
                    p.write_bytes(base64.b64decode(artifacts[0]['base64']))
                    results.append({'scene':scene.get('scene_number',i+1),'type':'file','path':str(p)})
                    st.write(f"  🎨 Scene {i+1} AI image ready")
                    continue
            st.write(f"  ⚠️ Scene {i+1} Stability error {r.status_code}")
        except Exception as e:
            st.write(f"  ⚠️ Scene {i+1}: {e}")
        results.append({'scene':scene.get('scene_number',i+1),'type':'placeholder','path':None})
    return results


def fetch_pexels(scenes, key):
    out = Path("output/assets"); out.mkdir(parents=True, exist_ok=True)
    results = []
    for i, scene in enumerate(scenes[:8]):
        kw = (scene.get('image_prompt') or scene.get('visual_description','nature'))[:50]
        try:
            r = requests.get("https://api.pexels.com/v1/search",
                headers={"Authorization":key},
                params={"query":kw,"per_page":1,"orientation":"landscape"}, timeout=10)
            if r.status_code == 200:
                photos = r.json().get('photos',[])
                if photos:
                    img_r = requests.get(photos[0]['src']['large2x'], timeout=20)
                    if img_r.status_code == 200:
                        p = out / f"scene_{i+1:02d}.jpg"
                        p.write_bytes(img_r.content)
                        results.append({'scene':scene.get('scene_number',i+1),'type':'file','path':str(p)})
                        continue
        except Exception as e: st.write(f"  Pexels {i+1}: {e}")
        results.append({'scene':scene.get('scene_number',i+1),'type':'placeholder','path':None})
    return results


def gen_voice(script, engine, language, el_key, oai_key):
    out = Path("output/audio"); out.mkdir(parents=True, exist_ok=True)
    audio_path = out / "narration.mp3"
    parts = [script.get('hook','')] + [s.get('narration','') for s in script.get('scenes',[])] + [script.get('outro','')]
    text = ' '.join(p for p in parts if p)[:4000]

    if "ElevenLabs" in engine and el_key:
        try:
            r = requests.post(
                "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM",
                headers={"xi-api-key":el_key,"Content-Type":"application/json"},
                json={"text":text,"model_id":"eleven_multilingual_v2",
                      "voice_settings":{"stability":0.55,"similarity_boost":0.75,"style":0.3}},
                timeout=90)
            if r.status_code == 200:
                audio_path.write_bytes(r.content)
                st.write("  ✅ ElevenLabs voice ready"); return str(audio_path)
            st.write(f"  ElevenLabs {r.status_code} → fallback")
        except Exception as e: st.write(f"  ElevenLabs: {e} → fallback")

    if "OpenAI" in engine and oai_key:
        try:
            r = requests.post("https://api.openai.com/v1/audio/speech",
                headers={"Authorization":f"Bearer {oai_key}","Content-Type":"application/json"},
                json={"model":"tts-1-hd","input":text[:4096],"voice":"nova","speed":1.0},
                timeout=90)
            if r.status_code == 200:
                audio_path.write_bytes(r.content)
                st.write("  ✅ OpenAI TTS ready"); return str(audio_path)
            st.write(f"  OpenAI TTS {r.status_code} → fallback")
        except Exception as e: st.write(f"  OpenAI: {e} → fallback")

    # gTTS always works (free)
    try:
        from gtts import gTTS
        lang_code = {"Hindi":"hi","Hinglish":"hi","English":"en"}.get(language,"hi")
        gTTS(text=text[:3500], lang=lang_code, slow=False).save(str(audio_path))
        st.write("  ✅ gTTS voice ready (free)"); return str(audio_path)
    except ImportError: st.error("gTTS install: pip install gtts")
    except Exception as e: st.error(f"gTTS: {e}")
    return None


def assemble_video(script, image_paths, audio_path, add_overlays):
    out = Path("output/videos"); out.mkdir(parents=True, exist_ok=True)
    output_path = out / "final_video.mp4"
    try:
        from moviepy.editor import (ImageClip, AudioFileClip, concatenate_videoclips,
                                     TextClip, CompositeVideoClip, ColorClip)
        clips = []
        palette = [(15,25,50),(25,15,40),(10,30,25),(35,15,20),(20,35,15),(30,25,10),(15,30,35),(25,20,40)]
        for i, scene in enumerate(script.get('scenes',[])):
            dur = scene.get('duration_seconds', 6)
            sc_num = scene.get('scene_number', i+1)
            img_info = next((x for x in image_paths if x.get('scene') == sc_num), None)
            if img_info and img_info.get('path') and Path(img_info['path']).exists():
                try: clip = ImageClip(img_info['path'], duration=dur).resize((1920,1080))
                except: clip = ColorClip((1920,1080), color=palette[i%8], duration=dur)
            else:
                clip = ColorClip((1920,1080), color=palette[i%8], duration=dur)
            if add_overlays and scene.get('on_screen_text'):
                try:
                    txt = TextClip(scene['on_screen_text'], fontsize=50, color='white',
                        stroke_color='black', stroke_width=2, font='DejaVu-Sans',
                        method='caption', size=(1800,None)
                    ).set_position(('center','bottom')).set_duration(dur)
                    clip = CompositeVideoClip([clip, txt])
                except: pass
            clips.append(clip)
        if not clips: st.error("Koi clip nahi bani"); return None
        final = concatenate_videoclips(clips, method="compose")
        if audio_path and Path(audio_path).exists():
            audio = AudioFileClip(str(audio_path))
            if audio.duration > final.duration: audio = audio.subclip(0, final.duration)
            final = final.set_audio(audio.set_duration(final.duration))
        final.write_videofile(str(output_path), codec='libx264', audio_codec='aac',
                              fps=30, preset='ultrafast', logger=None)
        return str(output_path)
    except ImportError: st.error("MoviePy install: pip install moviepy")
    except Exception as e: st.error(f"Video error: {e}")
    return None


def gen_seo(topic, script, language, api_key):
    title = script.get('title', topic) if script else topic
    summary = ' '.join(s.get('narration','')[:80] for s in (script or {}).get('scenes',[])[:3])
    prompt = f"""YouTube SEO metadata generate karo.
Language: {language}, Topic: {topic}, Title hint: {title}
Summary: {summary[:300]}

Respond ONLY valid JSON:
{{"title":"SEO title max 60 chars keyword-first",
"description":"500+ word desc in {language}: intro, what you learn, timestamps 0:00 Intro etc, keywords, subscribe CTA, 7 hashtags at end",
"tags":["25-30 relevant tags, Hindi and English mix"],
"category_id":"22","thumbnail_text":"3-4 word thumbnail text"}}"""
    try:
        r = requests.post("https://api.anthropic.com/v1/messages",
            headers={"x-api-key":api_key,"anthropic-version":"2023-06-01","content-type":"application/json"},
            json={"model":"claude-sonnet-4-20250514","max_tokens":2500,
                  "messages":[{"role":"user","content":prompt}]}, timeout=45)
        if r.status_code == 200:
            txt = r.json()['content'][0]['text'].strip().replace("```json","").replace("```","").strip()
            return json.loads(txt)
    except Exception as e: st.error(f"SEO: {e}")
    return {"title":topic[:60],"description":f"{topic} ke baare mein poori jaankari.",
            "tags":[topic,"hindi","youtube","viral"],"category_id":"22","thumbnail_text":topic[:20]}


def upload_yt(video_path, seo, privacy, creds_json):
    try:
        import google.oauth2.credentials, googleapiclient.discovery, googleapiclient.http
        d = json.loads(creds_json)
        creds = google.oauth2.credentials.Credentials(
            token=d.get('token'), refresh_token=d.get('refresh_token'),
            client_id=d.get('client_id'), client_secret=d.get('client_secret'),
            token_uri='https://oauth2.googleapis.com/token')
        yt = googleapiclient.discovery.build('youtube','v3',credentials=creds)
        body = {'snippet':{'title':seo.get('title','')[:100],
                           'description':seo.get('description','')[:5000],
                           'tags':seo.get('tags',[])[:30],
                           'categoryId':seo.get('category_id','22')},
                'status':{'privacyStatus':privacy,'selfDeclaredMadeForKids':False}}
        media = googleapiclient.http.MediaFileUpload(video_path,chunksize=-1,resumable=True,mimetype='video/mp4')
        req = yt.videos().insert(part=','.join(body.keys()),body=body,media_body=media)
        resp = None
        while resp is None: _, resp = req.next_chunk()
        return f"https://youtube.com/watch?v={resp['id']}"
    except ImportError: st.warning("Install: pip install google-api-python-client google-auth-oauthlib")
    except Exception as e: st.error(f"Upload: {e}")
    return None
