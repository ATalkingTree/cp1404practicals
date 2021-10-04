"""
CP1404/CP5632 Practical
Count word occurrences from a string
"""

collection_of_words = {}

sentence = input("Text: ")
words = sentence.split()
for word in words:
    if word in collection_of_words:
        collection_of_words[word] += 1
    else:
        collection_of_words[word] = 1
words = list(collection_of_words.keys())
words.sort()
max_length = 0
for word in words:
    if len(word) > max_length:
        max_length = len(word)
for word in words:
    print(f"{word:{max_length}} : {collection_of_words[word]}")
