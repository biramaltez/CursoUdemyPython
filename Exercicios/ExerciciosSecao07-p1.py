"""
# 1
A = [1, 0, 5, -2, -5, 7]
soma = A[0] + A[1] + A[5]
print(soma)
A[4] = 100
for x in A:
    print(x)

# 2
v = []
for x in range(6):
    v.append(int(input(f"Digite o número {x+1}: ")))
print("Números lidos: ", end=" ")
for x in v:
    print(x, end=" ")


"""
# 3
n, q = [], []
for x in range(10):
    n.append(float(input(f"Digite o número {x + 1}: ")))
for x in n:
    q.append(x**2)
print("Números lidos: ", end=" ")
for x in n:
    print(x, end=" ")
print("Quadrado dos números: ", end=" ")
for x in q:
    print(x, end=" ")
