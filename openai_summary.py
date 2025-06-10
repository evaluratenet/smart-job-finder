import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_company_summary(company_name):
    try:
        prompt = f"""
        Provide a two-paragraph overview of the company {company_name}. 
        Include what the company does, where it's based, and any relevant industry focus.
        """
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"Could not retrieve summary for {company_name}."