"""
CP1404/CP5632 Prac
Counts the amount of times a word appears in a string
"""

counted_word = {}
text = input("Text: ")
words = text.split()

for word in words:
    frequency = counted_word.get(word, 0)
    counted_word[word] = frequency + 1

