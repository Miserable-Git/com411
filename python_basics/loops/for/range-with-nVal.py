
# execute code within the range at every nValue

# for index in range (start-val, end-val, nValue):

# Ask user for brightness level
print("What level of brightness is required?")
brightness_desired = int(input())

# Adjust brightness
print("\nAdjusting brightness...\n")

for brightness in range(2, brightness_desired + 1, 3):
    print(brightness)
    print(f"Beep's brightness level: {'*' * brightness}")
    print(f"Bop's brightness level: {'*' * brightness}")

print("Adjustments complete!")