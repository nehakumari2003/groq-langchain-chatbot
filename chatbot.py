import os
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API Key
groq_api_key = os.getenv("GROQ_API_KEY")

# Initialize ChatGroq with the model
chat = ChatGroq(
    api_key=groq_api_key,
    model="llama3-8b-8192",

)

# Start chat loop
print("🤖 Chatbot is ready! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! 👋")
        break

    response = chat.invoke([
        HumanMessage(content=user_input)
    ])

    print("Chatbot:", response.content)
