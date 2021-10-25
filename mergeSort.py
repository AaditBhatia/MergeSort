#Recursively Partition key into smaller and smaller buckets
#Till buckets are small enough to be sorted on-chip memory.
#Counting sort, Local Sort- brings all keys of small buckets into sorted order
#produces sequence of 2^d sub-buckets. create 2^8 buckets 
#Each buckets contains a partition of keys that share same value on their most significant digit

def partition(self, key):
    newArr=[None]*len(key)+1
    tempArr=[None]*len(key)+1
    j=0
    for i in range (0,len(key)):
        j=0
        while(j!=len(key)):
            if key[i]%10 < newArr[j]:
                tempArr[:j]=newArr[:j]
                tempArr[j]=key[i]
                tempArr[j+1:]=newArr[j+1:]
                newArr=tempArr



     