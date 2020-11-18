'''
def profile(name, age, main_lang):
    print("이름: {0}\t 나이: {1}\t 언어: {2}".format(name, age, main_lang))
'''

def profile(name, age = 17, main_lang = "Korean"):
    print("이름: {0}\t 나이: {1}\t 언어: {2}".format(name, age, main_lang))

profile("김건우")
