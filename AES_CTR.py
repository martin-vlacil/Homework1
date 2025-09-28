import secrets
from Crypto.Cipher import AES

def keygen() -> bytes:
    # 16 bytes = 128 bits for AES
    return secrets.token_bytes(16)

def encrypt(message: str, key: bytes) -> bytes:
    nonce = secrets.token_bytes(8)
    # MODE_ECB ensures barebone AES encryption algorithm
    aes = AES.new(key, AES.MODE_ECB)
    byte_encoding = message.encode()
    blocks = cut_byte_encoding_into_blocks(byte_encoding)
    c0 = make_counter_block(nonce, 0)
    # Initialize the ciphertext with the initial counter
    ciphertext = c0
    # Loop over the blocks, create a counter for the relevant block, encrypt it with AES and XOR it into plaintext block
    for i, block in enumerate(blocks):
        counter = make_counter_block(nonce, i)
        counter_encryption = aes.encrypt(counter)
        ciphertext_block = bytes(a ^ b for a, b in zip(block, counter_encryption))
        # Build the ciphertext
        ciphertext += ciphertext_block
    
    return ciphertext

def decrypt(ciphertext: bytes, key: bytes) -> str:
    # MODE_ECB ensures barebone AES encryption algorithm
    aes = AES.new(key, AES.MODE_ECB)
    blocks = cut_byte_encoding_into_blocks(ciphertext)
    # Extract the first block with the nonce_counter and loop through the remaining blocks
    c0 = blocks[:1]
    nonce = c0[0][:8]
    blocks = blocks[1:]

    message_encoded = b""
    # Here we again encrypt the nonce and XOR into the ciphertext as XOR is inverse to itself to recover plaintext block
    for i, ciphertext_block in enumerate(blocks):
        counter = make_counter_block(nonce, i)
        counter_encryption = aes.encrypt(counter)
        message_block = bytes(a ^ b for a, b in zip(ciphertext_block, counter_encryption))
        # Build the message
        message_encoded += message_block

    # Converting bytecode into readable string
    try:
        message = message_encoded.decode()
        return message
    except UnicodeDecodeError as e:
        print("Cannot decode into plaintext as it does not contain UTF-8 characters. DID SOMEONE MESS WITH THE CIPHERTEXT?")

def make_counter_block(nonce: bytes, counter: int) -> bytes:
    return nonce + counter.to_bytes(8, "big")

def cut_byte_encoding_into_blocks(byte_encoding: bytes) -> list:
    blocks = []
    
    for i in range(0, len(byte_encoding), 16):
        blocks.append(byte_encoding[i:i + 16])

    return blocks