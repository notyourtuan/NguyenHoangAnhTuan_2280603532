from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import hashlib

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

client_key = RSA.import_key(2048)

server_public_key = RSA.import_key(client_socket.recv(2048))

client_socket.send(client_key.publickey().export_key(format='PEM'))

encrypted_aes_key = client_socket.recv(2048)

cipher_rsa = PKCS1_OAEP.new(client_key)
aes_key = cipher_rsa.decrypt(encrypted_aes_key)
