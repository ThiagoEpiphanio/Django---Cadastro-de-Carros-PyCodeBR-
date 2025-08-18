import os
from openai import OpenAI

def get_car_ai_bio(model, brand, year):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = f"""
    Me mostre uma descrição de venda para o carro {brand} {model} {year} em apenas 250 caracteres.
    Fale coisas específicas desse modelo de carro.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # pode trocar por "gpt-4o" ou quando disponível "gpt-5"
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=250,
    )

    return response.choices[0].message.content.strip()