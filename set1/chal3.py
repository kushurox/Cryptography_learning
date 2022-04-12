s1 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
s1 = bytearray.fromhex(s1)

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
    assert len(buf1) == len(buf2)
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
            bests.append({"msg": new, "nb": c})
            nbs.append(c)


    analyse(bests, nbs)

crack_xor(s1)