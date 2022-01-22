# com o mesmo resultado do exemplo 3.10

found = 0
for n in needles:
    if n in haystack:
        found += 1
print(found)