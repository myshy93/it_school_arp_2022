import pickle
from datetime import datetime

class Role:

    def __init__(self, name) -> None:
        self.name = name

class User:

    def __init__(self) -> None:
        self.name = "Test"
        self.creation_date = datetime.now()
        self.roles = [Role("admin"), Role("worker")]
    
if __name__ == "__main__":
    u1 = User()
    with open("users", "wb") as fout:
        # pickle
        pickle.dump(u1, fout)