"""
Python program to take a string in all uppercase, 
and return it with the first letter of each word
capitalized and the rest lowercase. 
Respects the '/' separator.
"""

import re
from join import join_string
from split import split_string


# Driver Function
if __name__ == "__main__":
  user_input = input()
  # tests
  # user_input = "a100A SOME COLOR/ANOTHER COLOR"
  # user_input2 = "100 SOME COLOR/ANOTHER COLOR/THIRD COLOR"

  # Splitting the string
  word_list = split_string(user_input)

  # Joining the string
  word_list = join_string(word_list, "capitalize")
  print(word_list)