import openai

openai.api_key = "your_openai_api_key"

def chatbot_response(user_input):
    """Chatbot for sustainability guidance."""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You're an assistant on sustainability."},
                  {"role": "user", "content": user_input}]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    user_input = input("Ask about sustainability: ")
    print(chatbot_response(user_input))
