"""
Author:  Derek Bittner
Progrom:  assign_average.py

"""


def switch_average(entry):
    my_dict = {'A': 'You entered an A!',
               'B': 'You entered an B!',
               'C': 'You entered an C!',
               'D': 'You entered an D!',
               'E': 'You entered an E!'}

    result = my_dict.get(entry, "This is not a valid grade!")
    return result


if __name__ == '__main__':
    print(switch_average("A"))
