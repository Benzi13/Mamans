def extract_o_words(sentence: str) -> str:
    words = sentence.split()
    o_words = [w.upper() for w in words if "o" in w.lower()]
    return ", ".join(o_words)

    
def main():
    line = 'This line contains words and some have the letter o'
    o_string = extract_o_words(line)
    
    print(f"{o_string=}")
if __name__ == "__main__":
    main()