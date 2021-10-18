cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    sequence = [0,1]
    for i in range(2,n):
        next_sum = sequence[-2] + sequence[-1]
        sequence.append(next_sum)    
    return sequence

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))