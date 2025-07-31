from Art import logo

print(logo)

alphabet = [chr(i) for i in range(97, 123)] * 2  # ['a', 'b', ..., 'z', 'a', ..., 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    
    for char in start_text:
        if char.isalpha():
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    
    print(f"The {cipher_direction}d text is: {end_text}")

# Loop to continue the program
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Handle shift values greater than 26
    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart != "yes":
        should_continue = False
        print("Goodbye!")


