first_letter = ord(input('First letter: '))
second_letter = ord(input('Second letter: '))

print(f'First letter position: {first_letter - ord("a") + 1}, second letter position: {second_letter - ord("a") + 1}')
print(f'{(second_letter - ord("a") + 1) - (first_letter - ord("a") + 1)} letters in between')
