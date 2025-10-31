import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image


st.title("Reconocimiento óptico de Caracteres")

import streamlit as st
import cv2
import numpy as np
import pytesseract

# 🌙 Configuración de tema oscuro y estilo visual
st.markdown("""
    <style>
    body {
        background-color: #0e1117;
        color: #fafafa;
    }
    .stRadio > label {
        color: #c9d1d9 !important;
        font-weight: 500;
    }
    .stCameraInput label, .stMarkdown, .stTextInput label {
        color: #e6edf3 !important;
    }
    .stButton button {
        background: linear-gradient(90deg, #7b61ff 0%, #9c27b0 100%);
        color: white;
        border-radius: 10px;
        border: none;
        transition: 0.3s;
    }
    .stButton button:hover {
        background: linear-gradient(90deg, #9c27b0 0%, #7b61ff 100%);
        transform: scale(1.03);
    }
    </style>
""", unsafe_allow_html=True)

st.title("📷 OCR con Cámara")
st.caption("Toma una foto, aplica un filtro y convierte el texto de la imagen en texto editable.")

# 🧠 Entrada de cámara
img_file_buffer = st.camera_input("📸 Toma una Foto")

# 🎨 Opciones de filtro
with st.sidebar:
    st.header("⚙️ Opciones de Procesamiento")
    filtro = st.radio("Aplicar Filtro", ('Con Filtro', 'Sin Filtro'))
    st.info("El filtro invierte los colores de la imagen para mejorar la detección de texto.")

# 🧩 Procesamiento de imagen
if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    
    # Aplicar filtro opcional
    if filtro == 'Con Filtro':
        cv2_img = cv2.bitwise_not(cv2_img)
        st.success("🎨 Filtro aplicado correctamente.")
    else:
        st.warning("📷 Imagen sin filtro.")
    
    # Conversión a RGB para mostrar correctamente
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    
    # Mostrar imagen procesada
    st.image(img_rgb, caption="🖼️ Imagen procesada", use_container_width=True)
    
    # Extraer texto
    with st.spinner("🔍 Extrayendo texto..."):
        text = pytesseract.image_to_string(img_rgb)
        st.balloons()
    
    # Mostrar texto resultante
    st.markdown("### 📝 Texto Detectado:")
    st.code(text if text.strip() != "" else "No se detectó texto.", language="markdown")


    


