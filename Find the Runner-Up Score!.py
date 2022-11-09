if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    listaSinRepetir = list(set(arr))
    listaSinRepetir.sort(reverse=True)
    print(listaSinRepetir[1])
