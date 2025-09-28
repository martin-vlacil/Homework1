# Homework1
Python version: 3.11.9

Before running for the first time, ensure installing these packages:
1. pip install pycryptodome
2. pip install secrets

The main funcition in main.py file contains 2 functions for each of the exercises. Simply comment or uncomment one of the two to run the test.

Run command: python main.py

Interpretation of the tests:
    1. successful_test_exercise_3_1()
        Initial message is first printed out. Ciphertext is then printed out and after decrypting, the message is shown
        again to make sure that is is the same as the initial message.
    2. attack_exercise_3_2()
        Same as before, the same Initial message is printed out.
        An exception occurs in the decrypt function (it expects that the decryption can decode a bytes object into a UTF-8 string after a succesful run, as the initial message is UTF-8). Because the ciphertext (nonce at the beginning) was altered, the decoding returns a message that is no longer UTF-8.

