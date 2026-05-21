import streamlit as st
import json
import os
import subprocess
import psutil
import time

if "backend_started" not in st.session_state:

    backend_running = False

    for process in psutil.process_iter():

        try:

            cmdline = process.cmdline()

            if (
                "node" in " ".join(cmdline)
                and
                "index.js" in " ".join(cmdline)
            ):

                backend_running = True
                break

        except:
            pass

    if not backend_running:

        subprocess.Popen(
            "node index.js",
            cwd="../backend",
            shell=True
        )

    st.session_state.backend_started = True

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="AI WhatsApp Personality Agent",
    page_icon="🤖",
    layout="centered"
)

# ==========================================
# LOAD DEFAULT PROMPT
# ==========================================

with open("../backend/default_prompt.json", "r") as file:

    DEFAULT_DATA = json.load(file)

DEFAULT_PROMPT = DEFAULT_DATA["prompt"]

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.stApp {
    background:
    radial-gradient(circle at top left, #1e1b4b, transparent 30%),
    radial-gradient(circle at bottom right, #312e81, transparent 30%),
    linear-gradient(135deg, #050816, #0f172a);
    color: white;
}

.main-title {
    font-size: 60px;
    font-weight: 800;
    text-align: center;
    margin-top: 20px;
    color: white;
}

.sub-title {
    text-align: center;
    color: #94a3b8;
    margin-bottom: 40px;
    font-size: 18px;
}

.glass-box {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 35px;
    border-radius: 28px;
    backdrop-filter: blur(18px);
    box-shadow: 0 0 40px rgba(99,102,241,0.2);
}

.stButton > button {
    width: 100%;
    height: 55px;
    border-radius: 18px;
    border: none;
    background: linear-gradient(90deg,#6366f1,#8b5cf6);
    color: white;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.02);
    box-shadow: 0 0 25px rgba(99,102,241,0.5);
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# HEADER
# ==========================================

st.markdown(
    '<div class="main-title">AI WhatsApp Personality Agent</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Create your own AI texting personality</div>',
    unsafe_allow_html=True
)

# ==========================================
# MAIN BOX
# ==========================================

st.markdown(
    '<div class="glass-box">',
    unsafe_allow_html=True
)

mode = st.radio(
    "Mode",
    [
        "Default Personality",
        "Custom Personality"
    ]
)

# ==========================================
# DEFAULT
# ==========================================

if mode == "Default Personality":

    st.text_area(
        "Default Personality",
        value=DEFAULT_PROMPT,
        height=300,
        disabled=True
    )

# ==========================================
# CUSTOM
# ==========================================

else:

    personality_name = st.text_input(
        "Personality Name",
        placeholder="Chaotic Meme Friend"
    )

    personality_description = st.text_area(
        "Personality Description",
        height=200,
        placeholder="Describe behavior..."
    )

    tone = st.selectbox(
        "Tone",
        [
            "Casual",
            "Funny",
            "Cool",
            "Flirty",
            "Confident",
            "Caring",
            "Dry Humor"
        ]
    )

    humor = st.slider(
        "Humor Level 😂",
        0,
        100,
        60
    )

    energy = st.slider(
        "Energy Level ⚡",
        0,
        100,
        70
    )

    emoji = st.slider(
        "Emoji Usage 🔥",
        0,
        100,
        40
    )

    creativity = st.slider(
        "Creativity 🧠",
        0,
        100,
        75
    )

# ==========================================
# DEPLOY BUTTON
# ==========================================

if st.button("⚡ Deploy Personality"):

    if mode == "Default Personality":

        final_prompt = DEFAULT_PROMPT

    else:

        final_prompt = f"""
You are a real young person casually chatting on WhatsApp like a close friend.

IMPORTANT:
- Always reply naturally and logically.
- Never sound robotic.
- Understand casual texting language.
- Reply like a real person texting.

PERSONALITY:
- Name: {personality_name}
- Description: {personality_description}
- Tone: {tone}

SETTINGS:
- Humor: {humor}/100
- Energy: {energy}/100
- Emoji Usage: {emoji}/100
- Creativity: {creativity}/100

FINAL RULE:
Reply naturally like a real WhatsApp conversation.
"""

    data = {
        "prompt": final_prompt
    }

    with open("../backend/prompt.json", "w") as file:

        json.dump(data, file, indent=4)

    st.success(
        "✅ Personality Updated Successfully"
    )


# ==========================================
# RESET SESSION BUTTON
# ==========================================

if st.button("🗑 Reset WhatsApp Session"):

    # ======================================
    # STOP NODE
    # ======================================

    subprocess.call(
        "taskkill /F /IM node.exe",
        shell=True
    )

    # ======================================
    # WAIT FOR FILE RELEASE
    # ======================================

    time.sleep(5)

    # ======================================
    # DELETE SESSION FILES
    # ======================================

    auth_path = "../backend/.wwebjs_auth"
    cache_path = "../backend/.wwebjs_cache"
    qr_path = "../backend/qr.png"

    if os.path.exists(auth_path):

        subprocess.call(
            f'rmdir /s /q "{auth_path}"',
            shell=True
        )

    if os.path.exists(cache_path):

        subprocess.call(
            f'rmdir /s /q "{cache_path}"',
            shell=True
        )

    if os.path.exists(qr_path):

        os.remove(qr_path)

    # ======================================
    # RESET SESSION STATE
    # ======================================

    if "backend_started" in st.session_state:

        del st.session_state["backend_started"]

    st.success(
        "✅ WhatsApp Session Reset Successfully"
    )

    st.info(
        "Refresh page once to generate new QR."
    )
    
st.markdown(
    '</div>',
    unsafe_allow_html=True
)