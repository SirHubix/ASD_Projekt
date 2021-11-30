import numpy
import time
import sys
from Quicksort import quickSort
from Mergesort import mergeSort
from Heapsort import heapSort
from Bubblesort import bubbleSort

sys.setrecursionlimit(9999999)

normalArray = numpy.arange(0, 500000)
print(normalArray)
reversedArray = normalArray[::-1]
print(reversedArray)
randomArrray = numpy.random.randint(0, 500000, 500000)
print(randomArrray)
# QUICKSORT
arr = randomArrray
r = len(arr) - 1
start = time.time()
quickSort(arr, 0, r)
end = time.time()
print(f'{end - start} losowy quciksort')
"""arr = normalArray
start = time.time()
quickSort(arr, 0, r)
end = time.time()
print(f'{end - start} posortowany quicksort ')
arr = reversedArray
start = time.time()
quickSort(arr, 0, r)
end = time.time()
print(f'{end - start} odwrotny  quicksort ')"""

# MERGESORT
arr = randomArrray
start = time.time()
mergeSort(arr)
end = time.time()
print(f'{end - start} losowy mergesort ')
arr = normalArray
start = time.time()
mergeSort(arr)
end = time.time()
print(f'{end - start}  posortowany mergesort ')

arr = reversedArray
start = time.time()
mergeSort(arr)
end = time.time()
print(f'{end - start} tablica odwrócona mergesort ')

print('Heapsort')
arr = randomArrray
start = time.time()
heapSort(arr)
end = time.time()
print(f'{end - start} losowy heapsort ')
arr = normalArray
start = time.time()
heapSort(arr)
end = time.time()
print(f'{end - start} posortowany heapsort')
arr = reversedArray
start = time.time()
heapSort(arr)
end = time.time()
print(f'{end - start} tablica odwrócona heapsort')
print('Bubblesort')
arr = randomArrray
start = time.time()
bubbleSort(arr)
end = time.time()
print(f'{end - start} losowa - bubblesort ')
arr = normalArray
start = time.time()
bubbleSort(arr)
end = time.time()
print(f'{end - start} posortowana bubblesort ')
arr = reversedArray
start = time.time()
bubbleSort(arr)
end = time.time()
print(f'{end - start} odwrócona bubblesort')
