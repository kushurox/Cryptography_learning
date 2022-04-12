def analyse(bests, nbs):
    _ = set(nbs)
    median = sum(_)/len(_)
    above_median = [x for x in bests if x['nb'] > median]
    highest = max(nbs)
    most_readable = [x for x in bests if x['nb'] >= highest]
    
    print("Candidate messages:", len(bests))
    print("Median of readable letters:", median)
    print("above median messages:", len(above_median))
    print("most readable:", most_readable)


def xor(buf1, buf2):
    return bytes([x^y for (x, y) in zip(buf1, buf2)])


def crack_xor(s):
    ascii_text_chars = list(range(97, 122)) + [32]
    bests = []
    nbs = []
    for i in range(2**8):
        ks = i.to_bytes(1, 'big') * len(s)
        new = xor(ks, s)
        c = 0
        for j in new:
            if j in ascii_text_chars:
                c+=1
        if c != 0:
            bests.append({"msg": new, "nb": c, "key": chr(i)})
            nbs.append(c)
    
    return bests, nbs


if __name__ == "__main__":
    with open("4.txt", "r") as fp:
        file = fp.read().split("\n")



    eve = []
    nbs = []
    for enc in file:
        s1 = bytearray.fromhex(enc)
        bests, nb = crack_xor(s1)
        eve.extend(bests)
        nbs.extend(nb)

    # analyse(eve, nbs)