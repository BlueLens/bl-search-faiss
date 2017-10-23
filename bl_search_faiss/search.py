import numpy as np
import time
from util import s3

import json
import os
import uuid
from os import listdir
from os.path import isfile, join

IMG_NUM = 1408
QUERY_IMG = 22
CANDIDATES = 5

NUM_CLASSES = 89

STR_BUCKET = "bucket"
STR_STORAGE = "storage"
STR_CLASS_CODE = "class_code"
STR_NAME = "name"
STR_FORMAT = "format"

class Search:
  def __init__(self):
    print('init')

  def search_imgage(self, image_file):
    print("")



