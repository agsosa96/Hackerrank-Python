# The included code stub will read an integer, n, from STDIN.

# Without using any string methods, try to print the following:
# 123...n

# Note that "" represents the consecutive values in between.


if __name__ == '__main__':
    suma = ''
    n = int(input())
    
    for i in range(n):
        suma = suma + str(i+1)
        
print(suma)
