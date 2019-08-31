n = int(input())
rb = list(map(int, input().rstrip().split()))
c=[]
for i in range(n):
    d = rb.count(rb[i])
    c.append(d)
g = max(c)
print(g)
