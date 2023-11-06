def merge_three_sorted_array(arr1,arr2,arr3):
    result=[]
    i=j=k=0
    while i < len(arr1) and j< len(arr2) and k< len(arr3):
        min_val=min(arr1[i],arr2[j],arr3[k])
        result.append(min_val)

        if min_val==arr1[i]:
            i+=1
        elif min_val==arr2[j]:
            j+=1
        else:
            k+=1

    while i< len(arr1):
       result.append(arr1[i])
       i+=1
    while j< len(arr2):
        result.append(arr2[j])  
        j+=1
    while k< len(arr3):
       result.append(arr3[k])
       k+=1 
    return result
arr1=[1,3,5,7,6] 
arr2=[12,13,14,15] 
arr3=[2,4,8,10,9,11]     
merge_array=merge_three_sorted_array(arr1,arr2,arr3)
print(merge_array)

