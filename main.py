import AES_CTR as aes_lib
import secrets

def main():
    # There is no error handling for a message that is not a multple of 128-bit, when changing, be careful when changing
    initial_message = "I am a message, surely no cryptographers will make me suffer by encrypting and decrypting me for testing purpo-UAAAAAAAAAAAAAAGH"
    key = aes_lib.keygen()
    nonce = secrets.token_bytes(8)
    print(f"Initial message: {initial_message}")
    ciphertext = aes_lib.encrypt(initial_message, key, nonce)
    print(f"Ciphertext after encrypting the message: {ciphertext}")
    message = aes_lib.decrypt(ciphertext, key, nonce)
    print(f"Message after decrypting the ciphertext: {message}")

if __name__ == "__main__":
    main()
