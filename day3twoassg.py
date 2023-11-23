email = input("Enter your email address: ")
res = email[email.index('@')+1:]
print("Domain name: " + res)
