from docx2pdf import convert

def gerar_pdf(caminho_docx, caminho_pdf):
    convert(caminho_docx, caminho_pdf)