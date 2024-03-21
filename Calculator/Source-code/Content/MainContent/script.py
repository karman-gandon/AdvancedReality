import ApplicationRuntime as ar

Layout = ar.link("layout.xml")

expression = "0"
Text1 = Layout.Detail("Calculated")

def Begin():
    #Your code at start MainContent page here
    Text1.param(InquotesData="0")

def add0():
    global expression
    expression += "0"
    Text1.param(InquotesData=expression)

def add1():
    global expression
    expression += "1"
    Text1.param(InquotesData=expression)

def add2():
    global expression
    expression += "2"
    Text1.param(InquotesData=expression)

def add3():
    global expression
    expression += "3"
    Text1.param(InquotesData=expression)

def add4():
    global expression
    expression += "4"
    Text1.param(InquotesData=expression)

def add5():
    global expression
    expression += "5"
    Text1.param(InquotesData=expression)

def add6():
    global expression
    expression += "6"
    Text1.param(InquotesData=expression)

def add7():
    global expression
    expression += "7"
    Text1.param(InquotesData=expression)

def add8():
    global expression
    expression += "8"
    Text1.param(InquotesData=expression)

def add9():
    global expression
    expression += "9"
    Text1.param(InquotesData=expression)

def add0():
    global expression
    expression += "0"
    Text1.param(InquotesData=expression)

def addplus():
    global expression
    expression += "+"
    Text1.param(InquotesData=expression)

def addminus():
    global expression
    expression += "+"
    Text1.param(InquotesData=expression)

def addmult():
    global expression
    expression += "+"
    Text1.param(InquotesData=expression)

def adddiv():
    global expression
    expression += "+"
    Text1.param(InquotesData=expression)

def clr():
    global expression
    expression = ""
    Text1.param(InquotesData=expression)

def calc():
    global expression
    expression = eval(expression)
    Text1.param(InquotesData=expression)

