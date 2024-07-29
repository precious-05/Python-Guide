# Open the file in read mode
with open("htmll.txt", "r") as file:
    count = 0

    # Read the lines from the file
    for line in file:
        # Convert the line to lowercase to ensure case insensitivity
        line = line.lower()
        # Split the line into words
        words = line.split()
        # Count occurrences of the word "the" in the line
        count += words.count("the")

# Display the total count of the word "the"
print(f"Total number of occurrences of 'the' is {count}")
