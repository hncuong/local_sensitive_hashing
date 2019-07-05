
class LocalSensitiveHashing(object):
    def __init__(self, signatures, k_cool_prime=1000000007):
        """ Local sensitive hashing
        Return: 
        - signatures: min hash signatures. Size  * ndocs matrix. Each value in range [0, cool_prime - 1]
        - k_cool_prime: a cool prime ~1e9. Number of bucket to hash each band into. Select here 
        http://compoasso.free.fr/primelistweb/page/prime/liste_online_en.php
        """
        self._signatures = signatures
    
    def tune_bucket(self):
        pass

    def hashing(self):
        pass
        