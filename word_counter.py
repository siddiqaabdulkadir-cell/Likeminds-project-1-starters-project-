# Word Counter by Aisha Abdulkadir

text = input("Enter a sentence: ")

# Split the text into words
words = text.split()

# Count how many words
word_count = len(words)

print("\nTotal words:", word_count)

# Create a dictionary to store frequency of each word
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("\nWord frequency:")
for word, count in frequency.items():
    print(word, ":", count)