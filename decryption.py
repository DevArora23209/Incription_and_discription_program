def abc(encoded_str):
    bb = encoded_str.count(',')
    dd = {chr(ord('a') + i): i + bb for i in range(1, 27)}
    dd[' '] = 0 + bb  # Spaces are encoded as 0 + bb    
    numerical_values = [int(value) for value in encoded_str.split(',') if value.isdigit()]
    original_word = ''.join(chr(value - bb + ord('a') - 1) for value in numerical_values)
    return original_word
while True:
    encoded_str = input("Enter the encoded string: ").lower()
    encoded_str = ''.join(char for char in encoded_str if char.isdigit() or char == ',')
    print("Encoded String:", encoded_str)
    original_word = abc(encoded_str)
    print("Original Word:", original_word)
