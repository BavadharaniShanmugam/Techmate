print("Welcome to TechMate - Your AI IT Support Assistant!")

while True:
    query = input("You: ").lower()

    if "hello" in query or "hi" in query:
        print("TechMate: Hello! How can I assist you?")
    elif "network" in query:
        print("TechMate: Please check your router or contact your ISP.")
    elif "system slow" in query:
        print("TechMate: Try restarting your system and clearing background tasks.")
    elif "bye" in query or "exit" in query:
        print("TechMate: Goodbye! Have a great day.")
        break
    else:
        print("TechMate: Sorry, I need more training to understand that.")

