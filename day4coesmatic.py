#Assigment is dictionary cosematics thing of girl (key:value)
cosmetic_thing = {"lip":"lipstick", "Eyeslash":"Mascara", "Skin tone":"Foundation"}
key = input("Enter the key: ")
value = cosmetic_thing.get(key)
print(f"The value for the key '{key}' is: {value}")
