
"""
С клавиатуры вводится два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц, B,C,D,E заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное заполнение, а целенаправленное.

Вариант №20:
Формируется матрица F следующим образом: если в Е количество чисел, больших К в четных столбцах в области 1 больше, чем произведение чисел в нечетных строках в области 4, то поменять в Е симметрично области 2 и 3 местами, иначе С и В поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение: (К*(A*F))* F T. Выводятся по мере формирования А, F и все матричные операции последовательно.
"""
from random import randint as rnd
def printMtrx(mtrxA):
  for i in range(len(mtrxA)):
    for j in range(len(mtrxA[i])):
      print(mtrxA[i][j], end = " ")
    print()
def multipliMtrx(mtrxA, mtrxB):
  mtrxC = []
  for i in range(len(mtrxA)):
    mtrxC.append([])
    for j in range(len(mtrxA)):
        s = 0
        for n in range(len(mtrxA)):
             s += mtrxA[i][n]*mtrxB[j][n]
        mtrxC[i].append(s)
  return mtrxC
def multipliNum(mtrxA, num):
  mtrxC = mtrxA
  for i in range(len(mtrxA)):
    for j in range(len(mtrxA[i])):
      mtrxC[i][j] = mtrxA[i][j]*num
  return mtrxC
def transposition(mtrxA):
  mtrxC = mtrxA
  for i in range(len(mtrxA)):
    for j in range(len(mtrxA[i])):
      mtrxC[i][j] = mtrxA[j][i]
  return mtrxC

#Основной код
n = int(input("Введите число N: "))
k = int(input("Введите число K: "))
m = n//2
n = m*2
mtrxA = []
fileName = "text.txt"
nums = []
with open(fileName, encoding="utf-8") as f:
    for i, line in enumerate(f):
        if i >= n*n:
            break
        nums.append(int(line.rstrip()))
for i in range(n):
    row = []
    for j in range(n):
        row.append(nums[i*n+j])
    mtrxA.append(row)

b = []
c = []
d = []
e = []
for i in range(m):
    b.append([])
    c.append([])
    d.append([])
    e.append([])
    for j in range(m):
        b[i].append(mtrxA[i+m][j+m])
        c[i].append(mtrxA[i+m][j])
        d[i].append(mtrxA[i][j])
        e[i].append(mtrxA[i][j+m])

s = 0
for i in range(m//2):
    for j in range(m-i-1,m):
        if j % 2 != 0: continue
        if e[i][j] > k: s += 1
for i in range(m//2, m):
    for j in range(i,m):
        if j % 2 != 0: continue
        if e[i][j] > k: s += 1

t = 1
for i in range(m):
  if i % 2 ==0: continue
  for j in range(m):
    if j>i and i<m+1-j:
      t *= e[i][j]

if s > t:
  print("The number of numbers is greater than the product")
  for i in range(0, m):
        for j in range(0,m-i):
            e[i][j], e[m-j-1][m-i-1] = e[m-j-1][m-i-1],e[i][j]
else:
  print("The product is greater than the number of numbers")
  for i in range(m):
        for j in range(m):
            c[i][j], b[i][j] = b[i][j], c[i][j]

f = []
f.extend(d)
f.extend(c)
for i in range(m):
    f[i].extend(e[i])
for i in range(m, n):
    f[i].extend(b[i-m])

print("Matrix A: ")
printMtrx(mtrxA)
print("--------------")
print("Matrix F: ")
printMtrx(f)
print("--------------")
af = multipliMtrx(mtrxA, f)
print("Matrix A multiplied to Matrix F :")
printMtrx(af)
print("--------------")
afk = multipliNum(af, k)
print("Matrix AF multiplied to K :")
printMtrx(afk)
print("--------------")
ft = transposition(f)
print("Matrix F transposed : ")
printMtrx(ft)
print("--------------")
res = multipliMtrx(afk, ft)
print("(K*(A*F))*Ft")
printMtrx(res)
