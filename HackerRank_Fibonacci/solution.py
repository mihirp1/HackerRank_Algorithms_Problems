cube = lambda x: x*x*x # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
     my_list = [0,1]
     for i in range(2,n):
         my_list.append(my_list[i-2] + my_list[i-1])
     return(my_list[0:n])



if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
