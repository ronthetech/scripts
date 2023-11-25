"""
Python function to join a string from a list, and 
return it with formatting based on given argument. 
Respects the '/' separator.
"""

import re


def join_string(input_list: list[str], case: str) -> str:
  for i, word in enumerate(input_list):
    if i > 0: # add option to make this a user input
      input_list[i] = eval(f"word.{case}()")

  if case == "capitalize" :
    code = input_list.pop(0)
    input_list[-1] += "-" + code

  word_list = re.sub(" / ", "/"," ".join(input_list))

  return word_list