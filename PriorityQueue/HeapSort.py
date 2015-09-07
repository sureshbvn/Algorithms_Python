__author__ = 'sureshbvn'
from PriorityQueue import Heap




def Heap_sort(heap):
    heap.printHeap()
    length=heap.size
    leastParent=length//2
    while(heap.size>0):
        temp=heap.heap[heap.size]
        heap.heap[heap.size]=heap.heap[1]
        heap.heap[1]=temp
        heap.size=heap.size-1
        heap.percolateDown(1)






if __name__=="__main__":
    heap=Heap()
    array=[100,30,40,1,2,3]
    heap.build_heap(array)
    Heap_sort(heap)
    heap.size=len(array)
    heap.printHeap()
