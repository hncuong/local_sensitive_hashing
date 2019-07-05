import hashlib
import numpy as np

NBIT = 32
MAX_VAL = 2 ** 32

def hashing_md5_to_32bit(s):
    # Encode to bytes
    if type(s) == str:
        s = s.encode('utf-8')
        
    # Hashing using md5
    hashobj = hashlib.md5(s)
    hexv = hashobj.hexdigest()
    val = int(hexv, 16) % MAX_VAL
    
    return val
    
def preprocessing_doc(doc):
    return doc.lower()

"""Get random hasher as pseudo permutation.
- cool_prime: a prime number slightly larger than the total number of shingle sets. Refer to:
        - http://ethen8181.github.io/machine-learning/clustering_old/text_similarity/text_similarity.html
        - http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php
k: number of hasher to take
"""

def random_pseudo_perm_hasher(a, b, cool_prime):
    def hashing(n):
        val = (a * n + b) % cool_prime
        return val
    return hashing

def get_random_pseudo_perm_hasher(cool_prime, k):
    coefs = np.random.randint(1, cool_prime, size=(k, 2))
    hashers = []
    for a, b in coefs:
        hashers.append(random_pseudo_perm_hasher(a, b, cool_prime))
    return hashers


"""
Gen random hasher use md5 hash modulo a random number. Refer to:
    - https://towardsdatascience.com/understanding-locality-sensitive-hashing-49f6d1f6134
    - https://medium.com/engineering-brainly/locality-sensitive-hashing-explained-304eb39291e4
"""
def md5_hashing(s):
    # Encode to bytes
    if type(s) == str:
        s = s.encode('utf-8')
        
    # Hashing using md5
    hashobj = hashlib.md5(s)
    hexv = hashobj.hexdigest()
    val = int(hexv, 16)
    
    return val

def random_hasher_md5(big_num):
    def hashing(n):
        n = str(n)
        val = md5_hashing(n)
        val = val % big_num
        return val
    return hashing

def gen_random_hasher(k):
    """k : number of hasher."""
    big_nums = np.random.randint(int(1e9), int(2e9), k)
    return [random_hasher_md5(big_num) for big_num in big_nums]
    