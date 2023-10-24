# https://leetcode.com/problems/string-to-integer-atoi/
import time
import sys

import re
def myAtoi(s: str) -> int:
  s = s.strip()
  try:
    num = int(re.search("((\s|^)[+-]\d+|^\d+)",s).group())
    min_val = -2**31
    max_val = 2**31 - 1
    
    if num < min_val:
        return min_val
    elif num > max_val:
        return max_val
    else:
        return num
  except:
    return 0

#41ms
#16mb
print(myAtoi("awd ad 987"))

start_time = time.time()
myAtoi("awd ad 987")  # Call the function with a specific input
end_time = time.time()
time_complexity = (end_time - start_time) * 1000 

# Calculate Space Complexity
memory_usage = sys.getsizeof(myAtoi("awd ad 987")) / (1024**2)

print(f"Time Complexity: {time_complexity:.7f} ms")
print(f"Space Complexity: {memory_usage:.7f} MB")