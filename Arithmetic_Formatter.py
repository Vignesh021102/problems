def arithmetic_arranger(arr):
    for i in range(len(arr)):
        arr[i] = arr[i].split(" ")
        match(arr[i][1]):
            case "+":
                arr[i].append(f"{int(arr[i][0])+int(arr[i][2])}")
            case "-":
                arr[i].append(f"{int(arr[i][0])-int(arr[i][2])}")
            case "/":
                arr[i].append(f"{int(arr[i][0])/int(arr[i][2])}")
            case "*":
                arr[i].append(f"{int(arr[i][0])*int(arr[i][2])}")
    maxLen = 0
    space = ""
    line = ""
    lines= ["","","",""]
    space4 = "    "
    for i in arr:
        space = ""
        line = ""
        maxLen = 0
        for j in range(4):
            if maxLen < len(i[j])+2:
                maxLen = len(i[j])+2
        for j in range(maxLen):
            space+=" "
            line+="-"
        lines[0]+=f"{space[:-len(i[0])]}{i[0]}{space4}"
        lines[1]+=f"{i[1]}{space[:-len(i[2])-1]}{i[2]}{space4}"
        lines[2]+=f"{line}{space4}"
        lines[3]+=f"{space[:-len(i[3])]}{i[3]}{space4}"
    for i in lines:
        print(i,"\n")
arithmetic_arranger(["32 + 698", "1 - 2", "45 + 43", "50 * 50"])