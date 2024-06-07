#f(n) = f(n-1)+f(n-2)

def fibbo(n):
    assert n>=0 and int(n),"must be positive int or zero" 
    if n in [0,1]:
        return n
    else:
        return fibbo(n-1) + fibbo(n-2)
    
print(fibbo(-6))
