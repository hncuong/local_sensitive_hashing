import numpy as np
from utils import choose_random_pseudo_perm_hasher, gen_random_int_hasher
from corpus import Corpus

MAX_INT = 2**31 - 1

class MinHasher(object):
    """Min hashing list of sets"""

    def __init__(self, corpus, k=100):
        """
        - k: # "permute" hash functions. Default 100.
        - corpus: documents as Corpus object.
        - cool_prime: a prime that is litter bigger than number of unique shingles.
        http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php
        """
        self._k = k

        self._ndocs = corpus.get_num_docs()
        self.idx_docs = corpus.get_idx_docs()
        self._hashers = self.get_hasher()
    
    def get_hashers(self):
        print("Generate {} random bucker hashers".format(self._k))
        return gen_random_int_hasher(self._k)

    def pseudo_perm_hasher(self):
        """Pseudo permutation hashing. MIN HASHING
        Return: k * ndocs matrix. Each value in range [0, cool_prime - 1]
        """
        # Do k hashing 
        # signatures = np.full((self._k, self._ndocs), MAX_INT, dtype=np.int32)
        signatures = [[MAX_INT] * self._k for _ in range(self._ndocs)]

        # For each row
        for r in range(len(self.idx_docs)):

            # DO perm hash functions for this row
            hrs = []
            for i in range(self._k):
                hasher = self._hashers(i)
                hrs.append(hasher(r))
            
            # For doc contain token id r
            for doc_id in self.idx_docs[r]:
                for hidx, hr in enumerate(hrs):
                    if hr < signatures[hidx][doc_id]:
                        signatures[hidx][doc_id] = hr

        return signatures

if __name__ == "__main__":
    pass


            
        