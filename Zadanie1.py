for i in range(500, 3001):
    if i % 7 == 0 and i % 5 != 0:
        print(str(i))

result = "".join(str(i) for i in range(500, 3001) if i % 7 == 0 and i % 5 != 0)
print(result)
print(result.count(str(21)))
result.replace('21', 'XX')
