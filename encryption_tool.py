from cryptography.fernet import Fernet
import os


def generate_key():
    """
    Generate and save encryption key.
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("[INFO] Key generated and saved as secret.key")


def load_key():
    """
    Load the encryption key.
    """
    return open("secret.key", "rb").read()


def encrypt_file(file_path):
    """
    Encrypt a file.
    """
    try:
        key = load_key()
        fernet = Fernet(key)

        with open(file_path, "rb") as file:
            data = file.read()

        encrypted = fernet.encrypt(data)

        with open(file_path + ".enc", "wb") as file:
            file.write(encrypted)

        print(f"[SUCCESS] File encrypted: {file_path}.enc")

    except Exception as e:
        print(f"[ERROR] {e}")


def decrypt_file(file_path):
    """
    Decrypt a file.
    """
    try:
        key = load_key()
        fernet = Fernet(key)

        with open(file_path, "rb") as file:
            data = file.read()

        decrypted = fernet.decrypt(data)

        output_file = file_path.replace(".enc", "")

        with open(output_file, "wb") as file:
            file.write(decrypted)

        print(f"[SUCCESS] File decrypted: {output_file}")

    except Exception as e:
        print(f"[ERROR] {e}")


def main():
    print("\n=== Advanced Encryption Tool ===\n")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File\n")

    choice = input("Select an option: ")

    if choice == "1":
        generate_key()

    elif choice == "2":
        file_path = input("Enter file path to encrypt: ")
        encrypt_file(file_path)

    elif choice == "3":
        file_path = input("Enter .enc file path to decrypt: ")
        decrypt_file(file_path)

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()