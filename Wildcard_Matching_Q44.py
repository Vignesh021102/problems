import re

#time limit: didn't pass
#try1
def matchString(s , p) -> bool:
  p = re.sub(r"[*]+",".*",p)
  # p = re.sub(r"[?]+",".",p)
  p = p.replace("?",".")
  # p = p.replace("*",".*")
  p += "$"
  return True if re.match(p,s) else False
#try2
def matchString(s , p) -> bool:
	i ,j = [0,0]
	sLen = len(s)
	pLen = len(p)
	try:
		while i < sLen or j < pLen:
		# print(s[i], p[j])
			if s[i] == p[j]:
				i += 1
				j += 1
			elif p[j] == "?":
				i+=1
				j+=1
			elif p[j] == "*":
				try:
					if j == pLen-1:
						j += 1
						i = sLen
						continue
					
					if p[j+1] == "*":
						j+=1
						i+=1
						continue
					# s = avadw p = *d*
					i += 1
					k = j+1
					# print(" innerLoop")
					while  k < pLen:
						# print(" ",s[i],p[k],p[k] != s[i],p[k]==s[i] or p[k] == "?",p[k] != "*")
						if p[k] == s[i] or p[k] == "?":
							k+=1
							i+=1
						elif p[k] == "*":
							break
						elif p[k] != s[i]:
							i+=1
					j = k
				except:
					return False
	except:
		return False
	# print(i,sLen,j,pLen,i == sLen and  j == pLen)
	if i == sLen and  j == pLen:
		return True
	return False


print(matchString("aa","a"))
print(matchString("aa","*"))
print(matchString("cs","*s"))
# print(matchString("badwabczzza","?*?abc*a*"))
# print(matchString("mississippi","m??*ss*?i*pi"))
# print(matchString("abbabaaabbabbaababbabbbbbabbbabbbabaaaaababababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaaaaabbbbbaabaaababaaaabb","**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb"))