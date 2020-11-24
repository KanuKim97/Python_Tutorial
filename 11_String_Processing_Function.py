sentence = "hi my name is mike"
print(sentence.upper())

sentence2 = "HI MY NAME IS MIKE"
print(sentence2.lower())

print(sentence[0].isupper())
print(sentence2[0].islower())

print(len(sentence))
print(len(sentence2))

print(sentence.replace("hi", "Bye"))

index = sentence.index("m")
print(index)

index = sentence.index("k", index + 1)
print(index)

print(sentence.find("mi"))
print(sentence.find("kim"))

print(sentence.count("i"))