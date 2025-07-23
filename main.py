from stats import count_words
from stats import count_chars

with open("./books/frankenstein.txt") as f:
    file_contents = f.read()

count_words(file_contents)
count_chars(file_contents)
