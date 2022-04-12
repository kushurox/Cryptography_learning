import Crypto.Util.number as n
from sympy.ntheory import factorint
from gmpy2.gmpy2 import mpz


p, q = n.getPrime(128), n.getPrime(128)
N = p*q

phi = (p-1)*(q-1)

e = 6553
d = n.inverse(e, phi)


def RSA_Encrypt(msg: str):
    msg = int.from_bytes(msg.encode(), 'big')
    return pow(msg, e, N)

def RSA_Decrypt(ct):
    decry = pow(ct, d, N)
    decry = decry.to_bytes(1024, 'big').decode()
    return decry

def show_metrics():
    print(f"N: {N}\ne: {e}\n")
    


def main():
    message = input("Enter message to encrypt: ")
    encrypted = RSA_Encrypt(message)
    decrypted = RSA_Decrypt(encrypted)
    print(f"original message: {message}\nencrypted message: {hex(encrypted)[2:]}\ndecrypted message: {decrypted}")
    show_metrics()

def main2():
    target = "mihir"
    t = [ord(c) for c in target]
    tm = bytes(t)
    print(hex(int.from_bytes(tm, 'big')))

main2()