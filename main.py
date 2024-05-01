letters="abcdefghijklmnopqrstuvwxyz"
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("--------START---------")
        print(f"{amount(file_contents)} words")
        print(count(file_contents))
        print("--------END---------")
def amount(string):
    return(len(string.split()))
def count(string):
    dict={}
    lower=string.lower()
    for i in lower:
        if i in letters:    
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
    return dict


main()