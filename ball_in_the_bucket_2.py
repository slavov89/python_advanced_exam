def read_matrix():
    matrixf = []
    for _ in range(6):
        matrixf.append(input().split(" "))
    return matrixf


def calculate_bucket(matrixf, colf):
    point = 0
    for i in range(6):
        if matrixf[i][colf] != "B":
            point += int(matrixf[i][colf])
    return point


matrix = read_matrix()
points = 0
for _ in range(3):
    throw = list(input())
    if len(throw) <= 6:
        row, col = int(throw[1]), int(throw[4])
        if row > 5 or col > 5:
            continue
    else:
        continue
    if matrix[row][col] == "B":
        points += calculate_bucket(matrix, col)
        matrix[row][col] = "0"

if points < 100:
    print(f"Sorry! You need {100-points} points more to win a prize.")
elif 100 <= points <= 199:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif 200 <= points <= 299:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
elif 300 <= points:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")
