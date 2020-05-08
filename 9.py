def user_hello(user):
    print(f"Привет,{user}")

clients = ['John','David', 'Kate', 'Alex']
for user in clients:
    user_hello(user)
new_user = "Artur"
clients.append(new_user)

print(f"Привет,{clients[-1]}")