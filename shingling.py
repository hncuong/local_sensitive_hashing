import hashlib
from utils import hashing_md5_to_32bit, preprocessing_doc

class Shingles(object):
    """Shingling documents in to set of shingles 
    and then compress them to 4 bytes tokens."""

    def __init__(self, k, hash_function=None):
        # shingles length
        self._k = k
        if hash_function is not None:
            self._hash_function = hash_function
        else:
            self._hash_function = hashing_md5_to_32bit


    def shingling(self, doc):
        doc = preprocessing_doc(doc)
        
        tokens = []

        # First token
        shingle = list(doc[:self._k])
        tokens.append(hashing_md5_to_32bit(''.join(shingle)))

        for i in range(self._k, len(doc)):
            # Move to next shingle
            shingle.pop(0)
            shingle.append(doc[i])

            # Hash
            tokens.append(hashing_md5_to_32bit(''.join(shingle)))
        
        return set(tokens)

if __name__ == "__main__":
    shingler = Shingles(k=4)
    print(shingler.shingling('Love the way you lie'))
    print(shingler.shingling('Love the way I lie'))

