with open("secret.jpg", "rb") as fp:
    content = fp.read()



key = None # I wont reveal key
enc = (key).to_bytes(1, 'big') * len(content)
a = bytearray()
for v, k in zip(content, enc):
    a.append(v^k)

with open("secret.encrypted", "wb") as fp:
    fp.write(a)

