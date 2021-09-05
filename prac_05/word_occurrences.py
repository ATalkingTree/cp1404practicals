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
sorted(collection_of_words)
for key, value in collection_of_words.items():
    print(f"{key} : {value}")
