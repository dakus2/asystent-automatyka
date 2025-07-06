import streamlit as st
import json
from PIL import Image
import pytesseract

with open('sensors.json') as f:
    sensors = json.load(f)

st.title("Asystent Automatyka – Produal + Helukabel")
st.write("Wybierz czujnik i załaduj zdjęcie lub PDF.")

chosen = st.selectbox("Wybierz czujnik:", [s['model'] for s in sensors])
sensor = next(s for s in sensors if s['model'] == chosen)

file = st.file_uploader("Dodaj zdjęcie/plik (jpg/png/pdf):", type=['jpg','jpeg','png','pdf'])
if file:
    img = Image.open(file)
    st.image(img, use_column_width=True)
    text = pytesseract.image_to_string(img)
    st.write("🔍 OCR odczytał:")
    st.text(text)

    st.write("### ✅ Propozycja podłączenia")
    st.write(f"- **Przewód:** {sensor['recommended_cable']}")
    st.write("- **Kolory i funkcje:**")
    for func, color in sensor['color_code'].items():
        st.write(f"  • {func}: **{color}**")
    st.write(f"- **Liczba żył:** {sensor['wires_required']}")
