from collections import defaultdict

class Corpus(object):
    """Represent corpus of documents use in LSH
    - docs: Contain docs of shingles
    - new_docs: mapping shingles to 0 => num shingles.
    - idx_docs: idx -> docs contain idx.
    """
    def __init__(self, docs):
        self._docs = docs
        self.token_to_docs = self.remap_index()

    def remap_index(self):
        """Remap index to 0 -> num shingles"""
        print("Remap token to index from 0 -> len(token)")
        token_to_docs = defaultdict(list)
        token_to_idxs = {}
        cnt = 0

        for doc_id, doc in enumerate(self._docs):
            new_doc = []

            for token in doc:
                if token in token_to_idxs:
                    idx = token_to_idxs[token]
                else:
                    token_to_idxs[token] = cnt
                    idx = cnt
                    cnt += 1
                token_to_docs[idx].append(doc_id)

        print("Number of shingles = {}".format(len(token_to_docs)))
        return token_to_docs
    
    def get_token_docs(self):
        return self.token_to_docs 
    
    def get_num_docs(self):
        return len(self._docs)

if __name__ == "__main__":
    # Read docs
    # Convert to corpus
    pass

