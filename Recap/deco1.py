import random

def underlined(f):
    def inner(*args, **kwargs):
        t = f(*args, **kwargs)
        print(t)
        print("-" * len(t))
        return t
    return inner

@underlined
def get_token():
    """Variable length 9-20 chars."""
    k = random.randint(9, 20)
    return "".join(random.sample([chr(i) for i in range(65, 91)], k))

@underlined
def get_rev_name(name):
    return "".join(list(reversed(name)))


# TCIQDHGAJKFMENSZO
# -----------------
get_token()
get_rev_name("Mike")


