s1 = "1c0111001f010100061a024b53535009181c"
s2 = "686974207468652062756c6c277320657965"

ans = "746865206b696420646f6e277420706c6179"

s1 = bytes(bytearray.fromhex(s1))
s2 = bytes(bytearray.fromhex(s2))


def xor(buf1, buf2):
    return bytes([x^y for (x, y) in zip(buf1, buf2)])


if __name__ == "__main__":
    print(xor(s1, s2) == bytearray.fromhex(ans))