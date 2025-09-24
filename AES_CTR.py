import secrets
from Crypto.Cipher import AES

def keygen() -> bytes:
    # 16 bytes = 128 bits for AES
    return secrets.token_bytes(16)

def encrypt(message: str, key: bytes, nonce: bytes) -> bytes:
    aes = AES.new(key, AES.MODE_ECB)
    byte_encoding = message.encode()
    blocks = cut_byte_encoding_into_blocks(byte_encoding)
    counter = make_counter_block(nonce, 0)
    counter_encryption = aes.encrypt(counter)
    # Initialize the ciphertext with the initial counter
    ciphertext = counter_encryption
    # Loop over the blocks, create a counter for the relevant block, encrypt it with AES and XOR it into plaintext block
    for i, block in enumerate(blocks):
        counter = make_counter_block(nonce, i)
        counter_encryption = aes.encrypt(counter)
        ciphertext_block = bytes(a ^ b for a, b in zip(block, counter_encryption))
        # Build the ciphertext
        ciphertext += ciphertext_block
    
    return ciphertext

def decrypt(ciphertext: bytes, key: bytes, nonce: bytes) -> str:
    aes = AES.new(key, AES.MODE_ECB)
    blocks = cut_byte_encoding_into_blocks(ciphertext)
    # Ignore the first block since we pass the nonce in the function parameter
    blocks = blocks[1:]

    message_encoded = b""
    # Here we again encrypt the nonce and XOR into the ciphertext as XOR is inverse to itself to recover plaintext block
    for i, block in enumerate(blocks):
        counter = make_counter_block(nonce, i)
        counter_encryption = aes.encrypt(counter)
        ciphertext_block = bytes(a ^ b for a, b in zip(block, counter_encryption))
        # Build the message
        message_encoded += ciphertext_block

    message = message_encoded.decode()

    return message

def make_counter_block(nonce: bytes, counter: int) -> bytes:
    return nonce + counter.to_bytes(8, "big")

def cut_byte_encoding_into_blocks(byte_encoding: bytes) -> list:
    blocks = []
    
    for i in range(0, len(byte_encoding), 16):
        blocks.append(byte_encoding[i:i + 16])

    return blocks