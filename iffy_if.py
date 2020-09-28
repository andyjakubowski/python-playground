age = int(input("Gimme your age:\n"))

if age < 0:
    print("Are you telling me you haven’t been born yet?")
elif age == 0 or age == 1 or age == 2:
    print("You’re such a baby.")
elif age > 2 and age <= 30:
    print("You are thirty or below.")
elif age > 30 and age < 100:
    print("You are over thirty, and under a hundred.")
else:
    print("You are so wise!")
