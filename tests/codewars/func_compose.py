# Function composition is a mathematical operation that mainly presents itself 
# in lambda calculus and computability. 

def compose(f, g):
    def z(*args, **kwargs):
        return f(g(*args, **kwargs))
    return z

f = lambda x: x**2
g = lambda x: 2*x + 3
print(compose(f, g)(0))

def l_compose(f, g):
    return lambda *args: f(g(*args))

print(l_compose(g,f)(1))