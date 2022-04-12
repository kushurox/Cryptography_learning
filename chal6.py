from base64 import b64decode
from typing import List, Union

import numpy

from chal4 import crack_xor
from chal5 import xor_rk


def hamming_distance(str1: bytes, str2: bytes) -> int:
    """
  Number of bit substitution needed to make two same strings same
  i.e number of differing bits
  measure of how different two strings are
  """
    str1 = int.from_bytes(str1, 'big')
    str2 = int.from_bytes(str2, 'big')
    res = str1 ^ str2
    return bin(res).count("1")


def analyse(bests, nbs):
    highest = max(nbs)
    most_readable = [x for x in bests if x['nb'] == highest]
    return most_readable


def split_chunks(iterable: Union[bytearray, list, bytes], cs: int) -> List[Union[int, bytearray]]:
    """Splits Chunks based on chunk_size"""
    max_chunks = len(iterable) // cs
    chunks = [iterable[(i - 1) * cs: cs * i] for i in range(1, max_chunks + 1)]
    return chunks


def get_normalized(ct: Union[bytes, list, bytearray], cs: int):
    """
  splits the chunks and stores the first two chunks in blocks, altho we use only 1 since our text is large enough.
  checks the similarity of the first block with the chunks of the whole cipher. lesser the edit distance, more similar
  more similar = favourable key size
  """
    chunks = split_chunks(ct, cs)
    blocks = [ct[0: cs], ct[cs: cs * 2]]
    hamming_distances = [[hamming_distance(block, chunk) for chunk in chunks] for block in blocks]
    h1 = hamming_distances[0]
    mean = sum(h1) / len(h1)
    return mean / cs


def transpose(mat: iter, cs: int) -> iter:
    """
  we transpose the matrix in order to single crack xor with respective cycles. refer repeating key xor encryption
  """
    chunks = split_chunks(mat, cs)
    return numpy.transpose(chunks)


if __name__ == "__main__":
    assert hamming_distance(b"this is a test", b"wokka wokka!!!") == 37, "Incorrect hamming distance"
    with open("6.txt", "r") as fp:
        ct = fp.read()
        str_msg = b64decode(ct).decode()
        ct = list(b64decode(ct))
    k2d = {
        key: get_normalized(ct, key) for key in range(2, 41)
    }

    least = min(k2d, key=lambda k: k2d[k])
    transposed = transpose(ct, least)
    key = "".join([analyse(*crack_xor(row))[0]['key'] for row in transposed])
    print(xor_rk(str_msg, key).decode())
