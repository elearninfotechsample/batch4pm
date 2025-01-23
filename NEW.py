class sample:
    '''this is oops example'''
    a=100
    def __init__(self):
        print('const')
    def m(self,a,b):
        print(a+b)
obj=sample()
obj.m(1,2)
print(obj.__doc__)
