import ApplicationRuntime as ar

Layout = ar.link("layout.xml")

def Begin():
    #Your code at start MainContent page here
    pass

def ChangeText():
    Text1 = Layout.Detail("Text1")
    Text1.param(InquotesData="Thanks for click :3")