def caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

def get_valid_shift():
    while True:
        try:
            shift = int(input("Enter the value of the shift, 1-25: "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("The shift should be in the range of 1-25.")
        except ValueError:
            print("Please enter an integer.")

def main():
    text = input("Enter a string to encrypt: ")
    shift = get_valid_shift()
    encrypted_text = caesar(text, shift)
    print("Encrypted text:", encrypted_text)

main()