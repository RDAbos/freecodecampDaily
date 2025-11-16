#Given two positive integers representing the width and height of a rectangle, determine how many rectangles can fit in the given one.

#Only count rectangles with integer width and height.
#For example, given 1 and 3, return 6. Three 1x1 rectangles, two 1x2 rectangles, and one 1x3 rectangle.
def count_rectangles(width, height):
    return (width * (width + 1) // 2) * (height * (height + 1) // 2)

w = int(input("Enter width: "))
h = int(input("Enter height: "))

print("Number of rectangles:", count_rectangles(w, h))
