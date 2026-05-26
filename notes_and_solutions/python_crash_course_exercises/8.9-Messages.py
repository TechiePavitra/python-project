# Make a list containing a series of short text messages. 
# Pass the list to a function called show_messages(), which prints each text message.

messages = ["hello", "good morning", "how are you"]

def  show_messages(messages):
    """Show all messages"""
    for message in messages:
        print(message)

show_messages(messages)