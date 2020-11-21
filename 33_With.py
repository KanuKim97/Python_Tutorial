"""
import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))
"""

"""
with open("a.txt", "w", encoding="utf-8") as a_files:
    a_files.write("ㅎㅇ")
"""

with open("a.txt", "r", encoding="utf-8") as a_files:
    print(a_files.read())
