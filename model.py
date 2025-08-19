def version1_hardcoded():
    print("\n=== VERSION 1: HARDCODED ===")
    a, b, c = 0.5, -3, 28
    t = 5  # Example: 5th hour
    T = a * t**2 + b * t + c
    print(f"Predicted temperature at t={t}: {T:.2f}°C")


def version2_keyboard():
    print("\n=== VERSION 2: KEYBOARD INPUT ===")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    t = float(input("Enter time t (hour/day): "))
    T = a * t**2 + b * t + c
    print(f"Predicted temperature at t={t}: {T:.2f}°C")



def version3_file_single():
    print("\n=== VERSION 3: FILE INPUT (SINGLE SET) ===")
    with open("inputs_single.txt", "r") as f:
        lines = f.readlines()
    a = float(lines[0])
    b = float(lines[1])
    c = float(lines[2])
    t = float(lines[3])
    T = a * t**2 + b * t + c
    print(f"a={a}, b={b}, c={c}, t={t} -> Predicted Temp: {T:.2f}°C")




def version4_file_multiple():
    print("\n=== VERSION 4: FILE INPUT (MULTIPLE SETS) ===")
    with open("inputs_multiple.txt", "r") as f:
        for line in f:
            a, b, c, t = map(float, line.strip().split())
            T = a * t**2 + b * t + c
            print(f"a={a}, b={b}, c={c}, t={t} -> Predicted Temp: {T:.2f}°C")


a, b, c = -0.2, 1.5, 24 

def quadratic_weather_model(time):
    """Predict temperature using quadratic equation."""
    return a * (time ** 2) + b * time + c

def waterfall_mode():
    print("\n=== WATERFALL MODE ===")
    for hour in range(0, 25, 6):  # every 6 hours
        temp = quadratic_weather_model(hour)
        print(f"Time: {hour} hrs -> Predicted Temp: {temp:.2f}°C")


def iterative_mode():
    print("\n=== ITERATIVE MODE ===")
    for iteration in range(1, 4):
        print(f"Iteration {iteration}:")
        for hour in range(0, 25, 12):  # every 12 hours
            temp = quadratic_weather_model(hour)
            print(f"Time: {hour} hrs -> Temp: {temp:.2f}°C")
        print("---")


def agile_mode():
    print("\n=== AGILE MODE ===")
    times_to_check = [0, 6, 12, 18, 24]
    for sprint in range(1, 3):
        print(f"Sprint {sprint}:")
        for t in times_to_check:
            temp = quadratic_weather_model(t)
            print(f"Time: {t} hrs -> Temp: {temp:.2f}°C")
        print("---")


if __name__ == "__main__":
    
    version1_hardcoded()
    version2_keyboard()
    version3_file_single()
    version4_file_multiple()

    
    waterfall_mode()
    iterative_mode()
    agile_mode()
