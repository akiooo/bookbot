def main():

    counter = 0

    with open("books/frankenstein.txt", "r") as f:
        for line in f:
            counter += len(line.split())
    
    print(counter)



main()
