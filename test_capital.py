import os 
from dotenv import load_dotenv
from openai import OpenAI 

load_dotenv()
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])



def ask(question: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        max_tokens=100,
        messages=[{"role": "user", "content": question}],
    )
    return response.choices[0].message.content.strip()


def test_capital_of_france():
    answer = ask("What is the capital of France?")
    print(f"\nModel said: {answer!r}")
    assert answer == "Paris"
