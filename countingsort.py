def countingsort(l):
    tamanho = len(l)
    output = [0] * tamanho
    count = [0] * 10
    for i in range(0, tamanho):
        count[l[i]] += 1
    for j in range(1,10):
        count[j] += count[j-1]
    a = tamanho -1
    
    while a >= 0:
        output[count[l[a]]-1] = l[a]
        count[l[a]] -= 1
        a -= 1

    for k in range(0, tamanho):
        l[k] = output[k]

l1 = [2,5,8,1,5,3]
countingsort(l1)
print(l1)