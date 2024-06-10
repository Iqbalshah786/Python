import string

plain_text = "Python is the coolest"
shift = 7
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase


def caesar_cipher(plain_text,shift):
    

    def shift_char(char,shift):
        if char in uppercase:
            index = uppercase.index(char)
            return uppercase[(index + shift) % 26]
        elif char in lowercase:
            index = lowercase.index(char)
            return lowercase[(index + shift) % 26]
        else: 
            return char
        
    ouput_text = [shift_char(char,shift) for char in plain_text]
    return "".join(ouput_text)



output_text1 = caesar_cipher(plain_text, shift)
print(output_text1)

# Another way to write the code:

output_text2 = []

for eachLetter in plain_text:
    if eachLetter in uppercase:
        index = uppercase.index(eachLetter)
        target_index = (index + shift) % 26
        newLetter = uppercase[target_index]
        output_text2.append(newLetter)
    elif eachLetter in lowercase:
        index = lowercase.index(eachLetter)
        target_index = (index + shift) % 26
        newLetter = lowercase[target_index]
        output_text2.append(newLetter)
    else:
        output_text2.append(" ")
print("".join(output_text2))
