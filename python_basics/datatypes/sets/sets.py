# Sets are stored into random memory locations - there is no order. which means sets are retrieved in random order.
# You cannot duplicate values in a set

lecturers = {"Jake", "Kyle"}
lecturers20 = {"Cassius", "Kyle"}

lecturers.add("Cassius")
lecturers.add("Warren")
lecturers.add("Neville")
lecturers.remove("Warren")

print(lecturers)

# Union set
lecturersU = lecturers.union(lecturers20)

# intersection set
lecturersI = lecturers.intersection(lecturers20)

print("\n")

print(lecturers)

print(f"Union set " + str(lecturersU))
print(f"Intersect set " + str(lecturersI))



