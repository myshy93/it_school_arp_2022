import pickle
from extra import User, Role

with open("users", "rb") as fi:
    # unpickle
    obj1 = pickle.load(fi)

print(obj1.roles)