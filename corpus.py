

class Corpus(object):
    """Represent corpus of documents use in LSH
    - docs: Contain docs of shingles
    - new_docs: mapping shingles to 0 => num shingles.
    - idx_docs: idx -> docs contain idx.
    """
    def __init__(self, docs):
        self._docs = docs
        self.new_docs, self.idx_docs, self.value_to_idx = self.remap_index()

    def remap_index(self):
        """Remap index to 0 -> num shingles"""
        print("Remap token to index from 0 -> len(token)")
        value_to_idx = {}
        cnt = 0
        new_docs = []
        idx_docs = []

        for doc_id, doc in enumerate(self._docs):
            new_doc = []

            for token in doc:
                if token in value_to_idx:
                    # Map id
                    word_id = value_to_idx[token]
                else:
                    # New token
                    word_id = cnt
                    value_to_idx[token] = word_id
                    idx_docs.append([])
                    cnt += 1

                # Add to doc
                new_doc.append(word_id)
                # Add doc to list contain idx
                idx_docs[word_id].append(doc_id)

            new_docs.append(new_doc)
        
        print("Number of shingles = {}".format(len(value_to_idx)))
        return new_docs, idx_docs, value_to_idx

    def metadata(self):
        return self.new_docs, self.idx_docs, self.value_to_idx
    
    def get_idx_docs(self):
        return self.idx_docs
    
    def get_num_docs(self):
        return len(self._docs)

if __name__ == "__main__":
    # Read docs

    # Convert to corpus
    pass

