#!/usr/bin/env python3
import os
import shutil
import glob
import logging

module_directory = os.path.dirname(os.path.abspath(__file__))
cache_directory = os.path.join(module_directory, 'cache/')

def files():
            return(glob.glob(cache_directory + "*"))

def clear():
            logging.info("clearing cache")
            for file in files():
                        os.remove(file)

def store(list_of_files):
            for file in list_of_files:
                        shutil.copy(file, cache_directory)
