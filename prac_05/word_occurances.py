"""
CP1404 Practical
Word Occurrences
Estimate: 20 mins
Actual: 20.5 mins
"""

word_to_count = {}
text = input("Enter text: ")
words = text.split()
# print(words)
for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

words = list(word_to_count.keys())
words.sort()
# print(words)
max_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
