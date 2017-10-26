import faiss
import numpy as np
import os
import logging


NUM_CLASSES = 89

STR_BUCKET = "bucket"
STR_STORAGE = "storage"
STR_CLASS_CODE = "class_code"
STR_NAME = "name"
STR_FORMAT = "format"

INDEX_FILE = os.environ['INDEX_FILE']

class Search:
  def __init__(self):
    print('init')
    self.index = faiss.read_index(INDEX_FILE)
    logging.basicConfig(filename='/usr/src/app/app.log',level=logging.DEBUG)

  def query(self, vector, candidates=10):
    xq = np.expand_dims(np.array(vector, dtype=np.float32), axis=0)

    xq.astype(np.float32)
    result_d, result_i = self.index.search(xq, candidates)
    print(result_i)
    return np.squeeze(result_i)



