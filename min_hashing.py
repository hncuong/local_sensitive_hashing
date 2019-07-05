import numpy as np
from utils import choose_random_pseudo_perm_hasher, gen_random_hasher
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
        self.token_to_docs = corpus.get_token_docs()
        self._hashers = self.get_hasher()
    
    def get_hashers(self):
        print("Generate {} random bucker hashers".format(self._k))
        return gen_random_hasher(self._k)

    def pseudo_perm_hasher(self):
        """Pseudo permutation hashing. MIN HASHING
        Return: ndocs * k matrix. Each value in range [0, cool_prime - 1]
        """
        # Do k hashing 
        # signatures = np.full((self._k, self._ndocs), MAX_INT, dtype=np.int32)
        signatures = [[MAX_INT] * self._k for _ in range(self._ndocs)] # n_docs * k

        # For each row
        for token, docs_id in self.token_to_docs.items():

            # DO perm hash functions for this row
            hrs = []
            for i in range(self._k):
                hasher = self._hashers(i)
                hrs.append(hasher(token))
            
            # For doc contain token id r
            for doc_id in docs_id:
                for hidx, hr in enumerate(hrs):
                    if hr < signatures[doc_id][hidx]:
                        signatures[doc_id][hidx] = hr

        return signatures

if __name__ == "__main__":
    pass


            
        