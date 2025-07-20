from stats import count_words

with open("./books/franenstein.txt") as f:
    file_contents = f.read()

count_words(file_contents)
