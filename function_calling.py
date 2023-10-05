sl = 10       #Global
def function1(n):
    # l = 5
    m = 8
    global l
    l = l+45

    print(n,"I have printed\n")

function1("This is me\n")
print(l)






x = 89
def saraj():
    x = 20
    def rohan():
        global x
        x = 88
        # print("before calling rohan()", x)
        rohan()
        print("after calling rohan()", x)

    saraj()
    print(x)





