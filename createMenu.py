def createMenu(optionList);
tmp = ""; ct=0
for opt in optoinList:
    tmp += str(ct) + ", " opt + "\n"
    ct += 1
return tmp
