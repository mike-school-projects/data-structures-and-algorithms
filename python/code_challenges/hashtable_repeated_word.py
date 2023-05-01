from data_structures.hashtable import Hashtable
import re

def first_repeated_word(phrase):
    word_list = phrase.split()
    hashtable = Hashtable()

    if len(word_list) <= 1:
        return None

    for index, word in enumerate(word_list):
        # clean word list to lower case, without ending punctuation
        word_list[index] = re.sub(r'[^\w\s]+$','', word).strip()
        word_list[index] = word_list[index].lower()

        # Check to see if it's in hashtable
        # if hashtable.has(word_list[index]):
        if word_list[index] in hashtable.keys():
            return word_list[index]

        else:
            hashtable.set(word_list[index], word_list[index])

    # No match
    return None

if __name__ == "__main__":
    phrase = "banana !ap!ple! APPLE banana"
    print(first_repeated_word(phrase))
