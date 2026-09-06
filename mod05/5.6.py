import random

total_points = int(input("Enter the number of random points: "))

points_inside_circle = 0
points_generated = 0

while points_generated < total_points:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x * x + y * y < 1:
        points_inside_circle = points_inside_circle + 1

    points_generated = points_generated + 1

pi = 4 * points_inside_circle / total_points

print("Approximation of pi:", pi)