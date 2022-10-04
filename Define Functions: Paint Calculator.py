def paint_calculator():
    test_h = int(input("Height of wall: "))
    test_w = int(input("Width of wall: "))
    coverage = 5
    total_wall = test_h * test_w
    paint_needed = total_wall/coverage
    rounded_paint = round(paint_needed)
    print(f"You'll need {rounded_paint} cans of paint.")


paint_calculator()