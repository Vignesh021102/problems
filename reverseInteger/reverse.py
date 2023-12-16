import sys
def reverse(num):
  """
  Reverses the given number.

  Args:
      num (int or float): The number to be reversed.

  Returns:
      str: The reversed number as a string.

  Raises:
      ValueError: If the input is not a number.
  """
  if num >= 2**30 or num <= 2**31 * -1 :
    # raise ValueError("Number exceeds 32-bit integer range")
    return 0
  if isinstance(num, (int, float)):
    num = str(num)
  else:
    raise ValueError("Input must be a number")
  
  if num[0] == '-':
    result = -1 * int(num[:0:-1])
  else:
    result = int(num[::-1])
  return result

print(reverse(1534236469))