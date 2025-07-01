import os
from dotenv import load_dotenv
from google import genai
import sys

def main():

    if len(sys.argv) < 2:
        print("Error: No prompt provided.")
        print("Usage: python3 main.py \"your prompt goes gere\"")
        sys.exit(1)

    user_prompt = sys.argv[1]

    print(f"Recieved prompt: \"{user_prompt}\"")
          
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
    model='gemini-2.0-flash-001',
    contents=["Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."]
    )
    print(response.text)
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)

if __name__ == "__main__":
    main()
