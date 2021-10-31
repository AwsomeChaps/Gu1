def shape(n):
    for i in range(2*n+ 1):
        if (i <= n):
            print(" " * (n - i) + "*" * 2 * i + " " * (n - i))
            
    for i in range(n-1):
        if n > 2:
            if ((n/3))<=(i):
                for x in range(i):
                    print("*" * (n - i) + " " * 2 * i + "*" * (n - i))
                break
            else:
                print("*" * 2 * n)
        else:
                print("*" * 2 * n)
        
            
shape(10)