def fact(N):
    prod = 1
    for i in range(2 , N+1):
        prod *= i
    return prod

if __name__ == '__main__':
                n = int(input().strip())
                ans = fact(n)
                print(ans)
