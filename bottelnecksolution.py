n = int(input())
rb = list(map(int, input().rstrip().split()))
for i in range(8):
    for j in range(8):
        if( rb[i] < rb[j] ):
            rb.pop(i)
p=len(rb)
for i in range(p):
    print(rb[i])

