# nested for loop
print("Nested For loop for tuple:")
cinemas = ("pushpa", "kgf", "rrr", "kalki", "bahubali")
for picture in cinemas:
    print(f"The cinema letters {picture}")
    for j in picture:
        print(f"The letter of allmovies {j}")
