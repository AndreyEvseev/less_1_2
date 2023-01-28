number_mistakes = 0
for x in 1, 0:
    for y in 1, 0:
        for z in 1, 0:
            result = not(x or y or z) == (not x and not y and not z)
            print(f'{x = }; {y = }; {z = };  result: {result}')
            if result == False:
                number_mistakes += 1
if number_mistakes == 0:
    identity = True
else:
    identity = False
print(f'{identity = }')
