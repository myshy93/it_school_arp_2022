user_info = {
    "name": "Alex",
    "age": 28,
    "email": "alex.radu@email.com",
    "gender": "M"
}

# lista valorilor; values => obiect de tip view
u_i_vales1 = user_info.values()
print(type(u_i_vales1))

for v in u_i_vales1:
    print(v)

