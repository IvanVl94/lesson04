from Calculat import Calculator

print("start")

res = Calculator.sub( 3, 4)
assert res == -1


res = Calculator.sum(0,5.6, 4.3)
res = round(res, 7)
print(res)
assert res == 9.9

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5]
res = Calculator.avg(numbers)
assert res == 5

print("finish")