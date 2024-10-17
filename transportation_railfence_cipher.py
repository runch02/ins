class First:
    def __init__(self, text, result = ""):
        self.text = text
        self.result = result
        
    def railfence_cipher(self):
        for i in range(len(self.text)):
            if i % 2 == 0:
                self.result += self.text[i]
                
        for j in range(len(self.text)):
            if i % 2 != 0:
                self.result += self.text[i]
        
        return self.result
        
def main():
    first = First(
        input("Enter the text: ")
    )
    
    print(first.railfence_cipher())

if __name__ == "__main__":
    main()