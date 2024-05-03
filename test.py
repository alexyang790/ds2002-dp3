messages = [
    {"order":3, "word":"fox"},
    {"order":0, "word":"the"},
    {"order":2, "word":"brown"},
    {"order":1, "word":"quick"},
]

# Sort the messages by the 'order' key
sorted_messages = sorted(messages, key=lambda x: x["order"])

# Extract the words in the correct order
ordered_words = [message["word"] for message in sorted_messages]

# Combine the words into a phrase
phrase = " ".join(ordered_words)

# Print the phrase
print(phrase)

print(sorted_messages)

phrase = ''
for i in range(4):
    print(i)
    phrase = phrase + (sorted_messages[i]['word']) + ' '
    print(phrase)

for i in range(4):
    print(i)