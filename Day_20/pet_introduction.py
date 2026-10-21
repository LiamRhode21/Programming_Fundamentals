def introduce_pet(name, species, age):
    print(f"{name} is a {species} aged {age}")

pet = {"age": 4, "name": "Pickles", "species": "cat"}
introduce_pet(**pet)
