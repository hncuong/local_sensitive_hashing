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

def choose_random_pseudo_perm_hasher(cool_prime, k):
    """
    cool_prime: a prime number slightly larger than the total number of shingle sets.
    Select here: http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php
    k: number of hasher to take
    """
    coefs = np.random.randint(0, cool_prime, size=(k, 2))
    return coefs

def md5_hashing(s):
    # Encode to bytes
    if type(s) == str:
        s = s.encode('utf-8')
        
    # Hashing using md5
    hashobj = hashlib.md5(s)
    hexv = hashobj.hexdigest()
    val = int(hexv, 16)
    
    return val

def random_hasher_integer(big_num):
    def hashing(n):
        n = str(n)
        val = md5_hashing(n)
        val = val % big_num
        return val
    return hashing

def gen_random_int_hasher(k):
    """k : number of hasher."""
    big_nums = np.random.randint(int(1e9), int(2e9), k)
    return [random_hasher_integer(big_num) for big_num in big_nums]
    