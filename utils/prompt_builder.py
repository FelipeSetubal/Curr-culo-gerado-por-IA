def criar_prompt(vaga, curriculo):
    return f"""
Você é um especialista em recrutamento e otimização de currículos.

Adapte o currículo para a vaga abaixo.

REGRAS:
- Não inventar informações
- Usar palavras-chave da vaga
- Destacar SQL, Python e Power BI se relevante
- Ser direto e profissional
- Estruturar como currículo pronto

VAGA:
{vaga}

CURRÍCULO BASE:
{curriculo}
"""