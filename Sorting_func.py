from Support_func import *

def Heap_Sort(input : list) -> list:
    L = len(input)
    for i in range(L):
        Bubble_Up(input,i)
    L = len(input)
    for i in range(L):
        input[0], input[L - 1 - i] = input[L - 1 - i], input[0]
        Bubble_Down(input,0, L-2-i)
    return input
def Bubble_Up(input, i):
    while i > 0:
        parent = (i-1) // 2
        if input[i] > input[parent]:
            input[i], input[parent] = input[parent], input[i]
            i = parent
        else:
            i = 0
def Bubble_Down(input, i, last):
    while last > (i*2):
        lc = i*2 + 1
        rc = i*2 + 2
        maxc = lc
        if last > lc and input[rc] > input[lc]:
            maxc = rc
        if input[i] < input[maxc]:
            input[i], input[maxc] = input[maxc], input[i]
            i = maxc
        else:
            i = last



def Merge_Sort(input : list) -> list:
    #if the lst is greater than 1 begin sorting
    if len(input) > 1:
        n = int(len(input))
        #splits the input list in two
        list1 = input[:n//2]
        list2 = input[n//2:]
        #recursively call the function on both lists
        Merge_Sort(list1)
        Merge_Sort(list2)
        #call the function ot merge them back together
        merge(list1, list2, input)
    #if list does not require sorting return it as is
    return input

#merge support function for merge sort
def merge(list1, list2, input):
    #establish counters
    i = 0
    n = 0
    #loop to iterate through the lists
    while i + n < len(input):
        #logic to merge the list
        if i == len(list1):
            input[i+n] = list2[n]
            n += 1
        elif n == len(list2):
            input[i+n] = list1[i]
            i += 1
        elif list2[n] < list1[i]:
            input[i+n] = list2[n]
            n += 1
        else:
            input[i+n] = list1[i]
            i += 1



def Quick_Sort(input : list) -> list:
    #establish the less then, equal then and greater than (relative to the pivot) lists
    less = []
    equal = []
    greater = []
    
    if len(input) > 1:
        #define the pivot (anything would work i just chose the very first)
        pivot = input[int(len(input)/2)]
        #iterate through the list
        for i in range(len(input)):
            #check if the current index is less than, equal to or greater than the pivot
            if input[i] < pivot:
                #append it to the correct list depending on the answer
                less.append(input[i])
            if input[i] == pivot:
                equal.append(input[i])
            if input[i] > pivot:
                greater.append(input[i])
        
        #recursively call this function to return a fully sorted list
        return Quick_Sort(less) + equal + Quick_Sort(greater)
    
    #if the list doesn't need sorting return the list as is
    else:
        return input



def Insertion_Sort(input : list) -> list:
    #establish the counters
    i = 0
    n = 1
    #loop for iterating through the list
    while n < len(input):
        a = i
        b = n
        #compare the two values
        if input[i] > input[n]:
            #loop backwards through the list to find its proper place
            while a >= 0:
                #check if it is out of order
                if input[a] > input[b]:
                    #if values are out of order swap them and delete the excess
                    input.insert(a, input[b])
                    input.pop(b+1)
                #update both counters -1 to move backwards down the list
                a -= 1
                b  -= 1
            #update both counters
            i += 1
            n += 1
        #if they are in order update the counters
        else: 
            i += 1
            n += 1
    #return the input once sorted
    return input

list_of_algorithms = [Heap_Sort, Merge_Sort, Quick_Sort, Insertion_Sort]
print(evaluateall(100000, 100, 15, list_of_algorithms))