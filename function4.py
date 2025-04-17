alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("type 'encode' or 'decode': \n").lower()
text = input("enter your text: \n").lower()
shift = int(input("type the shift number: \n"))

def ceaser(original_text, shift_amount, encode_or_decode):
    output_text = "" 
    if encode_or_decode == "decode":
        shift_amount *= -1  # reverse shift for decoding

    for letter in original_text:
        if letter in alphabets:
            shifted_position = alphabets.index(letter) + shift_amount
            shifted_position %= len(alphabets)
            output_text += alphabets[shifted_position]
        else:
            output_text += letter  # keep spaces/punctuation as-is

    print(f"here is the {encode_or_decode} result: {output_text}")

# function call (no colon here!)
ceaser(original_text=text, shift_amount=shift, encode_or_decode=direction)
