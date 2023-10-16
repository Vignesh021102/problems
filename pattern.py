def check(num):
  for i in range(1,num*2):
    i = (num*2) - i if i>=num else i
    string = " "* ((num//2)+num-i)
    string += "* "*i
    print(string)
    print()

check(int(input("Enter num: ")))