def up_first(msg):
    """Делает первую букву строки заглавной."""
    if msg:
        return msg[0].upper() + msg[1:]
    else:
        return msg


def reverse_string(string):
    return string[::-1]
