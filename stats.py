def count_words(file_contents): 
    word_count = file_contents.split(" ")
    print("%s words found in Frankenstein" % len(word_count))

def count_chars(file_contents):
    char_counts = {}
    for char in file_contents:
        if (char.lower() not in char_counts):
            char_counts.update({char.lower(): 1})
        else:
            char_counts.update({char.lower(): char_counts.get(char.lower()) + 1})
    print(char_counts)


