def caesar_cipher(text, shift, mode):
    result = ""

    # Adjust shift for decrypt mode
    if mode == "decrypt":
        shift = -shift

    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # Leave numbers, spaces, punctuation unchanged
            result += char

    return result


# --- Main program ---
print("=== Caesar Cipher Program ===")
message = input("Enter your message: ")
shift = int(input("Enter shift value (e.g., 3): "))
mode = input("Choose mode (encrypt/decrypt): ").lower()

if mode not in ["encrypt", "decrypt"]:
    print("Invalid mode selected!")
else:
    output = caesar_cipher(message, shift, mode)
    print(f"\nResult ({mode}ed text): {output}")
