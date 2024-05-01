def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""

    # Traverse each character in the text
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Determine the appropriate shift based on character case
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)  # 65 maps 'A' to 0, 'B' to 1, 'C' to 2, and so on
            else:
                encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)  # 97 does the same but for lowercase
        else:
            encrypted_char = char  # Keep non-alphabetic characters unchanged
        encrypted_text += encrypted_char

    return encrypted_text

# Test the function
text = "Seventynine"
shift = 6 # how many positions each letter in the plaintext is shifted
print("Text : " ,text,"\nShift : ",str(shift),"\nCipher: ",caesar_cipher_encrypt(text, shift))

