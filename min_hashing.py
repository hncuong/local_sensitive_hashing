import numpy as np
from utils import get_random_pseudo_perm_hasher, gen_random_hasher
from corpus import Corpus
from datetime import datetime

MAX_INT = 2**31 - 1

class MinHasher(object):
    """Min hashing list of sets"""

    def __init__(self, corpus, k=200, cool_prime=1000003):
        """
        - k: # "permute" hash functions. Default 100.
        - corpus: documents as Corpus object.
        - cool_prime: a prime that is litter bigger than number of unique shingles. Refer to:
            - http://ethen8181.github.io/machine-learning/clustering_old/text_similarity/text_similarity.html
            - http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php
        """
        self._k = k
        self._cool_prime = cool_prime

        self._ndocs = corpus.get_num_docs()
        self.token_to_docs = corpus.get_token_docs()
        self._hashers = self.get_hashers()
    
    def get_hashers(self):
        print("Generate {} random bucker hashers".format(self._k))
        # return gen_random_hasher(self._k)
        return get_random_pseudo_perm_hasher(self._cool_prime, self._k)

    def pseudo_perm_hasher(self):
        """Pseudo permutation hashing. MIN HASHING
        Return: ndocs * k matrix. Each value in range [0, cool_prime - 1]
        """
        # Do k hashing 
        # signatures = np.full((self._k, self._ndocs), MAX_INT, dtype=np.int32)
        signatures = [[MAX_INT] * self._k for _ in range(self._ndocs)] # n_docs * k

        # For each row
        for idx, (token, docs_id) in enumerate(self.token_to_docs.items()):
            if idx % 100000 == 0:
                print(datetime.now(), " - Processing shingle id {}.".format(idx))

            # DO perm hash functions for this row
            hrs = []
            for i in range(self._k):
                hasher = self._hashers[i]
                hrs.append(hasher(token))
            
            # For doc contain token id r
            for doc_id in docs_id:
                for hidx, hr in enumerate(hrs):
                    if hr < signatures[doc_id][hidx]:
                        signatures[doc_id][hidx] = hr

        return signatures

if __name__ == "__main__":
    pass


            
        