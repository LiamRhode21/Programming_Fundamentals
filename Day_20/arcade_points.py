def calculate_points(*scores):
    points = 0
    for score in scores:
        points += score
    print(points)

calculate_points(10, 25, 15)
calculate_points(100, 50)
calculate_points()