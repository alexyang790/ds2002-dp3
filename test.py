messages = [{'1': 'who'}, {'6': 'about'}, {'9': 'PowerPoint.'}, {'4': "they're"}, {'8': 'need'}, {'7': "don't"}, {'0': 'People'}, {'2': 'know'}, {'3': 'what'}, {'5': 'talking'}]

# Sort the messages by the 'order' key
#sorted_messages = sorted(messages, key=lambda x: x.keys())
print(lambda x:)
sorted_messages = sorted(messages, key=lambda x: int(list(x.keys())[0]))

print(sorted_messages)

'''
# Print the reorganized messages
for message in sorted_messages:
    print(f"Order: {message['order']}, Word: {message['word']}")
'''