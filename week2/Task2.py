s1 = "hello123world45"

total = 0

for character in s1:
    if character.isdigit():
        total += int(character)


print(total)

count = 0

for character in s1:
    if character.isdigit():
        count += 1 

average = total / count

print(average)