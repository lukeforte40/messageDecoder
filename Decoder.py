def txtToDictionary(txtFile):
    txtKey = ''
    txtValue = ''
    txtDict = {}
    file = open(txtFile)
    for line in file:
        for char in line:
            if char.isdigit():
                txtKey += char
            elif char == ' ':
                continue
            elif char == '\n':
                continue
            else:
                txtValue += char
        if txtKey != '':
            txtKey = int(txtKey)
            txtDict[txtKey] = txtValue
        txtKey = ''
        txtValue = ''
    return txtDict

def calcNextNum(currentNum, lastNum):
    if currentNum == 1:
        currentNum += 2
    else:
        diff = currentNum - lastNum
        diff += 1
        currentNum = currentNum + diff
    return currentNum

def decode(txtDict):
    currentNum = 1
    lastNum = 1
    nextNum = 1
    outputString = ''
    while txtDict.get(currentNum) != None:
        outputString += txtDict.get(currentNum) + ' '
        nextNum = calcNextNum(currentNum, lastNum)
        lastNum = currentNum
        currentNum = nextNum
    return outputString

txtDict = txtToDictionary('coding_qual_input.txt')
print(decode(txtDict))
