def rotate(text, key):
    alphabeth = 'abcdefghijklmnopqrstuvwxyz'
    ciphered_text = ''

    for i in range( len(text)):
        if (text[i].isalpha()):
            current_char_possition = alphabeth.index(text[i].lower())
            ciphered_index = (current_char_possition+key) % 26
            if (text[i].isupper()):
                ciphered_text += alphabeth[ciphered_index].upper()
            else:
                ciphered_text += alphabeth[ciphered_index]
        else:
            ciphered_text += text[i]
            
    return ciphered_text

print (rotate("omg gives trl", 5))
# ROT0 c gives c
# ROT26 Cool gives Cool
# ROT13 The quick brown fox jumps over the lazy dog. gives Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
# ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. gives The quick brown fox jumps over the lazy dog.