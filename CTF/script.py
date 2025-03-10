from pwn import remote
from Crypto.Util.number import long_to_bytes, inverse, GCD

host = "verbal-sleep.picoctf.net"
port = 58750

def get_data():
    conn = remote(host, port)
    data = conn.recvall().decode()
    conn.close()
    
    lines = data.split("\n")
    N = int(lines[0].split(": ")[1])
    e = int(lines[1].split(": ")[1])
    cyphertext = int(lines[2].split(": ")[1])
    
    return N, e, cyphertext

# Collect multiple (N, cyphertext) pairs
data_samples = []
for _ in range(5):  # Collect multiple responses
    data_samples.append(get_data())

# Find shared factors using GCD
for i in range(len(data_samples)):
    for j in range(i + 1, len(data_samples)):
        N1, _, _ = data_samples[i]
        N2, _, _ = data_samples[j]
        p = GCD(N1, N2)
        if p != 1 and p != N1:
            print(f"Common prime found: {p}")
            q = N1 // p
            print(f"Recovered p: {p}, q: {q}")

            # Compute private key d
            phi = (p - 1) * (q - 1)
            d = inverse(65537, phi)

            # Decrypt the message
            _, _, cyphertext = data_samples[i]
            plaintext = pow(cyphertext, d, N1)
            flag = long_to_bytes(plaintext)
            print(f"Decrypted flag: {flag.decode()}")
            exit()
