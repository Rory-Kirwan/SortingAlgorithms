from time import *
from random import *
import sys

### A function to check if a list is sorted ###
def checksorted(inlist, Algorithm) -> bool:
    '''
        Function : To check if an inputted list is sorted or not
        Input : A list
        Output : A boolean True or False depending on wether or not the list is sorted
    '''
    #assign counters
    i = 0
    n = 1
    a  = 0
    #iterate trough the list
    while n < len(inlist):
        #compare the current index in the list with the next index in sequence
        if inlist[i] > inlist[n]:
            #if it is not sorted add one to the failure check
            a += 1
        #iterate through the counters
        i += 1
        n += 1
    #check if the failure check has had anything added to it
    if a > 0:
        Algorithm(inlist)
    elif a == 0:
        #return True if it is sorted
        return True


def randomlist(n,k):
    #define misc. variables
    i = 0
    new_list = []
    #while loop ton generate the list
    while i < n - k:
        #random number to append to the list
        b = randint(1, n - k)
        new_list.append(b)
        i += 1
    #reset the iterable
    i = 0
    #another while loop to generate the duplicates
    while i < k:
        #find an integer to duplicate
        b = new_list[randint(0, (n - k - 1))]
        #append it onto the end
        new_list.append(b)
        i += 1
    shuffle(new_list)
    #return the randomly shuffled list
    return new_list


### Test the runtime of one algorithm with one inputted list ###
def testonealg(inlist, Algorithm):
    start_time = perf_counter()
    Algorithm(inlist)
    end_time =  perf_counter()
    checksorted(inlist, Algorithm)
    return end_time - start_time  

def evaluate(n, k, num, f):
    '''
    generate num lists with length n and duplicates k
    then call testonalg(list, f) on each of them 
    computes the average runtime and prints it to screen
    ''' 
    b = 0
    i = 1
    listoflists = []
    if type(num) == int:
        while i <= num:
            listoflists.append(randomlist(n , k))
            i += 1
    elif type(num) == list:
        listoflists = num
    for n in listoflists:
        a = testonealg(n, f)
        b += a
    if type(num) == list:
        return "runtime :" + str(b/len(num))
    elif type(num) == int:
        return "runtime :" + str(b/num)

def evaluateall(n,k,num,funcs: list):
    print("Size of lists :", n, " Amount of duplicates :", k)
    input = []
    i = 0
    while i <= num:
        input.append(randomlist(n,k))
        i += 1

    for i in funcs:
        a = evaluate(n, k, input, i)
        func_name = i.__name__
        print(func_name, a)
    return None