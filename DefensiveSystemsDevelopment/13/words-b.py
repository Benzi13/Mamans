from typing import List

def filter_and_format(words: List[str]) -> List[str]:
    result = []
    for w in words:
        if w.lower().startswith("b"):
            result.append(w.capitalize())
    return result
    
def filter_and_format_one_liner(words):
    return [w.capitalize() for w in words if w.lower().startswith("b")]

    
def main():
    a_list = ["apple", "banana", "carrot", "black", "box"]
    b_list = filter_and_format(a_list)
    b_list_one_liner = filter_and_format_one_liner(a_list)
    print(f"{b_list=}")
    print(f"{b_list_one_liner=}")

if __name__ == "__main__":
    main()