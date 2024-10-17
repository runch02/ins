import rsa

def main():
    publicKey, privateKey = rsa.newkeys(512)
    message = input("Enter the message: ")
    encryptMessage = rsa.encrypt(message.encode(), publicKey)
    decryptMessage = rsa.decrypt(encryptMessage, privateKey).decode()

    print(f"Original Message '{message}'")
    print(f"Encrypted Message '{encryptMessage}'")
    
    print(f"Decrypt Message '{decryptMessage}'")
    
if __name__ == "__main__":
    main()