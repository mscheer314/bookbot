from string import Template

def count_words(file_contents): 
    return len(file_contents.split(" "))

def count_chars(file_contents):
    char_counts = {}
    for char in file_contents:
        if (char.lower() not in char_counts):
            char_counts.update({char.lower(): 1})
        else:
            char_counts.update({char.lower(): char_counts.get(char.lower()) + 1})
    return char_counts

def get_list(dict):
    return sorted([{"char": key, "num": value} for key, value in dict.items()], key=lambda x: x['num'], reverse=True)

def formatCharString(charList):
    result = ""
    template = Template("$key: $value\n")
    for charContent in charList:
        result += template.substitute(key=charContent["char"], value=charContent["num"])
    return result

def report(file_path):

    with open(file_path) as f:
        file_contents = f.read()

    report_header = Template("========== BOOKBOT ==========\nAnalyzing book found at $file")
    word_count_section = Template("---------- Word Count ----------\nFound $count total words.")
    char_count_section = Template("---------- Character Count ----------\n$chars")

    charData = get_list(count_chars(file_contents))

    print(report_header.substitute(file=file_path))
    print(word_count_section.substitute(count=count_words(file_contents)))
    print(char_count_section.substitute(chars=formatCharString(charData)))
