def pad_string(s):
    return s.zfill(3)  # zfill pads the string with zeros to ensure length 3

# Example usage
input_string = input("Enter a string: ")
padded_string = pad_string(input_string)
print("Padded String:", padded_string)