from unittest import mock


months = {
'January': 1,
'February': 2,
'April': 4,
'May': 5,
'March': 3,
'October': 10,
'July': 7,
'August': 8,
'June': 6,
'September': 9,
'November': 11,
'December': 12
}

def trim_by_six(dict_in):
    for k in list(dict_in.keys()):
        if dict_in[k] > 6:
            del dict_in[k]


trim_by_six(months)

print(months)