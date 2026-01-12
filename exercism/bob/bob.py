import re

def response(hey_bob):
    hey_bob = hey_bob.rstrip()

    if ((hey_bob == hey_bob.upper()) and (hey_bob.endswith('?')) and (re.search('[a-zA-Z]', hey_bob))): #YELLING a question
       return "Calm down, I know what I'm doing!"
    elif (hey_bob.endswith('?')):                   #question ? at the end
       return "Sure."
    elif ( ((hey_bob == "") or (('  ' in hey_bob) or ('\t' in hey_bob)) and (hey_bob == hey_bob.upper()))):    #silance or whitespaces
       return "Fine. Be that way!"
    elif ((hey_bob == hey_bob.upper()) and (re.search('[a-zA-Z]', hey_bob))):              #YELLING uppercase
       return "Whoa, chill out!"
    else:
        return "Whatever."

