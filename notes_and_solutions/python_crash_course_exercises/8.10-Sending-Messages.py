# Start with a copy of your program from Exercise 8-9.
# Write a function called send_messages() that prints each text message
# and moves each message to a new list called sent_messages as it’s printed.
# After calling the function, print both of your lists to make sure the messages were moved correctly.

messages = ["hello", "good morning", "how are you"]
sent_messages = []

def send_messages(messages):
    """Send Messages"""
    while messages:
        current_message = messages.pop()
        sent_messages.append(current_message)

send_messages(messages)

def  show_messages(sent_messages):
    """Show all messages"""
    for sent_message in sent_messages:
        print(sent_message)

show_messages(sent_messages)

print("\nCurrent List elements:  ")
print(f"messages: {messages}")
print(f"sent_messages: {sent_messages}")