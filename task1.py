import random

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
    


def define_segment(arr:list, segment_length:int):
    length=len(arr)
    arr_temp=[None]*length
    i=None
    for i in range(0,length-segment_length*2,segment_length*2):
        merging(arr,arr_temp,i,i+segment_length,i+2*segment_length)
    #if (length-i)>3*segment_length:
    if (i is not None ) and (length-i)>3*segment_length:
        merging(arr,arr_temp,i+segment_length*2,i+3*segment_length,length)
    else:
        merging(arr,arr_temp,0,segment_length,length)

    arr.clear()
    arr.extend(arr_temp)

def mergesort(data):
    length=len(data)
    segment_length=1
    while segment_length<length:
        define_segment(data,segment_length)  
        segment_length*=2
    



def dotestdata(length)->list:
    return [random.randint(0,1000) for _ in range(length) ]
for i in range(1,11):
    data=dotestdata(i)

    print(data)
    mergesort(data)
    print(data)