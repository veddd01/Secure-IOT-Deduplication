#!/usr/bin/env python
# coding: utf-8

import hashlib
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

# Function to chunk the file (simple line-based chunking)
def chunk_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines if line.strip()]

# Filter chunks (remove duplicates here)
def filter_chunks(chunks):
    return list(set(chunks))

# Generate fingerprint by hashing combined unique content
def generate_content_fingerprint(chunks):
    unique = filter_chunks(chunks)
    combined_data = ''.join(unique)
    fingerprint = hashlib.sha256(combined_data.encode()).hexdigest()
    return fingerprint

# Sign the fingerprint using RSA private key
def sign_fingerprint(fingerprint, private_key_path="private.pem"):
    key = RSA.import_key(open(private_key_path).read())
    h = SHA256.new(fingerprint.encode())
    signature = pkcs1_15.new(key).sign(h)
    return signature

# Verify the signature using the RSA public key
def verify_signature(fingerprint, signature, public_key_path="public.pem"):
    key = RSA.import_key(open(public_key_path).read())
    h = SHA256.new(fingerprint.encode())
    try:
        pkcs1_15.new(key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False

# Example usage
if __name__ == "__main__":
    file = "original_file.txt"
    chunks = chunk_file(file)
    fingerprint = generate_content_fingerprint(chunks)

    # Sign the fingerprint
    signature = sign_fingerprint(fingerprint)

    # Verify the signature
    is_valid = verify_signature(fingerprint, signature)
    print("Signature valid:", is_valid)
