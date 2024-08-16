# シーザー暗号を複合するためのスクリプト
# 暗号文とシフト数をinputで渡す

def caesar_cipher_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift % 26
            ascii_offset = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - ascii_offset - shift_amount) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# テスト
ciphertext = input("暗号文を入力してください: ")
shift = int(input("シフト量を入力してください: "))

decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
print(f"復号化されたテキスト: {decrypted_text}")