firstLeg = float(input("What's the first leg of a triangle?: "))
secondLeg = float(input("What's the second leg of a triangle?: "))

hypotenuse = ((firstLeg ** 2 + secondLeg ** 2) ** 0.5)

print(f"""The hypotenuse is: {hypotenuse}""")