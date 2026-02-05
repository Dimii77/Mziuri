#1
with open("text.txt", "w", encoding="utf-8") as f:
    f.write("i dont like jews")

#2
print("----#2----")
with open("text.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
    raodenoba = len(content)
    print(raodenoba)

#3
with open("text.txt", "a", encoding="utf-8") as f:
    f.write("\n i love nuttela")

#4
with open("pirveli.txt", "r", encoding="utf-8") as f1:
    contenti = f1.read()
with open("meore.txt", "w", encoding="utf-8") as f2:
    f2.write(contenti)

#5
with open("file1.txt", "r", encoding="utf-8") as f3,open("file2.txt", "r", encoding="utf-8") as f4:
    data1 = f3.read()
    data2 = f4.read()

with open("gaertianebuli.txt", "w", encoding="utf-8") as f5:
    data3 = f5.write(data1 + "\n" + data2)

#6
print("----#6----")
with open("file1.txt", "r", encoding="utf-8") as f6:
    text1 = f6.read()
    print(text1.upper())

#7
print("----#7----")
with open("file2.txt", "w", encoding="utf-8") as f7:
    while True:
        userinput = input("Enter a text. To end Enter 0: ")
        if userinput == "0":
            break
        f7.write(userinput + "\n"
print("Information has been saved in file2.txt")

#8
print("----#8----")
# i give up vro