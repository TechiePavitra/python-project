# Start with your work from Exercise 8-10. 
# Call the function send_messages() with a copy of the list of messages. 
# After calling the function, print both of your lists to show that the original list has retained its messages.

messages = ["hello", "good morning", "how are you"]
sent_messages = []

def send_messages(messages):
    """Send Messages"""
    while messages:
        current_message = messages.pop()
        sent_messages.append(current_message)

send_messages(messages[:])

def  show_messages(sent_messages):
    """Show all messages"""
    for sent_message in sent_messages:
        print(sent_message)

show_messages(sent_messages)

print("\nCurrent List elements:  ")
print(f"messages: {messages}")
print(f"sent_messages: {sent_messages}")