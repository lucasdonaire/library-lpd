def returnF(expoente):
    return lambda x: expoente**x

f = returnF(2)
# == def f(x) return 2**x

def returnClass(t):
    class classe:    
        def tplusx(self,x):
            return t+x
        def ttimesx(self,x):
            return t*x
        def texpx(self,x):
            return t**x
    return classe



a = returnClass(2)
print(type(a))
a_ = a()
print(type(a_))
print(a_.tplusx(3))
