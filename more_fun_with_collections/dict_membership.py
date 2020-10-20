"""
Author:  Derek Bittner
Program:  dict_membership.py

"""


def in_dict(some_dict, some_value):
    return some_value in some_dict


if __name__ == '__main__':
    my_dict = dict({'A': 3, 'B': 4, 'C': 5, 'D': 6, 'E': 7})
    print(my_dict)
    print('Is {} in {}?  {}'.format(5, my_dict, in_dict(my_dict, str(5))))

