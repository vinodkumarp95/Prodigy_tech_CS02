from PIL import Image
import numpy as np


def encrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = np.array(image)

    # Ensure the pixel values stay within 0-255
    encrypted_pixels = (pixels.astype(np.int32) + key) % 256
    encrypted_pixels = encrypted_pixels.astype('uint8')  # Convert back to uint8 after computation

    encrypted_image = Image.fromarray(encrypted_pixels)
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")


def decrypt_image(image_path, output_path, key):
    image = Image.open(image_path)
    pixels = np.array(image)

    # Ensure the pixel values stay within 0-255
    decrypted_pixels = (pixels.astype(np.int32) - key) % 256
    decrypted_pixels = decrypted_pixels.astype('uint8')  # Convert back to uint8 after computation

    decrypted_image = Image.fromarray(decrypted_pixels)
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")


def main():
    while True:
        mode = input(
            "\nDo you want to encrypt or decrypt an image? (Enter 'encrypt', 'decrypt', or 'exit' to quit): ").strip().lower()
        if mode not in ['encrypt', 'decrypt', 'exit']:
            print("Invalid input. Please enter 'encrypt', 'decrypt', or 'exit'.")
            continue

        if mode == 'exit':
            print("Exiting the program. Goodbye!")
            break

        image_path = input("Enter the path to the image file: ").strip()
        output_path = input("Enter the path to save the processed image: ").strip()
        while True:
            try:
                key = int(input("Enter the encryption key (an integer value): "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer for the key.")

        if mode == 'encrypt':
            encrypt_image(image_path, output_path, key)
        elif mode == 'decrypt':
            decrypt_image(image_path, output_path, key)


if __name__ == "__main__":
    main()
