from sympy import mod_inverse

# Function to decrypt using Affine cipher
def affine_decrypt(ciphertext, a, b):
    try:
        a_inv = mod_inverse(a, 26)  # Compute modular inverse
    except ValueError:
        print(f"Skipping a={a}, no modular inverse.")
        return None  # Skip invalid values of a
    
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            y = ord(char.upper()) - ord('A')
            x = (a_inv * (y - b)) % 26
            plaintext += chr(x + ord('A'))
        else:
            plaintext += char
    return plaintext

# List of valid cheese names to match against
cheese_list = [
    "CHEDDAR", "GOUDA", "BRIE", "MOZZARELLA", "TOMMEDETSAVOIE",
    "PARMESAN", "CAMEMBERT", "ROQUEFORT", "PROVOLONE", "GRUYERE",
    "HAVARTI", "MUNSTER", "SWISS", "FETA", "RICOTTA", "ASIAGO"
]

# Ciphertext from the challenge
ciphertext = "HASSMHVMHQWPACMGIO"

print("Running Affine Cipher Decryption...")

# Try all valid values of a and b
for a in range(1, 26, 2):  # Only odd numbers (except multiples of 13) have modular inverses in mod 26
    if a % 13 == 0:
        continue
    for b in range(26):
        decrypted_text = affine_decrypt(ciphertext, a, b)
        if decrypted_text:
            print(f"Trying a={a}, b={b} -> {decrypted_text}")
        
        # Check if the decrypted text matches any known cheese names
        if decrypted_text and any(cheese in decrypted_text for cheese in cheese_list):
            print(f"\n[!] Possible cheese found: {decrypted_text} (a={a}, b={b})\n")
            exit()
