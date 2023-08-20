import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon

circle_lst = []
polygon_lst = []


def integer_points_in_circle(center, radius):
    x, y = center
    points = []
    for i in range(int(x - radius), int(x + radius) + 1):
        for j in range(int(y - radius), int(y + radius) + 1):
            if (i - x) ** 2 + (j - y) ** 2 < radius ** 2:
                points.append((i, j))
    return points


def integer_points_in_polygon(polygon_):
    x_min, y_min, x_max, y_max = polygon_.bounds
    points = []
    for i in range(int(x_min), int(x_max) + 1):
        for j in range(int(y_min), int(y_max) + 1):
            point = Point(i, j)
            if point.within(polygon_):
                points.append((i, j))
    return points


def intersections():
    if not polygon_lst:
        points = set.intersection(*[set(circle) for circle in circle_lst])
    elif not circle_lst:
        points = set.intersection(*[set(poly) for poly in polygon_lst])
    else:
        circle_points = set.intersection(*[set(circle) for circle in circle_lst])
        polygon_points = set.intersection(*[set(poly) for poly in polygon_lst])
        points = circle_points.intersection(polygon_points)
    return points


def polygon(ax, shape_code, coords):
    if shape_code == 'c' or shape_code == 'C':
        r = int(input("Enter the radius : "))
        circle_lst.append(integer_points_in_circle(coords, r))
        circle = plt.Circle(coords, r, fill=False, ec="red")
        ax.add_patch(circle)
    else:
        coords.append(coords[0])
        xs, ys = zip(*coords)
        polygon1 = Polygon(coords)
        polygon_lst.append(integer_points_in_polygon(polygon1))
        ax.plot(xs, ys)


def coordinates():
    n = int(input("Enter the number of vertices for the polygon: "))
    vertices = []
    for i in range(n):
        x, y = map(int, input(f"Enter the coordinates for vertex {i + 1}: ").split(','))
        vertices.append((x, y))
    return vertices


def inputs():
    print(
        "SHAPE CODE : \nR : Rectangle \nT : Triangle\nC : Circle\nP : Polygon\nNOTE : The axis limits are from -10 to "
        "10")
    lims = (-10, 10)
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(1, 1, 1)
    plt.ylim(lims)
    plt.xlim(lims)
    n = int(input("Enter number of shapes: "))
    while n != 0:
        c = input("Enter the shape code: ")
        if c == 'c' or c == 'C':
            coords = input("Enter the center of range as two comma-separated values: ")
            coords = tuple(map(int, coords.strip().split(',')))
            polygon(ax1, c, coords)
        else:
            coords = coordinates()
            polygon(ax1, c, coords)
        n -= 1
    result = intersections()

    if result == set():
        print("No intersection points")
    else:
        print("Intersection points : ", result)
    return plt.show()


inputs()
