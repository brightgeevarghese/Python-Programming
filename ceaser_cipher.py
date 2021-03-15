# read message from user
my_message = input()
# read the distance
distance = int(input())
cipher_text = ''
# check whether distance > 26
if distance > 26:
    distance %= 26
# process every letter by adding with distance
for ch in my_message:
    # check whether its a lowercase
    if 'a'<=ch<='z':
        data = ord(ch) + distance
        if data > 122:
            data -= 26
        cipher_text += chr(data)
    # check whether its an uppercase
    elif 'A'<=ch<='Z':
        data = ord(ch) + distance
        if data > 90:
            data -= 26
        cipher_text += chr(data)
    else:
        cipher_text += ch
print('Encoded data is', cipher_text)
# Decode it
my_text = ''
# process the generated cipher_text
for ch in cipher_text:
    # check whether its a lowercase
    if 'a' <= ch <= 'z':
        #subtract distance from the letter, ch
        data = ord(ch) - distance
        if data < 97:
            data += 26
        my_text += chr(data)
    # check whether its an uppercase
    elif 'A' <= ch <= 'Z':
        # subtract distance from the letter, ch
        data = ord(ch) - distance
        if data < 65:
            data += 26
        my_text += chr(data)
    else:
        my_text += ch
print('Decoded msg is', my_text)
