def up_first(msg):
    """Делает первую букву строки заглавной."""
    if msg:
        return msg[0].upper() + msg[1:]
    else:
        return msg


def reverse_string(string):
    return string[::-1]


def el_type_count(random_list, counting_type):
    counter = 0
    if type(random_list) is list:
        for i in random_list:
            if type(i) == counting_type:
                counter += 1
    return counter
