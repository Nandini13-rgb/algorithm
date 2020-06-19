def bubble_sort(arr):
  for j in range(len(arr)):
      for i in range(len(arr)-1):
          if arr[i] > arr[i+1]:
              temp = arr[i+1]
              arr[i+1] = arr[i]
              arr[i] = temp
  print(arr)
bubble_sort([3,4,7,8,1,2,5,6,9,10])
            
