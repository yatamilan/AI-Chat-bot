import requests
import tkinter as tk
from tkinter import scrolledtext

# Hugging Face API details
API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
HEADERS = {"Authorization": "Bearer Enter_Your_API"}

def chatbot_response(user_input):
    response = requests.post(API_URL, headers=HEADERS, json={"inputs": user_input})
    response_data = response.json()

    if isinstance(response_data, list) and len(response_data) > 0 and "generated_text" in response_data[0]:
        return response_data[0]["generated_text"]
    else:
        return "Sorry, I didn't understand."

# Function to send a message
def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return  # Ignore empty messages
    
    chat_history.insert(tk.END, "You: " + user_input + "\n", "user")
    entry.delete(0, tk.END)  # Clear input field
    
    bot_response = chatbot_response(user_input)
    chat_history.insert(tk.END, "Bot: " + bot_response + "\n", "bot")
    chat_history.yview(tk.END)  # Scroll to the bottom

# Create main window
root = tk.Tk()
root.title("🌈 AI Chatbot")
root.geometry("500x600")
root.configure(bg="#A7C7E7")  # Light Blue Background

# Chat history area
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=25, font=("Arial", 12), bg="#E3F2FD", fg="black")
chat_history.pack(padx=10, pady=10)
chat_history.tag_config("user", foreground="#1E3A8A", font=("Arial", 12, "bold"))  # Dark Blue for User
chat_history.tag_config("bot", foreground="#1B5E20", font=("Arial", 12, "italic"))  # Green for Bot

# Input field and send button
entry = tk.Entry(root, width=50, font=("Arial", 12), bg="#FFF8E1", fg="black")  # Soft Yellow
entry.pack(padx=10, pady=5)

send_button = tk.Button(root, text="Send 🚀", font=("Arial", 12, "bold"), bg="#FF9800", fg="white", command=send_message)  # Orange Button
send_button.pack(pady=5)

# Run the chatbot GUI
root.mainloop()

