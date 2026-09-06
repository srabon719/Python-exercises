length = float(input("Enter the length of the zander in centimeters: "))

if length < 42:
    difference = 42 - length
    print("Release the fish back into the lake.")
    print("The fish is", difference, "centimeters below the size limit.")
else:
    print("The zander meets the size limit.")