sentence = "hi my name is geonwoo kim"
print(sentence.upper())

sentence2 = "HI MY NAME IS GEONWOO KIM"
print(sentence2.lower())

print(sentence[0].isupper())
print(sentence2[0].islower())

print(len(sentence))
print(len(sentence2))

print(sentence.replace("hi", "Bye"))

index = sentence.index("k")
print(index)

index = sentence.index("m", index + 1)
print(index)

print(sentence.find("kim"))
print(sentence.find("Han"))

print(sentence.count("i"))