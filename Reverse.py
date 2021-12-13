def rev(f):
    def g(x,y): return f(y,x)
    return g
