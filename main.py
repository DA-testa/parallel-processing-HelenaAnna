# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    Nakamaisthread = 0
    laiks = [0] * n
    row = [(0, i) for i in range (n)]


    for i in range(m):
        darits = data[i]
        #thread = Nakamaisthread
        s, a = row[Nakamaisthread]
        output.append((s, a))
        s = max(s, laiks[a]) + darits
        laiks[a] = s
        row[Nakamaisthread] = (s, a)
        Nakamaisthread = (Nakamaisthread + 1) % n

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
