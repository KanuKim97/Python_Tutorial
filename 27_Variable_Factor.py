# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#    print("이름: {0}\t 나이: {1}\t".format(name, age), end=" ")
#    print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름: {0}\t 나이: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile("mike", 20, "한국어", "영어", "스페인어", "중국어", "일본어")
profile("mike2", 22, "한국어", "영어", "", "", "")
