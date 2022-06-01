def show_messages(shown_messages):
    for message in shown_messages:
        print(message)
def send_messages(messages,sent_messages):
    while messages:
        sent_message=messages.pop()
        print(sent_message)
        sent_messages.append(sent_message)
messages=['1','2','3']
sent_messages=[]
send_messages(messages[:],sent_messages)
print(messages)
print(sorted(sent_messages))