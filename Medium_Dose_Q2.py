
# Medium Dose: Q2

# Dictionary with alphabets, numbers and their respective moorse codes.
morse_dict = {
".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
"..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
"-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
"..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
"--..": "Z",
"-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4",
".....": "5", "-....": "6", "--...": "7", "---..": "8", "----.": "9"
}

def morse_to_eng(input_code):
    morse_code = input_code.strip().split("       ")   # Standard 7 space split between 2 words
    
    for i in range(len(morse_code)):
        morse_code[i] = morse_code[i].strip().split("   ")   # standard 3 space split between 2 letters
    
    eng_code = ""    # output code

    for word in morse_code:   # decoding morse code and appending it to output code
        for letter in word:
            eng_code += morse_dict.get(letter, "")

        eng_code += " "   # adding a space between 2 words

    return eng_code



# sample input: print(morse_to_eng("-..   ---   -.   -       -...   .   .-..   ..   . ...-   .       --   .       .---   ..-   ...   -       .--   .-   -   -.-.   ...."))
# sample input: print(morse_to_eng("...-   ..   ....   .-   .-   -.       --.   ..-   .--.   -   .-"))