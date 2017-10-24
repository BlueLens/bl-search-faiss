import faiss

import os

IMG_NUM = 1408
QUERY_IMG = 22
CANDIDATES = 5

NUM_CLASSES = 89

STR_BUCKET = "bucket"
STR_STORAGE = "storage"
STR_CLASS_CODE = "class_code"
STR_NAME = "name"
STR_FORMAT = "format"
nq = 1
n_candidates = 10

INDEX_FILE = os.environ['INDEX_FILE']

class Search:
  def __init__(self):
    print('init')
    self.index = faiss.read_index(INDEX_FILE)

  def query(self, vector):
    self.index.nprobe = 1
    result_d1, result_i1 = self.index.search(vector, n_candidates)
    print(result_d1)
    print(result_i1)



