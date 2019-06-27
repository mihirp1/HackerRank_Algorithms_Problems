def fact(N):
    if(N == 0):
        return 1
    if(N == 1):
        return 1
    if(N > 1):
        return N * fact(N-1) 

if __name__ == '__main__':
                n = int(input().strip())
                ans = fact(n)
                print(ans)

