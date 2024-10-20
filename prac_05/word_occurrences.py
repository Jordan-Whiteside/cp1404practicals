"""
Word Occurrences
Estimate:  1 hour
Actual:
"""
from operator import itemgetter

full_text = input("Text: ").strip()
word_to_count = {}
words = full_text.split()
for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

for word, count in sorted(word_to_count.items(), key=itemgetter(0)):
    print(f"{word} : {count}")
