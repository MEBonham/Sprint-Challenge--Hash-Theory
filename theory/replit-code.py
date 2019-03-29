
print("A    B    result")
for a in range(2):
    for b in range(2):
        result = a or not b
        print(f'{a}    {b}    {result}')
print()
print("A    B    result")
for a in range(2):
    for b in range(2):
        result = (not a or b) and not (a and not b)
        print(f'{a}    {b}    {result}')
print()
print("A    B    C    result")
for a in range(2):
    for b in range(2):
        for c in range(2):
            result = not (a or b) or ((a or c) and not (b or not c))
            print(f'{a}    {b}    {c}    {result}')