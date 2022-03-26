courses: dict[int, str] = dict()
courses[110] = "Intro to Programming"
courses[210] = "Data Structures"

print(courses[110])

points: dict[str, int] = {"Kris": 0, "Kaki": 10}

points["Kaki"] += 100

print(points)

schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")