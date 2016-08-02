def even_odd(x):
    if x%2==0:
       print x,"is EVEN"
    else:
       print x,"is odd"

def do_n(n,x):
    for i in range(n):
        even_odd(x)

do_n(5,10)
