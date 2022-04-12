from base64 import b64encode
from operator import xor
s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
def h2b(s: str):
    return b64encode(bytearray.fromhex(s)).decode()

def xor_two(buf1, buf2):
   return xor(buf1, buf2)


t = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
assert h2b(s) == t