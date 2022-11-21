def selection_sort(arr):
    for i in range(0,len(arr)-1):
        curr_min_idx = i 
        for j in range(i+1, len(arr)):
            if arr[j]<arr[curr_min_idx]:
                curr_min_idx = i
        
        arr[i], arr[curr_min_idx] = arr[curr_min_idx],arr[i]    #swap
         





arr = [2,6,5,1,3,4]
selection_sort(arr)
print(arr)