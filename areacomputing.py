sq1st1 = int(input("Enter the length of the first object: "))
sq1st2 = int(input("Enter the width of the first object: "))
sq1area = sq1st1*sq1st2

print(f"The area of the first object is {sq1area} sq. units")

sq2st1 = int(input("\nEnter the length of the second object: "))
sq2st2 = int(input("Enter the width of the second object: "))
sq2area = sq2st1*sq2st2
print(f"The area of the second object is {sq2area} sq. units")

if sq1area == sq2area:
    print("\nThe area difference of these two objects are 0 sq units.")

if sq1area > sq2area:
    print("\nThe area difference of these two objects are", (sq1area - sq2area), "sq. units")

if sq1area < sq2area:
    print("\nThe area difference of these two objects are", (sq2area - sq1area), "sq. units")
