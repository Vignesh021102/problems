
def check(s):
    s = s.lower()
    mid = int(len(s)/2)
    num1 = 0
    num2 = 0
    vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    for i in range(0,mid):
        try:
            vowels[s[i]]
            num1+=1
        except:
            0
        try:
            vowels[s[i+mid]]
            num2 += 1
        except:
            0

        #print(s[i],s[i+mid],num1,num2)
    return True if (num1 == num2) else False
print(check('AbCdEfGh'))