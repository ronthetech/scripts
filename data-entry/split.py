"""
Python function to split a string into a list, and 
remove whitespaces. 
Respects the '/' separator.
"""

import re


def split_string(input_str: str):
  word_list = re.split(" |(/)", input_str)

  for item in word_list:
    if item is None:
      word_list.remove(item)

  return word_list