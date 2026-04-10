import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

import streamlit as st

from services.ai_service import gerar_curriculo
from services.doc_generator import gerar_docx
from services.pdf_generator import gerar_pdf

# config da página
st.set_page_config(page_title="Gerador de Currículo", layout="centered")

st.title("Gerador de Currículo com IA")

st.write("Cole a vaga e seu currículo base para gerar um currículo otimizado.")

# API KEY
api_key = st.text_input("API Key", type="password")

# Inputs
vaga = st.text_area("Descrição da vaga", height=200)
curriculo = st.text_area("Currículo base", height=300)

nome = st.text_input("Nome do arquivo", value="curriculo")

# botão
if st.button("Gerar Currículo"):

    if not api_key or not vaga or not curriculo:
        st.warning("Preencha todos os campos!")
    else:
        try:
            with st.spinner("Gerando com IA..."):

                texto = gerar_curriculo(api_key, vaga, curriculo)

                # 📂 cria pasta outputs se não existir
                os.makedirs("outputs", exist_ok=True)

                caminho_docx = f"outputs/{nome}.docx"
                caminho_pdf = f"outputs/{nome}.pdf"

                gerar_docx(texto, caminho_docx)
                gerar_pdf(caminho_docx, caminho_pdf)

            st.success("Currículo gerado com sucesso!")

            # download PDF
            with open(caminho_pdf, "rb") as f:
                st.download_button(
                    "Baixar PDF",
                    f,
                    file_name=f"{nome}.pdf"
                )

            # download DOCX
            with open(caminho_docx, "rb") as f:
                st.download_button(
                    "Baixar DOCX",
                    f,
                    file_name=f"{nome}.docx"
                )

        except Exception as e:
            st.error(f"Erro: {e}")