if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    #The stratedy used is to convert the array into a ser so thata we have
    #one element of each.
    ListWithoutDuplicates = list(set(arr))
    OrderedListWithoutDuplicates = ListWithoutDuplicates.sort(reverse=True)
    print(OrderedListWithoutDuplicates[1])
