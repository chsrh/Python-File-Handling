#Read the entire text
f = open("architecture.txt", 'r', encoding='utf-8')
text = f.read()
print(text)
f.close()

#Read the first n lines
n = 3
with open("architecture.txt", 'r', encoding='utf-8') as f:
    for i in range(n):
        line = f.readline()
        print(line)

#Read the last n lines
n = 3
with open("architecture.txt", 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()
    last_n_lines = lines[-n:]
    for line in last_n_lines:
        print(line)

#Count the number of words
with open("architecture.txt", 'r', encoding='utf-8') as f:
    text = f.read()
    words = text.split()
    print("The number of words in the file is:", len(words))

