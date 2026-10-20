def display_snacks(*args):
    if len(args) == 0:
        print("No snacks Packed!")
    else:
        for snack in args:
            print(snack)
        print(f"Snack count: {len(args)}")

display_snacks("Popcorn", "Pretzels", "Cookies")
display_snacks()