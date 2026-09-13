name = input("Enter your name: ")

with open(f"name.txt", "w") as file:
    file.write(name)

print("Name saved successfully.")