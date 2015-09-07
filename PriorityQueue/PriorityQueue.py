__author__ = 'sureshbvn'
class Heap:
    def __init__(self):
        self.heap=[0]#my heap starts with index 1. so keeping the first element zero always.
        self.size=0
    def parent(self,i):
        return i//2
    def leftChild(self,i):
        return 2*i
    def rightChild(self,i):
        return (2*i)+1
    def getMinChildIndex(self,i):
        if 2*i>self.size:
            return None

        if (2*i)+1>self.size:
            return 2*i
        else:
            if self.heap[2*i]<self.heap[(2*i)+1]:
                return 2*i
            else:
                return (2*i)+1

    def getMaxChildIndex(self,i):
        if 2*i>self.size:
            return None

        if (2*i)+1>self.size:
            return 2*i
        else:
            if self.heap[2*i]>self.heap[(2*i)+1]:
                return 2*i
            else:
                return (2*i)+1

    def percolateDown(self,i):
        while 2*i<=self.size:
            min=self.getMaxChildIndex(i)
            if(self.heap[i]<self.heap[min]):
                temp=self.heap[i]
                self.heap[i]=self.heap[min]
                self.heap[min]=temp
            i=min

    def percolateUp(self,i):
        while i//2>0:
            if(self.heap[i]>self.heap[i//2]):
                temp=self.heap[i]
                self.heap[i]=self.heap[i//2]
                self.heap[i//2]=temp
            i=i//2
    def insertElement(self,element):
        self.heap.append(element)
        self.size=self.size+1
        self.percolateUp(self.size)
    def printHeap(self):
        print self.heap


    #build the heap given the array
    def build_heap(self,array):
         len_of_array=len(array)
         index=len_of_array//2
         self.heap=[0]+array[:]
         self.size=len_of_array#for zero
         while index>0:
             self.percolateDown(index)
             index=index-1





if __name__=="__main__":
    queue=Heap()
    """
    queue.insertElement(1)
    queue.insertElement(13)

    queue.insertElement(5)

    queue.insertElement(17)

    queue.insertElement(6)

    queue.insertElement(4)
    queue.insertElement(2)

    queue.insertElement(100)

    queue.insertElement(5)
    """

    a=[2,4,3,1,17,1,322,43]
    queue.build_heap(a)
    queue.printHeap()

