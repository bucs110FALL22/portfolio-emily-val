import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 3
cost_per_class = cost_per_week/classes_per_week
print("Each class will be $", cost_per_class, ":)")
print(weeks, type(weeks))
print(classes, type(classes))
print(tuition, type(tuition))
print(classes_per_week, type(classes_per_week))
print(cost_per_week, type(cost_per_week))
#Part B
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
random_color = random.choice(colors)
print(random_color)

