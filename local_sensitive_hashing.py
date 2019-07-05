from collections import defaultdict

class LocalSensitiveHashing(object):
    def __init__(self, signatures, 
            row_p_band=4):
        """ Local sensitive hashing
        Return: 
        - signatures: min hash signatures. Size ndocs * k matrix. Each value in range [0, cool_prime - 1]
        - n_bucket: Number of bucket to hash each band into. Select here
        - row_p_band: number of rows per band. NUmband = total_rows // row_p_band
        Refer to this
        https://medium.com/engineering-brainly/locality-sensitive-hashing-explained-304eb39291e4
        """
        self._signatures = signatures
        self._n_docs = len(signatures)
        self._k = len(signatures[0])
        self._row_p_band = row_p_band
        self._n_band = self._k // self._row_p_band

        self.buckets = [defaultdict(list) for _ in range(self._n_band)]
        self.share_signatures = [[] for _ in range(self._n_band)]

    def get_band(self, docid, bucid):
        # Get band of docid in bucid
        return tuple(self._signatures[docid] \
                [bucid * self._row_p_band: (bucid + 1) * self._row_p_band])
    
    def hashing(self):
        # Constructing buckets
        for docid in range(self._n_docs):
            for bucid in range(self._n_band):
                # Add to bucket bucid, of this band 
                band = self.get_band(docid, bucid)
                self.buckets[bucid][band].append(docid)

                # If len == 2: bucket shared
                if len(self.buckets[bucid][band]) == 2:
                    self.share_signatures[bucid].append(band)

        # Constructing doc that close to each other.
        doc_to_docs = defaultdict(set)
        for bucid in range(self._n_band):
            for band in self.share_signatures[bucid]:
                docs_id = self.buckets[bucid][band]

                ## Add to adjacent docs.
                for doc_id in docs_id:
                    doc_to_docs[doc_id].update(docs_id)
        
        for doc_id in doc_to_docs:
            doc_to_docs[doc_id].remove(doc_id)
        
        return doc_to_docs




        