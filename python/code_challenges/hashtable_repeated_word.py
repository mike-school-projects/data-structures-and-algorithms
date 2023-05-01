from data_structures.hashtable import Hashtable
import re

def first_repeated_word(phrase):
    # variables
    word_list = phrase.split()
    hashtable = Hashtable()

    # check empty or 1 word phrase
    if len(word_list) <= 1:
        return None

    for index, word in enumerate(word_list):
        word_list[index] = clean(word)

        # Check to see if it's in hashtable
        if word_list[index] in hashtable.keys():
            return word_list[index]

        else:
            # Add to hashtable
            hashtable.set(word_list[index], word_list[index])

    # No match
    return None

def clean(input_word):
    # clean word list to lower case, without ending punctuation
    output_word = re.sub(r'[^\w\s]+$','', input_word).strip()
    output_word = output_word.lower()
    return output_word

if __name__ == "__main__":
    phrase = "banana !ap!ple! APPLE banana"
    print(first_repeated_word(phrase))
