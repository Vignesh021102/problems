def lastWordLen(s):
    n = -1
    isLastLetter = False
    num = 0
    while True:
        try:
            if s[n] != ' ':
                isLastLetter = True
                num += 1
            elif isLastLetter == True:
                return num
        except:
            return num
        n -= 1

print(lastWordLen('abc   xyz '))