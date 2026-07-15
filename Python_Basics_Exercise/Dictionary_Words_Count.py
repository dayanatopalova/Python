text = "I love Python I love coding"
words = text.split()
print(words)

counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)