a=1000 #gv

def f1():
    global a
    a=2000 #lv
    c=3000 #lv

    print(globals() ['a'])

def f2():
    print(a)

f1()
f2()
