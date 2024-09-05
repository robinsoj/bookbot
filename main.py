def word_count(str):
    words = str.split()
    return len(words)

def char_count(str):
    new_str = str.lower()
    distinct_letters = set()
    results = {}
    for a in range(0, len(new_str)):
        if ((new_str[a]) > '`' and (new_str[a] < '~')):
            distinct_letters.add(new_str[a])
    for a in distinct_letters:
        results[a] = 0
    for b in range(0, len(new_str)):
        if (new_str[b] in results):
            results[new_str[b]] += 1
    return results

def sort_dict(dict):
    return dict["num"]

def print_report(bk, wc, ltrs):
    print(f"--- {bk} ---")
    print(f"{wc} words found in the document")
    list_ltrs = []
    for k in ltrs:
        dict = {"name": k, "num": ltrs[k]}
        list_ltrs.append(dict)
    list_ltrs.sort(reverse=True, key=sort_dict)
    for k in list_ltrs:
        name = k["name"]
        num = k["num"]
        print(f"The '{name}' character was found {num} times")
    print("--- End report ---")

def main():
    book = 'books/frankenstein.txt'
    with open(book) as f:
        file_contents = f.read()
        wc = word_count(file_contents)
        char_dict = char_count(file_contents)
        print_report(book, wc, char_dict)


main()