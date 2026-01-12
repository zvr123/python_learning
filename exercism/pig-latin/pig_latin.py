def translate(text):
    pig_sentence = ''

    words = text.split()
    count_words = len(words)

    for word in words:
        count_words -= 1
        pig_text = check_rules(word)
        pig_sentence += pig_text
        if (count_words > 0):
            pig_sentence += ' '
        else:
            return pig_sentence


def check_rules(text):
    if (check_vowels(text)):
        return (ad_ay_2_end(text))
    else:
        index = check_consonants(text)
        pig_text = move_cons_2_end(text, index)
        return (ad_ay_2_end(pig_text))

#Rule1
def check_vowels(text):
    two_chars = text[0] + text[1]
    if (text[0] in vowels) or (two_chars in add2vowels):
        return True
    else:
        return False
    
#Rule2    
def check_consonants(text):
    # isVowel = False
    # while (not isVowel):   
    for index in range(len(text)):
        if (text[index] in vowels):  #rule2 - return the index of the 1st vowel in the string
            if ((text[index-1] == 'q') and (text[index] == 'u')): # rule3 - 'qu' is rule3 and is a special case 
                return index+1 
            else:
                return index  # vowel and not qu
        elif ((text[index] == 'y') and (index > 0)): # y is treated as vowel if it's not the 1st char
            print (index)
            return index

def move_cons_2_end(text, index):       
    pigs_text_tmp = ''
    for i in range(len(text)-index):    # coppies from the 1st vowel to the new string
        pigs_text_tmp += text[index+i]
    for i in range(index):           # coppies the start consonants to the end of the new string
        pigs_text_tmp += text[i]
    return pigs_text_tmp
    
# Add ay to all of the rules
def ad_ay_2_end(text):
    text += 'ay'
    return text
    

# Main
text = 'quick  fast'
vowels = ['a', 'i', 'o', 'u', 'e']
add2vowels = ['xr', 'yt']

print (translate (text))

