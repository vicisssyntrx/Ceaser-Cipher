def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

# --- User Interaction ---
print("Welcome to Caesar Cipher Encryption/Decryption")
choice = input("Type 'E' to Encrypt or 'D' to Decrypt: ").upper()
message = input("Enter your message: ")
shift = int(input("Enter the shift number (e.g., 3): "))

if choice == 'E':
    print("Encrypted:", encrypt(message, shift))
elif choice == 'D':
    print("Decrypted:", decrypt(message, shift))
else:
    print("Invalid choice.")
