file = open('Music.txt', 'r')
print(file.read(12))
file.close()
file = open('Music.txt', 'r')
print(file.readline())
print(file.readline())
print(file.readline())
file.close()
file = open('Music.txt', 'r')
print(file.readlines())
file.close()
file = open('Music.txt', 'r')
for x in file:
    print(x)
file.close()