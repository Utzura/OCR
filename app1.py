import streamlit as st
import cv2
import numpy as np
import pytesseract

# 🌙 Tema oscuro elegante (forzado)
st.markdown("""
    <style>
    /* Fondo principal y texto */
    .main {
        background-color: #0d1117 !important;
        color: #e6edf3 !important;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #161b22 !important;
        border-right: 1px solid #30363d;
    }
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] h3, 
    section[data-testid="stSidebar"] label {
        color: #c9d1d9 !important;
    }

    /* Radio buttons */
    div[data-testid="stRadio"] label {
        color: #e6edf3 !important;
        font-weight: 500;
    }

    /* Títulos */
    h1, h2, h3 {
        color: #58a6ff !important;
    }

    /* Botones */
    .stButton>button {
        background: linear-gradient(90deg, #7b61ff 0%, #9c27b0 100%);
        color: white;
        border-radius: 10px;
        border: none;
        font-weight: 600;
        padding: 0.6em 1.2em;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #9c27b0 0%, #7b61ff 100%);
        transform: scale(1.04);
    }

    /* Código (texto OCR) */
    code {
        background-color: #161b22 !important;
        color: #c9d1d9 !important;
        border-radius: 6px;
        padding: 10px;
        display: block;
    }
    </style>
""", unsafe_allow_html=True)

# 🧠 Título
st.title("📷 OCR con Cámara")
st.caption("Toma una foto, aplica un filtro y extrae texto de la imagen fácilmente.Espero que vaya bien la foto :3")

# 📸 Captura con cámara
img_file_buffer = st.camera_input("Toma una Foto...")

# ⚙️ Sidebar con opciones
with st.sidebar:
    st.header("⚙️ Opciones de Procesamiento")
    filtro = st.radio("Aplicar Filtro", ('Con Filtro', 'Sin Filtro'))
    st.info("El filtro invierte los colores de la imagen para mejorar la detección de texto.")

# 🧩 Procesamiento de imagen
if img_file_buffer is not None:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    
    # Filtro visual
    if filtro == 'Con Filtro':
        cv2_img = cv2.bitwise_not(cv2_img)
        st.success("🎨 Filtro aplicado correctamente.")
    else:
        st.warning("📷 Imagen sin filtro.")
    
    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    st.image(img_rgb, caption="🖼️ Imagen procesada", use_container_width=True)
    
    with st.spinner("🔍 Analizando texto..."):
        text = pytesseract.image_to_string(img_rgb)
        st.balloons()

    st.markdown("### 📝 Texto Detectado:")
    st.code(text if text.strip() else "⚠️ No se detectó texto.", language="markdown")



