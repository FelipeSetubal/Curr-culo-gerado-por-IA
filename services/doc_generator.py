from docx import Document

def gerar_docx(texto, caminho_arquivo):
    doc = Document()

    for linha in texto.split("\n"):
        doc.add_paragraph(linha)

    doc.save(caminho_arquivo)