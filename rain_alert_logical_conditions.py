# Rain Alert System

humidity = int(input("Enter humidity (0-100): "))
cloud = int(input("Enter cloud level (0-100): "))

if humidity > 75 and cloud > 70:
    print("🌧️ High chance of rain!")
    print("☔ Carry an umbrella.")
elif humidity > 60:
    print("🌦️ Possible rain.")
else:
    print("☀️ Low chance of rain.")
