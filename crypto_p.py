from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP


with open('encrypted_data.bin', 'wb') as out_file:
    recipient_key = RSA.import_key(
        open('my_rsa_public.pem').read()
    )

    session_key = get_random_bytes(16)

    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    out_file.write(cipher_rsa.encrypt(session_key))

    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    data = b'blah blah blah Python blah blah'
    cipher_text, tag = cipher_aes.encrypt_and_digest(data)

    out_file.write(cipher_aes.nonce)
    out_file.write(tag)
    out_file.write(cipher_text)

# from Crypto.PublicKey import RSA
#
#
# code = "nooneknows"
# key = RSA.generate(2048)
#
# encrypted_key = key.exportKey(
#     passphrase=code,
#     pkcs=8,
#     protection="scryptAndAES128-CBC"
# )
#
# with open('my_private_rsa_key.bin', 'wb') as f:
#     f.write(encrypted_key)
#
# with open('my_rsa_public.pem', 'wb') as f:
#     f.write(key.publickey().exportKey())

# from Crypto.Cipher import DES
#
# key = b'abcdefgh'
#
#
# def pad(text):
#     while len(text) % 8 != 0:
#         text += b' '
#     return text
#
#
# des = DES.new(key, DES.MODE_ECB)
# text = b'Python rocks!'
# padded_text = pad(text)
#
# encrypted_text = des.encrypt(padded_text)
# print(encrypted_text)
#
# data = des.decrypt(encrypted_text)
# print(data)
# import hashlib
# import binascii
#
#
# dk = hashlib.pbkdf2_hmac(
#     hash_name='sha256',
#     password=b'bad_password34',
#     salt=b'bad_salt',
#     iterations=100000
# )
# result = binascii.hexlify(dk)
# print(result)

# result = hashlib.md5(b'Python rocks!').hexdigest()
# result2 = hashlib.md5(b'Python rocks!').digest()
# sha = hashlib.sha1(b'Hello Python').hexdigest()
#
# print(result)
# print(result2)
# print(sha)

