"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """
    # formatted_title = ''

    # title_list = title.split()
    # for word in title_list:
    #     formatted_title += word.capitalize() + ' '

    # return formatted_title[:-1]
    return title.title()

def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    :param sentence: str - a sentence to check.
    :return: bool - return True if punctuated correctly with period, False otherwise.
    """
        # if (sentence[-1] == '.'):
        #     return True
        # else:
        #     return False
    return sentence.endswith('.')

def clean_up_spacing(sentence):
    """Verify that there isn't any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """
    return sentence.strip()



def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """
    # new_sentence = ''
    # sentence_list = sentence.split()
    # print (sentence_list)
    # for word in sentence_list:
    #     if (word[-1].isalpha()): # no extra signs
    #         if (word == old_word):
    #             print (word, old_word)
    #             new_sentence += new_word + ' '
    #         else:
    #             print ('else: ' + word, old_word)
    #             new_sentence += word + ' '
    #     else: #there is a sign at the end of the word
    #         if (word[:-1] == old_word):
    #             print (word, old_word)
    #             new_sentence += new_word + word[-1]+ ' '
    #         else:
    #             print ('else: ' + word, old_word)
    #             new_sentence += word + ' '
    # print (new_sentence)
    # return new_sentence[:-1]
    return sentence.replace(old_word, new_word)

print (replace_word_choice("I bake good cakes.", "good", "amazing"))