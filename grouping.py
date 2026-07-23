from collections import defaultdict

words = ["apple", "banana", "avocado", "blueberry", "cherry"]

grouped_words = defaultdict(list)

for word in words:
    first_letter = word[0]
    grouped_words[first_letter].append(word)

print(dict(grouped_words))
