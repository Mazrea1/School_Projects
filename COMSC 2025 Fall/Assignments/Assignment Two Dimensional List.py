import random
# Create a 2D list (matrix) with random integers

def randomNumber():
    return random.randint(1, 10)

matA = [[randomNumber() for x in range(10)] for y in range(10)]
matB = [[randomNumber() for x in range(10)] for y in range(10)]

matC = matA + matB

print(matC)