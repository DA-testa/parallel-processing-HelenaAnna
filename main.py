# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
   a =[(0, j) for i in range(n)]

   for i, t in enumerate(data):
    min_laiks = float("inf")
    min_a = -1

    for s, (laiks, _) in enumerate (a):
        if laiks < min_laiks:
            min_laiks = laiks
            min_t = t

    output.append((a[min_t][1], min_laiks))
    a[min_t] = (min_laiks + t, a[min_t][1])
    
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    #n = 0
    #m = 0
    n, m = map(int, input().split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n, m, data)
    
    # TODO: print out the results, each pair in it's own line
    for p, time in result:
        print(p, time)


if __name__ == "__main__":
    main()
