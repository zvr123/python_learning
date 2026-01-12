def answer(question):

    question = question.strip('?')
    
    if not question.startswith("What is"):
        raise ValueError("Non-math question")
    
    words = question.split()
    print (len(words), words)
    result = 0
    if len(words) < 3:
        raise ValueError("syntax error")
    else:
        try:
            result = int(words[2])
        except:
            raise ValueError("syntax error")

    i=3
    while i < len(words):
        match words[i]:
            case 'plus':
                try:
                    result += int(words[i+1])
                    i +=2
                except:
                    raise ValueError (f'syntax error')
            case 'minus':
                try:
                    result -= int(words[i+1])
                    i +=2
                except:
                    raise ValueError (f'syntax error')
            case 'multiplied':
                try:
                    result *= int(words[i+2])
                    i +=3
                except:
                    raise ValueError (f'syntax error')
            case 'divided':
                try:
                    result /= int(words[i+2])
                    i +=3
                except:
                    raise ValueError (f'syntax error')
            case _:
                if words[i].isdigit():
                    raise ValueError (f'syntax error')
                else:
                    raise ValueError (f'unknown operation')

    return result

    # except (ValueError, IndexError):
    #     raise ValueError("Invalid question")

# print (answer('What is 5?'))
# print (answer('What is 5 plus 5?'))
# print (answer('What is 5 minus 5?'))
# print (answer('What is 5 multiplied by 5?'))
# print (answer('What is 5 divided by 5?'))
# print (answer('What is 5 plus 13 plus 6?'))
# print (answer('What is 3 plus 2 multiplied by 3?'))
# print (answer('What is 52 cubed?'))
# print (answer('Who is the President of the United States'))
# print (answer('What is 1 plus plus 2?'))
