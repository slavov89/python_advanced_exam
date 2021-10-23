from collections import deque

materials = [int(x) for x in input().split(" ")]  # last integer of materials
magic_levels = deque([int(x) for x in input().split(" ")])  # first magic level value
gemstone, porcelain, gold, diamond = 0, 0, 0, 0
while materials and magic_levels:  # Stop crafting gifts when you are out of materials or magic level.
    product = materials[-1] + magic_levels[0]
    if 100 <= product <= 499:
        if 100 <= product <= 199:
            gemstone += 1
            materials.pop()
            magic_levels.popleft()
        elif 200 <= product <= 299:
            porcelain += 1
            materials.pop()
            magic_levels.popleft()
        elif 300 <= product <= 399:
            gold += 1
            materials.pop()
            magic_levels.popleft()
        elif 400 <= product <= 499:
            diamond += 1
            materials.pop()
            magic_levels.popleft()
        continue
    elif product < 100:
        if product % 2 == 0:  # even number, double the materials, and triple the magic, then sum it again.
            product = materials[-1]*2 + magic_levels[0]*3
        else:  # odd number, double the sum of the materials and the magic level.
            product = 2* materials[-1] + 2* magic_levels[0]
        if 100 <= product <= 199:
            gemstone += 1
            materials.pop()
            magic_levels.popleft()
        elif 200 <= product <= 299:
            porcelain += 1
            materials.pop()
            magic_levels.popleft()
        elif 300 <= product <= 399:
            gold += 1
            materials.pop()
            magic_levels.popleft()
        elif 400 <= product <= 499:
            diamond += 1
            materials.pop()
            magic_levels.popleft()
        else:  # if neither
            materials.pop()
            magic_levels.popleft()
            continue
    elif 499 < product:  # If the product of the operation is more than 499
        product /= 2
        if 100 <= product <= 199:
            gemstone += 1
            materials.pop()
            magic_levels.popleft()
        elif 200 <= product <= 299:
            porcelain += 1
            materials.pop()
            magic_levels.popleft()
        elif 300 <= product <= 399:
            gold += 1
            materials.pop()
            magic_levels.popleft()
        elif 400 <= product <= 499:
            diamond += 1
            materials.pop()
            magic_levels.popleft()
        else:
            materials.pop()
            magic_levels.popleft()
            continue

# If, however, the result is not between or equal to any of the numbers in the table above after performing the calculation, remove both the materials and the magic level.

# You have succeeded in crafting the presents when you've
# crafted either one of
# the pairs - a gemstone and a sculpture or gold and jewellery.

if gemstone >= 1 and porcelain >= 1:
    print("The wedding presents are made!")
elif gold >= 1 and diamond >= 1:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
elif magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

if diamond > 0:
    print(f"Diamond Jewellery: {diamond}")
if gold > 0:
    print(f"Gold: {gold}")
if gemstone > 0:
    print(f"Gemstone: {gemstone}")
if porcelain > 0:
    print(f"Porcelain Sculpture: {porcelain}")

