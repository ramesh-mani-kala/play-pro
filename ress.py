# Square pattern
def square_pattern(n):
    for i in range(n):
        print('* ' * n)

# Right triangle pattern
def right_triangle_pattern(n):
    for i in range(1, n + 1):
        print('* ' * i)

# Inverted right triangle pattern
def inverted_right_triangle_pattern(n):
    for i in range(n, 0, -1):
        print('* ' * i)

# Full pyramid pattern
def full_pyramid_pattern(n):
    for i in range(1, n + 1):
        print('  ' * (n - i) + '* ' * (2 * i - 1))

# Inverted full pyramid pattern
def inverted_full_pyramid_pattern(n):
    for i in range(n, 0, -1):
         print('  ' * (n - i) + '* ' * (2 * i - 1))

# Hollow square pattern
def hollow_square_pattern(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print('* ' * n)
        else:
            print('* ' + '  ' * (n - 2) + '*')

#Diamond pattern
def diamond_pattern(n):
    for i in range(1, n + 1):
        print('  ' * (n - i) + '* ' * (2 * i - 1))
    for i in range(n - 1, 0, -1):
        print('  ' * (n - i) + '* ' * (2 * i - 1))

# Hourglass Pattern
def hourglass_pattern(n):
    for i in range(n, 0, -1):
        print('  ' * (n - i) + '* ' * (2 * i - 1))
    for i in range(2, n + 1):
        print('  ' * (n - i) + '* ' * (2 * i - 1))
        
# Example usage:
square_pattern(5)
print()
right_triangle_pattern(5)
print()
inverted_right_triangle_pattern(5)
print()
full_pyramid_pattern(5)
print()
inverted_full_pyramid_pattern(5)
print()
hollow_square_pattern(5)
print()
diamond_pattern(5)
print()
hourglass_pattern(5)