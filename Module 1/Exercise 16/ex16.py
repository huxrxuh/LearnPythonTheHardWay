#Reading and writing files

filename = "test.txt"

print(f"We're goin to erase the {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

s = "Now I'm going to ask you for three lines"
print(s)

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

s = "I'm going to write these to the file."
print(s)

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

s = "And finally, we close it."
print(s)

target.close()

