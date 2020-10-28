def numberbefore(string, sym):
    indexSym = string.find(sym)
    numArray = []
    i = 1
    while True:
        if (string[indexSym-i].isdigit or string[indexSym-i] == ".") and indexSym-i >= 0:
            numArray.append(string[indexSym-i])
            i+=1
        else:
            numArray.reverse()
            return float("".join(numArray))
        
def numberafter(string, sym):
    indexSym = string.find(sym)
    numArray = []
    i = 1
    if string[indexSym+i] == "+" or string[indexSym+i] == "-" or string[indexSym+i] == "*" or string[indexSym+i] == "/":
        numArray.append(string[indexSym+i])
        i+=1
    while True:
        if indexSym+i < len(string):
            if (string[indexSym-i].isdigit or string[indexSym-i] == "."):
                numArray.append(string[indexSym+i])
                i+=1
            else:
                return float("".join(numArray))
        else:
            return float("".join(numArray))
        
def binaryOperators1(string):
    if "-" in string or "+" in string:
        for i in range(string.count("+")+string.count("-")):
            if (string.find("+") < string.find("-") or (string.find("+")>-1 and string.find("-")==-1)) and string.find("+")!=-1:
                num1 = numberbefore(string,"+")
                num2 = numberafter(string,"+")
                string = string.replace(str(num1)+"+"+str(num2), str(num1+num2))
                if string.find("-")==-1 and string.find("+")==-1:
                    return string
            elif string.find("-") < string.find("+") or (string.find("-")>-1 and string.find("+")==-1) and string.find("-")!=-1:
                num1 = float(numberbefore(string,"-"))
                num2 = float(numberafter(string,"-"))
                string = string.replace(str(num1)+"-"+str(num2), str(num1-num2))
                if string.find("-")==-1 and string.find("+")==-1:
                    return string
    else:
        return string
    return string
def binaryOperators2(string):
    if "/" in string or "*" in string:
        for i in range(string.count("*")+string.count("-")):
            if (string.find("*") < string.find("/") or (string.find("*")>-1 and string.find("/")==-1)) and string.find("*")!=-1:
                num1 = numberbefore(string,"*")
                num2 = numberafter(string,"*")
                string = string.replace(str(num1)+"*"+str(num2), str(num1*num2))
                if string.find("*")==-1 and string.find("/")==-1:
                    return string
            elif string.find("/") < string.find("*") or (string.find("/")>-1 and string.find("*")==-1) and string.find("/")!=-1:
                num1 = float(numberbefore(string,"/"))
                num2 = float(numberafter(string,"/"))
                string = string.replace(str(num1)+"/"+str(num2), str(num1/num2))
                if string.find("/")==-1 and string.find("*")==-1:
                    return string
    else:
        return string
    return string
def calculator(string):
    string = binaryOperators2(string)
    string = binaryOperators1(string)
    return string
string = input()
print(calculator(string))

