import AES_CTR as aes_lib
import secrets

def main():
    successful_test_exercise_3_1()
    # attack_exercise_3_2()


def attack_exercise_3_2():
    initial_message = "I am a message, surely no cryptographers will make me suffer by encrypting and decrypting me for testing purpo-UAAAAAAAAAAAAAAGH"
    key = aes_lib.keygen()
    print(f"Initial message: {initial_message}")
    ciphertext = aes_lib.encrypt(initial_message, key)

    # The attack: modifying the first block - c0, to mess with the nonce
    modified = bytearray(ciphertext)
    modified[0] = 0x12
    modified[1] = 0x34
    modified[2] = 0x56
    ciphertext = bytes(modified)
    message = aes_lib.decrypt(ciphertext, key)

def successful_test_exercise_3_1():
    # There is no error handling for a message that is not a multple of 128-bit, when changing, be careful when changing
    initial_message = "I am a message, surely no cryptographers will make me suffer by encrypting and decrypting me for testing purpo-UAAAAAAAAAAAAAAGH"
    key = aes_lib.keygen()
    print(f"Initial message: {initial_message}")
    ciphertext = aes_lib.encrypt(initial_message, key)
    print(f"Ciphertext after encrypting the message: {ciphertext}")
    message = aes_lib.decrypt(ciphertext, key)
    print(f"Message after decrypting the ciphertext: {message}")

if __name__ == "__main__":
    main()
