import streamlit as st
from PIL import Image
import random

st.set_page_config(page_title="Uff-AI 🔥 Roast Time!", page_icon="😈", layout="centered")

# CSS for style and scanner animation
st.markdown("""
    <style>
    body {
        background-color: #fff;
    }
    .main {
        background: linear-gradient(135deg, #ffe0e9, #ffd4b3);
        padding: 3rem;
        border-radius: 25px;
        box-shadow: 0px 0px 40px rgba(255, 70, 70, 0.3);
    }
    .title {
        font-size: 60px;
        text-align: center;
        font-weight: 900;
        color: #ff1744;
        text-shadow: 2px 2px #000;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.04); }
        100% { transform: scale(1); }
    }
    .subtitle {
        text-align: center;
        font-size: 26px;
        color: #d50000;
        margin-bottom: 30px;
    }
    .upload-section {
        background-color: #fff6f7;
        border: 2px dashed #ff1744;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 30px;
    }
    .upload-instruction {
        color: #ff0000;
        font-size: 20px;
        font-weight: bold;
    }
    .button-style div.stButton > button {
        width: 100%;
        padding: 15px;
        font-size: 24px;
        background: linear-gradient(45deg, #ff1744, #ff9100);
        color: white;
        border-radius: 15px;
        border: none;
        font-weight: bold;
        box-shadow: 0px 4px 10px #ff1744a0;
        transition: all 0.3s ease-in-out;
    }
    .button-style div.stButton > button:hover {
        transform: scale(1.05);
    }
    .side-by-side {
        display: flex;
        justify-content: center;
        align-items: flex-start;
        gap: 40px;
        margin-top: 30px;
    }
    .animal-img, .user-img {
        border-radius: 20px;
        max-width: 350px;
        box-shadow: 0px 4px 25px rgba(0,0,0,0.25);
        position: relative;
    }
    .scanner {
        position: relative;
    }
    .scanner::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: linear-gradient(to bottom, rgba(255,0,0,0.2) 0%, rgba(255,0,0,0.6) 50%, rgba(255,0,0,0.2) 100%);
        animation: scan 2s infinite linear;
        pointer-events: none;
    }
    @keyframes scan {
        0% { background-position: 0 -100%; }
        100% { background-position: 0 100%; }
    }
    .roast-box {
        font-size: 28px;
        font-weight: bold;
        color: #880e4f;
        background: #fff0f3;
        padding: 25px;
        border-radius: 20px;
        margin-top: 25px;
        text-align: center;
        box-shadow: 0px 0px 20px rgba(255, 23, 68, 0.2);
    }
    .you-look {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
        color: #e53935;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<div class="title">🔥 Uff-AI: Roast Me, Baby! 🔥</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Upload your selfie and get absolutely DESTROYED 😂</div>', unsafe_allow_html=True)

st.markdown('<div class="upload-section">', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    '<span class="upload-instruction">📸 Choose your face to get flamed!</span>', 
    type=["jpg", "jpeg", "png"], 
    label_visibility="collapsed"
)

st.markdown('</div>', unsafe_allow_html=True)

# Animal images
animals = {
    "Buffalo": "https://cdn.pixabay.com/photo/2021/06/20/15/41/buffalo-6351369_1280.jpg",
    "Sloth": "https://cdn.pixabay.com/photo/2024/04/30/18/30/ai-generated-8730753_1280.jpg",
    "Goose": "https://cdn.pixabay.com/photo/2014/06/29/13/08/gosling-379393_1280.jpg",
    "Llama": "https://cdn.pixabay.com/photo/2021/08/02/18/04/llama-6517467_1280.jpg",
    "Alpaca": "https://cdn.pixabay.com/photo/2018/03/20/22/22/alpaca-3244928_1280.jpg",
    "Pufferfish": "https://cdn.pixabay.com/photo/2024/08/07/11/59/animal-8951854_1280.jpg",
    "Warthog": "https://cdn.pixabay.com/photo/2020/03/13/10/18/africa-4927528_1280.jpg",
    "Narwhal": "https://magazine.washington.edu/wp-content/uploads/2018/06/Narwhal375.jpg",
    "Emu": "https://cdn.pixabay.com/photo/2018/06/16/20/59/emu-3479510_1280.jpg",
    "Donkey": "https://cdn.pixabay.com/photo/2017/02/24/16/10/donkey-2095513_1280.jpg"
}

# Roasts
roast_texts = [
    "You look like a {} – but somehow the animal version has more dignity.",
    "If awkwardness had a mascot, it would be a {}… or you, really.",
    "Bro, are you a {}? ‘Cause that face could cause a global identity crisis.",
    "You're rocking that {} energy – clumsy, confused, and deeply roastable.",
    "NASA called. They found a new species: part-human, part {}. 100% roastable.",
    "Some say you resemble a {}, but that’s honestly an insult… to the {}.",
    "If mirrors could cry, yours would every time you channel that {} look.",
    "The only glow-up you got was into a full-fledged {} impersonator.",
    "You out-{}ed the {}, and that’s not something to be proud of.",
    "Your aura screams {}… mixed with expired mayo and zero confidence."
]

# Show roast logic
def roast_me():
    animal = random.choice(list(animals.keys()))
    roast = random.choice(roast_texts).format(animal, animal)

    st.markdown('<div class="you-look">You look like this 👇</div>', unsafe_allow_html=True)

    st.markdown(f'''
        <div style="display: flex; justify-content: center; align-items: center; gap: 40px; margin-top: 30px;">
            <div class="scanner" style="position: relative;">
                <img src="data:image/jpeg;base64,{uploaded_image}" width="300" style="border-radius: 20px; box-shadow: 0px 4px 25px rgba(0,0,0,0.25); display: block;">
            </div>
            <div>
                <img src="{animals[animal]}" width="300" style="border-radius: 20px; box-shadow: 0px 4px 25px rgba(0,0,0,0.25); display: block;">
            </div>
        </div>
    ''', unsafe_allow_html=True)

    st.markdown(f'<div class="roast-box">{roast}</div>', unsafe_allow_html=True)

# Encode uploaded image to base64 for inline HTML
import base64
from io import BytesIO

def get_base64_img(img):
    buf = BytesIO()
    img.save(buf, format="JPEG")
    byte_im = buf.getvalue()
    return base64.b64encode(byte_im).decode()

# Roast Button
st.markdown('<div class="button-style">', unsafe_allow_html=True)
if uploaded_file and st.button("🔥 Roast Me Hard! 🔥"):
    image = Image.open(uploaded_file)
    uploaded_image = get_base64_img(image)
    roast_me()
elif not uploaded_file:
    st.markdown('<div class="upload-instruction">❌ Upload a selfie first before I unleash the beast! 🐾</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)