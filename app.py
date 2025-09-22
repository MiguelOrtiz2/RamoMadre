import streamlit as st
from PIL import Image
import os
import time

# --------------------------
# Configuración de la página
# --------------------------
st.set_page_config(
    page_title="Ramo Digital para Mamá",
    page_icon="💐",
    layout="centered"
)

# --------------------------
# Fondo bonito usando CSS
# --------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, #fff0f5, #ffe4e1); /* degradado rosa suave */
        color: #333333;
        font-family: 'Comic Sans MS', cursive;
    }
    .big-font {
        font-size:28px !important;
        color:#ff1493;
    }
    .medium-font {
        font-size:22px !important;
        color:#ff4500;
    }
    .stButton>button {
        background-color: #ff69b4;
        color: #ffffff;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------
# Mensajes iniciales
# --------------------------
st.markdown('<p class="big-font">💐 Mamá, quiero decirte algo especial…</p>', unsafe_allow_html=True)
time.sleep(2)
st.markdown('<p class="medium-font">Te amo mucho y te agradezco todo el apoyo que me das, llevándome a Metro Eugenia y estando siempre pendiente de mí.</p>', unsafe_allow_html=True)
time.sleep(3)
st.markdown('<p class="medium-font">Aunque no siempre sepas lo de la "chaviza", estas flores digitales son para mostrarte que quiero que nuestra relación y tu apoyo se queden conmigo para siempre, aunque parezca algo tonto.</p>', unsafe_allow_html=True)
time.sleep(3)
st.markdown('<p class="medium-font">Sé que a veces mi carrera se complica y mis estados de ánimo pueden variar, pero a pesar de todo, amo el apoyo incondicional que me das.</p>', unsafe_allow_html=True)
time.sleep(3)
st.markdown('<p class="medium-font">Gracias por todos los esfuerzos que haces por mí, sé que cuestan, aunque a veces me parezcan pocos, y te valoro muchísimo por ello.</p>', unsafe_allow_html=True)
time.sleep(3)
st.markdown('<p class="big-font">💐 Te amo mucho, mamá 💐</p>', unsafe_allow_html=True)
st.markdown("---")  # Línea separadora

# --------------------------
# Configuración de imágenes
# --------------------------
image_folder = os.path.join(os.getcwd(), "images")
image_files = ["foto1.jpg", "foto2.jpg", "foto3.jpg", "foto4.jpg", "foto5.jpg", "foto6.jpg"]

# Verifica si existen las imágenes
for img_file in image_files:
    img_path = os.path.join(image_folder, img_file)
    if not os.path.exists(img_path):
        st.warning(f"No se encontró la imagen: {img_file}")

# --------------------------
# Carrusel de imágenes
# --------------------------
st.markdown("### 🌸 Ramo Digital 🌸")

image_container = st.empty()

# Mostrar imágenes en loop
while True:
    for img_file in image_files:
        img_path = os.path.join(image_folder, img_file)
        if os.path.exists(img_path):
            img = Image.open(img_path)
            image_container.image(img, caption="💐 Momentos especiales 💐", use_column_width=True)
            time.sleep(1.5)
