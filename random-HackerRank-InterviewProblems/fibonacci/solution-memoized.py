def fact(N):
    fac = {}
    if(N == 0):
        fac[0] = 1
        return 1
    if(N == 1):
        fac[1] = 1
        return 1
    if(N > 1):
        try:
            return fac[N]
        except KeyError:
            fac[N] = N * fact(N-1)
            return fac[N] 

if __name__ == '__main__':
                n = int(input().strip())
                ans = fact(n)
                print(ans)

