#attempt one
def convert( s, numRows):
	if numRows == 1:
		return s
	sLen = len(s)
	temp = 0
	rows = [""]*numRows
	while (temp < sLen):
		col = 1 + (numRows - 2)
		#first column
		for i in range(0,numRows):
			try:
				rows[i]+= s[temp+i]
			except:
				rows[i] += ""
		print(rows)
		#dynamic ziz zag column
		for i in range(1,numRows-1):
			if (temp+i+numRows-1) >= sLen:
				break
			pos = (numRows-2) - i +1
			try:
				rows[pos] += s[temp+i+numRows-1]
				#setting empty space for all rows in same column
				print(rows)
				for j in range(0,numRows):
					if pos == j:
						continue
					rows[j] += ""
			except:
				rows[pos] += "*"
				continue
			print(rows)
		# return
		temp += numRows + (numRows - 2)
	for i in rows:
		print(i)
	print("".join(rows))
	return "".join(rows)

print(convert("PAYPALISHIRING",2))