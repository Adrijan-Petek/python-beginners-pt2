# file_example.py

"""
📄 Tutorial 2: Reading and Writing Files in Python
This script teaches beginners how to create, write, append, and read files.
"""

# Create a new text file and write initial lines
with open("greetings.txt", "w") as f:
    f.write("Hello, Crypto Mobb learners!\n")
    f.write("This is your first text file.\n")

# Append additional lines using a loop
with open("greetings.txt", "a") as f:
    for i in range(1, 6):
        f.write(f"Line {i}: Keep learning Python!\n")

# Read and display file content
print("📂 Contents of greetings.txt:")
with open("greetings.txt", "r") as f:
    content = f.read()
    print(content)

# Optional: count number of lines
line_count = len(content.splitlines())
print(f"📝 Total lines in greetings.txt: {line_count}")
