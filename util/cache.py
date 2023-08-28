#!/usr/bin/env python3
import os
import shutil
import glob
import logging
from . import directory

def files():
            return(glob.glob(directory.cache + "*"))

def clear():
            logging.info("clearing cache")
            for file in files():
                        os.remove(file)

def store(file):
            shutil.copy(file, directory.cache)
