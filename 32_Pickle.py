import pickle
"""
profile_pickle = open("profile.pickle", "wb")
profile = {"이름": "김건우", "나이": 20, "취미": ["축구", "농구", "배구"]}
print(profile)
pickle.dump(profile, profile_pickle)
profile_pickle.close()
"""

profile_pickle = open("profile.pickle", "rb")
profile = pickle.load(profile_pickle)
print(profile)
profile_pickle.close()
