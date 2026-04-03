import random

# get  a number

randonnum = random.randrange(1,100)

def getnumber():
    usernumber = input(' Ge a number ')
    print(usernumber, randonnum)


    return usernumber

def evaluate (x, randonnum ):

    print('val X: ', x , randonnum)

    if (x>randonnum):
        print('x > random')
        return ('store')
    elif (x<randonnum):
        print('x < random')
        return ('mindre')
    else:
        print('x = random')
        return ('equal')




while True:
    val = int(getnumber())

    #print (f'number : ', val)
    response = evaluate(val, randonnum)

    print ('response  : ', response)







