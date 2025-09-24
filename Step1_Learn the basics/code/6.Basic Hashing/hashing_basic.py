# Python3 program to count frequencies of
# elements in an array using Hashing
# Time Complexity : O(n)
# Space Complexity : O(n)

def countFreq(arr, n):
    ht = {}
    for i in range(n):
        if arr[i] in ht:
            ht[arr[i]] += 1
        else:
            ht[arr[i]] = 1
    for key, value in ht.items():
        print(key, value)



    
# Find the highest/lowest frequency element

def hashing_func(arr):
    ht = {}
    for i in range(len(arr)):
        if arr[i] in ht:
            ht[arr[i]] += 1
        else:
            ht[arr[i]] = 1
    return ht

def sum_highest_frequency(arr):
    ht = hashing_func(arr)
    maxv = max(ht.values())
    sum_max_freq = sum(mx for mx in ht.values() if mx==maxv)
    return sum_max_freq
    
def sum_lowest_frequency(arr):
    ht = hashing_func(arr)
    minv = min(ht.values())
    sum_min_freq = sum(mn for mn in ht.values() if mn == minv)
    return sum_min_freq


if __name__ == "__main__":
    arr = [10,5,10,15,10,5,5]
    n = len(arr)
    # countFreq(arr, n)
    # sum_highest_frequency(arr)
    # sum_lowest_frequency(arr)
    
    
    