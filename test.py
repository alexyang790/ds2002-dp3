messages = [
    {"order":3, "word":"fox"},
    {"order":0, "word":"the"},
    {"order":2, "word":"brown"},
    {"order":1, "word":"quick"},
]

# Sort the messages by the 'order' key
sorted_messages = sorted(messages, key=lambda x: x["order"])
print(sorted_messages)

'''
# Print the reorganized messages
for message in sorted_messages:
    print(f"Order: {message['order']}, Word: {message['word']}")
'''