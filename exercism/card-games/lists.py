"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    number_list = [number, number+1, number+2]
    return number_list


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    #return rounds_1+rounds_2
    rounds_1.extend(rounds_2)
    return rounds_1


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    # if (rounds.count(number) > 0):
    #     return True
    # else:
    #     return False
    return number in rounds 

def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    total_sum = 0
    number_of_elements = len(hand)
    for i in hand:
        total_sum += i

    return (total_sum/number_of_elements)
        


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    real_average = card_average(hand)
    first_last_average = (hand[0] + hand[-1]) /2
    median_average = hand[int(len(hand)/2)]

    if (real_average == first_last_average or real_average == median_average):
        return True
    else:
        return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    # average_even = 0
    # average_odd = 0
    # iter = 0
    # for i in range(0, len(hand), 2):
    #     average_even += hand[i]
    #     iter+=1
    # average_even = average_even/iter

    # iter = 0
    # for i in range(1, len(hand), 2):
    #     average_odd += hand[i]
    #     iter+=1
    # average_odd = average_odd/iter

    # if (average_even == average_odd):
    #     return True
    # else:
    #     return False
    return card_average(hand[::2]) == card_average(hand[1::2])
    
def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if (hand[-1] == 11):
        hand[-1] = 22
    return hand

hand = [5, 9, 11]
print (maybe_double_last(hand))