from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL_NAME = "openai/gpt-oss-120b"

MODEL_CONFIG = {
    "technical": {
        "system_prompt":
        """You are a Technical Support Expert.
        Be precise, logical and code-focused.
        Help debug errors, fix bugs and explain technical issues clearly."""
    },
    "billing": {
        "system_prompt":
        """You are a Billing Support Expert.
        Be empathetic and professional.
        Help with refunds, payments, subscriptions and company policy."""
    },
    "general": {
        "system_prompt":
        """You are a friendly Customer Support Agent.
        Handle general queries and casual conversation politely."""
    }
}


def route_prompt(user_input):

    routing_prompt = f"""
Classify the following customer query into ONE of these categories:
technical
billing
general

Return ONLY the category name.

Query: {user_input}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0,
        messages=[
            {"role": "system", "content": "You are an intent classifier."},
            {"role": "user", "content": routing_prompt}
        ]
    )

    category = response.choices[0].message.content.strip().lower()
    return category


def get_bitcoin_price():
    # Mock Tool Function
    return "Current Bitcoin price is $52,340 (mock data)."


def process_request(user_input):

    category = route_prompt(user_input)

    print(f"\n🧠 Routed to: {category} Expert")

    # TOOL USE CASE
    if "bitcoin" in user_input.lower() or "btc" in user_input.lower():
        return get_bitcoin_price()

    system_prompt = MODEL_CONFIG.get(category,
                                     MODEL_CONFIG["general"])["system_prompt"]

    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0.7,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content


if __name__ == "__main__":

    while True:
        query = input("\nAsk Customer Support: ")

        if query.lower() == "exit":
            break

        answer = process_request(query)
        print("\n💬 Response:\n", answer)
