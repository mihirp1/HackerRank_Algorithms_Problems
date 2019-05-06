
def OverCharge(n, ar):


    iter1=0
    value1=0

    truesum = 0
    truediff = 0
    annas_divided_contri = 0
    for iter1,value1 in enumerate(ar):
        if(iter1 != k):
             truesum = truesum + ar[iter1]
    annas_divided_contri = truesum//2
    
    
    truediff = paid - annas_divided_contri
    #print(paid - truediff)
    if(truediff == 0):
        print("Bon Appetit")
    else:
        print(paid - annas_divided_contri)
        
        






if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n = int (n)
    k = int (k)
    #n = n-1
    #k = k-1
    ar = list(map(int, input().strip().split(' ')))
    paid = int( input().strip())
    result = OverCharge(n, ar)
    #print(result)
