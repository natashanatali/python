# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while

n = int(input())
sum = 1

while n > 0:
     sum = sum * n
     n = n - 1
# print(sum)

print(sum)
 