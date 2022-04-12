from itertools import cycle

def xor_rk(msg, key):
    key = cycle(key)
    return bytes([(ord(c) ^ ord(next(key))) for c in msg])