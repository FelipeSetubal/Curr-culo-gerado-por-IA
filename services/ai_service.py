from openai import OpenAI
from utils import prompt_builder   # ✅ AQUI

def gerar_curriculo(api_key, vaga, curriculo):
    client = OpenAI(api_key=api_key)

    prompt = prompt_builder.criar_prompt(vaga, curriculo)  # ✅ aqui também

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content