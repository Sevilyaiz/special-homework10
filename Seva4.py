name = "Alla"
is_palindrome = name.lower() == name[::-1].lower()
print(is_palindrome)

for i in range(1,10):
    for s in range(1,10):
        print(f'{i * s}*5', end='')
        print()