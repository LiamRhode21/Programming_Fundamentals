def display_welcome():
    print("Welcome to Pixel Palace!")

def calculate_tokens(packs, token_per_pack = 10):
    return packs * token_per_pack

def display_summary(player_name, tokens):
    print(f"Player: {player_name}")
    print(f"Tokens: {tokens}")
    
TOKENS_PER_PACK = 15

display_welcome()
player_name = input("Player name: ")
packs = int(input("Number of token packs: "))
tokens = calculate_tokens(packs, TOKENS_PER_PACK)
display_summary(player_name, tokens)
