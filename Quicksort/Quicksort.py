from typing import List
def partition(arr:List[int],low:int,high:int)->int:
	pivot = arr[high]
	i = low-1
	for j in range(low,high):
		if arr[j] <= pivot:
			i = i + 1
			temp = arr[i]
			arr[i] = arr[j]
			arr[j] = temp
	
	temp = arr[i+1]
	arr[i+1] = arr[high]
	arr[high] = temp
	return i+1

def quickSort(arr:List[int],low:int,high:int):
 	if low < high:
 		pi = partition(arr,low,high)
 		quickSort(arr,low, pi-1)
 		quickSort(arr,pi+1,high)
 
arr = [10, 7, 8, 9, 1, 5]
n = 6
quickSort(arr,0,n-1)

