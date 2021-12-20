'''
The probe's x,y position starts at 0,0. Then, it will follow some trajectory by moving in steps. On each step, these changes occur in the following order:

- The probe's x position increases by its x velocity.
- The probe's y position increases by its y velocity.
- Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
- Due to gravity, the probe's y velocity decreases by 1.

# PART I
Find the initial velocity that causes the probe to reach the highest y position and still eventually be within the target area after any step. What is the highest y position it reaches on this trajectory?

# PART II
How many distinct initial velocity values cause the probe to be within the target area after any step?

'''
# target area: x=111..161, y=-154..-101

min_x, max_x, min_y, max_y = 111, 161, -154, -101

highest = 0
unique = 0
x_range = max(abs(min_x), abs(max_x))
y_range = max(abs(min_y), abs(max_y))

for y in range(-y_range, y_range + 1):
    for x in range(-x_range, x_range + 1):
        pos_x, pos_y = 0, 0
        vel_x, vel_y = x, y
        height = 0
        
        while pos_x <= max_x and pos_y >= min_y:
            pos_x += vel_x
            pos_y += vel_y
            vel_x -= (vel_x > 0) - (vel_x < 0)
            vel_y -= 1
            height = max(height, pos_y)
            if (min_x <= pos_x <= max_x and
                    min_y <= pos_y <= max_y):
                highest = max(highest, height)
                unique += 1
                break

print("Part 1:", highest)
print("Part 2:", unique)

