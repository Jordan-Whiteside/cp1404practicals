"""
Word Occurrences
Estimate:  1 hour
Actual: 41 minutes
"""
from operator import itemgetter

full_text = input("Text: ").lower().strip()
word_to_count = {}
words = full_text.split()
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

max_length = max([len(key) for key in word_to_count.keys()])
for word, count in sorted(word_to_count.items()):
    print(f"{word:{max_length}} : {count}")
