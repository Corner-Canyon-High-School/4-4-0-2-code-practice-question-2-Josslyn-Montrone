red = int(input("Input the red: "))
green = int(input("Input the green: "))
blue = int(input("Input the blue: "))
if red >= 0 and red <= 255 and green >= 0 and green <= 255 and blue >= 0 and blue <= 255:
    print("No problems")
elif red < 0 or red > 255:
    print("Red number is not correct.")
elif green < 0 or green > 255:
    print("Green number is not correct.")
elif blue < 0 or blue > 255:
    print("Blue number is not correct.")