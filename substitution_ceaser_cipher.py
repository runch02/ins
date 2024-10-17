class First:
    
    def __init__(self, text, shift, result = ""):
        self.text = text
        self.shift = int(shift)
        self.result = result
        
    def ceaser_cipher(self):
        for i in range(len(self.text)):
            char = self.text[i]
            if char.isupper():
                self.result += chr((ord(char) + self.shift - 65) % 26 + 65)
            elif char.islower():
                self.result += chr((ord(char) + self.shift - 97) % 26 + 97)
            else:
                self.result += char
        return self.result
    

def main():        
    first = First(
        input("Enter the text: "),
        input("Enter the shift key: ")
    )
    
    str(first.shift)
    
    print(first.ceaser_cipher())


if __name__ == "__main__":
    main()