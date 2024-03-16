### Motion auto formula ###
# Question = input("Question: ")
print("For any empty value, just press enter.")
variable_storage = list(map(input("Enter all variable here: ").split(",")))
s = float(input("Enter distance: "))
x1,y1 = float(input("Enter point 1:"))
x2,y2 = float(input("Enter point 2:"))
v0 = float(input("Enter velocity before acceleration: "))
v = float(input("Enter velocity after acceleration: "))
a = float(input("Enter acceleration: "))
t = float(input("Enter time: "))
def no_s():
    v = v0 + a * t
    formula = "v = v0 + a * t"
    return formula
def no_v():
    s = (v + v0)/2 * t
    formula = "s = (v + v0)/2 * t"
    return formula
def no_v_v0():
    s = v * t
    formula = "s = v * t"
    return formula
def no_t():
    v**2  = v0**2 + 2 * a * s
    formula = "v**2  = v0**2 + 2 * a * s"
    return formula
def no_v0():
    s = v * t - (1/2) * a * t**2
    formula = "s = v * t - (1/2) * a * t**2"
    return formula
if s == "":
    no_s()
elif v == "":
    no_v()
    if v0=="":
        no_v_v0()
elif v0 == "":
    no_v0()
elif t == "":
    no_t()

# print(f"Distance is {}")
# print(f"Initial velocity is {}")
# print(f"Final velocity is {}")
# print(f"Time is {}")
# print(f"Acceleration is {}")

