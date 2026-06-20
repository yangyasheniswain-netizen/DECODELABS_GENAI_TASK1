import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("models/gemini-3.5-flash")

chat = model.start_chat(history=[])

print("AI Chatbot Started!")
print("Type 'exit' to quit")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot Closed!")
        break

    try:
        response = chat.send_message(user_input)
        print("Bot:", response.text)

    except Exception as e:
        print("Error:", e)