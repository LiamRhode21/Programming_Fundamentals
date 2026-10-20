# ** kwargs accept any number of key word arguments
# Python collects them into a dictionary
# a dictionary stores key:value pairs

def about_you(**traits):
    # for each item(key:value) in the traits dictionary
    for key,value in traits.items():
        print(f"{key}: {value}")

# call the function with keyword arguments
about_you (eye_color = "blue", favorite_number = 21, hair_color = "brown")
# the dictionary (traits) holding these arguments looks like this
# {"eye_color":"blue", "favorite_number":21, "hair_color":"brown"}