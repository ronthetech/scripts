"""
Python program to make a string all uppercase.
Respects the '/' separator.
"""

import re
from join import join_string
from split import split_string


# Driver Function
if __name__ == "__main__":
  # user_input = input()
  # tests
  user_input = "a100A Some Color/Another Color"
  # user_input2 = "100 Some Color/Another Color/Thir. Color"

  # Splitting the string
  word_list = split_string(user_input)

  # Joining the string
  word_list = join_string(word_list, "upper")
  print(word_list)