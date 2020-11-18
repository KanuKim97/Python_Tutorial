# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#    print("이름: {0}\t 나이: {1}\t".format(name, age), end=" ")
#    print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름: {0}\t 나이: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile("김건우", 20, "한국어", "영어", "스페인어", "중국어", "일본어")
profile("김건우2", 22, "한국어", "영어", "", "", "")
