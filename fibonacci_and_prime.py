# To check a number is fibonacci and prime or not
#0,1,1,2,3,5,8,13
def fibonumber(n):
    first = 1
    second  = 1
    i = 1
    l = []
    fibo = False
    l.append(0)
    l.append(first)
    l.append(second)
    while(i<n):
        
        third = first +second
        l.append(third)
        #print(third)
        first = second
        second = third
        i = i+1
    for j in range(0,len(l)):
        if(n == l[j]):
            #print( "a fibonacci")
            fibo = True
            
        #else:
        #   print("not a fibonacci")
    if(fibo):
        return "a fibonacci"
    else:
        return "not a fibonacci"



# prime number
def primenumber(n):
    prime = True
    for i in range(2,n):
        if(n%i!=0):     
            pass
        else:
            #print(i , "else")
            prime= False
    if(prime):
        return "prime number"
    else:
        return "not a prime"


def all(n):
    print(primenumber(n))
    print(fibonumber(n))

all(7)