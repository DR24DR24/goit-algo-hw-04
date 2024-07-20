import random
import timeit

def merging(arr,arr_temp,start_seg1,start_seg2,end_seg2):
    index1=start_seg1
    index2=start_seg2
    index_result=start_seg1
    while index1<start_seg2 and index2<end_seg2:
        if arr[index1]>arr[index2]:
            arr_temp[index_result]=arr[index2]
            index2+=1
        else:
            arr_temp[index_result]=arr[index1]
            index1+=1
        index_result+=1
    while index1<start_seg2: #and index1<end_seg2:
        arr_temp[index_result]=arr[index1]
        index1+=1
        index_result+=1
    while index2<end_seg2:
        arr_temp[index_result]=arr[index2]
        index2+=1
        index_result+=1
    


def define_segment_and_merging(arr:list, segment_length:int):
    length=len(arr)
    arr_temp=[None]*length
    i=None
    for i in range(0,length-segment_length*2,segment_length*2):
        merging(arr,arr_temp,i,i+segment_length,i+2*segment_length)
    #if (length-i)>3*segment_length:
    if (i is not None ): 
        if (length-i)>3*segment_length:
            merging(arr,arr_temp,i+segment_length*2,i+3*segment_length,length)
        else:
            for j in range(i+segment_length*2,length):
                arr_temp[j]=arr[j]
    else:
        merging(arr,arr_temp,0,segment_length,length)

    arr.clear()
    arr.extend(arr_temp)

def mergesort(data):
    length=len(data)
    segment_length=1
    while segment_length<length:
        define_segment_and_merging(data,segment_length)  
        segment_length*=2
    

def insertion_sort(arr:list,segment_start:int,segment_length:int):
    
    for i in range(segment_start+1,segment_start+segment_length):
        temp=arr[i]
        for j in range(i,segment_start,-1):
            if temp<arr[j-1]:
                arr[j] = arr[j-1]
            else: 
                arr[j]=temp
                break
        else:
            arr[segment_start]=temp

    

def define_segment_insert(arr:list, segment_length:int):
    length=len(arr)
    #arr_temp=[None]*length
    i=None
    for i in range(0,length-segment_length+1,segment_length):
        insertion_sort(arr,i,segment_length)
    #if (length-i)>3*segment_length:
    if (i is not None ) and (length-i)>segment_length:
        insertion_sort(arr,i+segment_length,length-i-segment_length)
    if (i is None ):
        insertion_sort(arr,0,length)


def merge_insertion_sort(data:list,segment_initial_length:int):
    define_segment_insert(data,segment_initial_length)
    length=len(data)
    segment_length=segment_initial_length
    while segment_length<length:
        define_segment_and_merging(data,segment_length)  
        segment_length*=2

def dotestdata(length)->list:
    return [random.randint(0,length) for _ in range(length) ]

def check_sort_data(data):
    length=len(data)
    for i in range(1,length):
        if data[i]<data[i-1]:
            return False
    return True

def write_test_data(name,size):
    data=dotestdata(size)
    with open(name,"w") as file:
        for items in data:
            file.write(f"{items}\n")
    print(f"data with size {size} in file {name}")

def load_test_data(name):
    with open(name,"r") as file:
        data=[int(line) for line in file]
    return data



# for i in range(11,12):
#     data=dotestdata(i)

#     print(data)
#     #mergesort(data)
#     #define_segment_insert(data,3)
#     merge_insertion_sort(data,6)
#     print(data)
size=100000
#write_test_data("test10.txt",size)
data=load_test_data("test10.txt")
#print(data)
time_merge_insertion=timeit.timeit(\
    stmt=lambda: merge_insertion_sort(data,8),number=1)
print(f"time_merge_insertion {time_merge_insertion} {check_sort_data(data)}")
#merge_insertion_sort(data,4)
#print(data)
# data=load_test_data("test10.txt")
# time_insertion_sort=timeit.timeit(\
#     stmt=lambda: insertion_sort(data,0,size),number=1)
# print(f"time_insertion_sort {time_insertion_sort}")
#print(data)
#insertion_sort(data,0,10)
#print(data)
data=load_test_data("test10.txt")
#print(data)
time_mergesort=timeit.timeit(\
    stmt=lambda: mergesort(data),number=1)
print(f"time_mergesort {time_mergesort} {check_sort_data(data)}")
print(time_merge_insertion/time_mergesort)
#print(data)
#mergesort(data)
#print(data)
