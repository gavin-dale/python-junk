def myfunc(a,b,c=0,d=0,e=0):
    # returns 5% of sum of a and b
    return sum((a,b)) * .05
def myFuncArgs(*args):
    return sum(args) * 0.05

print(myFuncArgs(1,2,3,4,5,6,7))

def myFuncKwargs(**kwargs):
    if 'fruit' in kwargs:
        print('yummy yummy {}'.format(kwargs['fruit']))
    else: 
        print('no fruit here')

print(myFuncKwargs(fruit='apple', veggie='lettuce'))

def myFuncBoth(*args,**kwargs):
    print('I would like {} {}'.format(args[0],kwargs['food']))

myFuncBoth(10,20,30,fruit='orange',food='eggs',animal='dog')


