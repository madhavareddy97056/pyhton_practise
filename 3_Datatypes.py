# variables & Datatypes

# String datatype
Name = "Madhava Reddy"
City = "Hyderabad"
Skill = "DevOps"
Cloud = "AWS"

# Integer Datatype
age = 27
pincode = 500090
experience = 3

# float Datatype
v1 = 1.2231
v2 = 243.2342
v3 = 432.520

# boolean
a = True
b = False
print(a)
print(b)

# List and printing list, mutable
my_info = [Name, age, pincode, "klu", experience, v1, v2, v3, ["aws", "azure", "ibm", "Gcp"]]
print(my_info)
print(type(my_info))

# Tuple and printing tuple, immutable
my_tuple = (Name, age, pincode, "klu", experience, v1, v2, v3, ["aws", "azure", "ibm", "Gcp"])
print(my_tuple)
print(type(my_tuple))

# Dictionary, key:value pair
my_hobbies = {"hobby1":"Gymming", "hobby2":"running", "hoppy3":"swimming", "sports":["cricket", "swimming", "weight_lifting"]}
print(my_hobbies)
print(type(my_hobbies))
