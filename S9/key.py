
cfr = ["petrescu", "omrani", "debeljiuc", "boateng", "deac" , "petrila", "grahovac"]

def len_is(string):
    print("Key function called with: ", string)
    return len(string)

def longest_strings(lst):
    lst.sort(key=len_is, reverse=True)
    print (lst[:5])

longest_strings (cfr)