
#implementation headr
#header for add()
def add(x,y):
   return x-y

#header for sub()
def sub(x,y):
    return x-y  #on master branch

#header for mul()
def mul(x,y):
    return x*y  #on branch bug456

#header for div

def div(x,y):   #on master branch
    if y==0:
        return DIVIDE_BY_0_ERROR
    else:
        return x/y
#implement squre 
def square(x):  
    return x*x
#just to see stash