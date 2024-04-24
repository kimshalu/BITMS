file = open("example.txt", "w")#writes
file.write("Hello, World!\nThis is a test file.\n")
file.close()

file = open("example.txt", "r")#reads
content = file.read()
print("File Content:")
print(content)
file.close()

print(file.mode)#mode of file

file = open("example.txt", "r")#readline
line1 = file.readline()
print("\nFirst Line:")
print(line1)
file.seek(0)
print("\nRemaining Lines:")
remaining_lines = file.readlines()#readlines
for line in remaining_lines:
    print(line.strip())
file.close()

file = open("example.txt", "a")#appends
file.write("\nAppending new content.")
file.close()
