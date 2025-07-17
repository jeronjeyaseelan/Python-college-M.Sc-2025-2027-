import math

def rectangular_to_polar(x, y):
    """Convert rectangular (x,y) coordinates to polar (r,θ) coordinates"""
    r = math.sqrt(x**2 + y**2)
    theta = math.atan2(y, x)
    # Convert theta to degrees
    theta_deg = math.degrees(theta)
    return r, theta_deg

def polar_to_rectangular(r, theta_deg):
    """Convert polar (r,θ) coordinates to rectangular (x,y) coordinates"""
    # Convert theta to radians
    theta = math.radians(theta_deg)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    return x, y

def main():
    while True:
        print("\n1. Rectangular to Polar")
        print("2. Polar to Rectangular")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            x = float(input("Enter x coordinate: "))
            y = float(input("Enter y coordinate: "))
            r, theta = rectangular_to_polar(x, y)
            print(f"Polar coordinates: r = {r:.2f}, θ = {theta:.2f}°")

        elif choice == '2':
            r = float(input("Enter r value: "))
            theta = float(input("Enter θ in degrees: "))
            x, y = polar_to_rectangular(r, theta)
            print(f"Rectangular coordinates: x = {x:.2f}, y = {y:.2f}")

        elif choice == '3':
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
