def main():
    book_path = "books/frankenstein.txt"
    letter_dict = {}
    #atribui a text o conteúdo do livro
    text = book_text(book_path)
    final_list = words_list(text)
  
    #retorna a quantidade de palavras
    final_count = count_text(text)
    #retorna o dicionário completo e ordenado
    letter_dict = words_to_dict(final_list, letter_dict)
    
    print_report(book_path,final_count)
    report_dict(letter_dict)

    print("\n############# END OF REPORT ##############")


#transforma todas as palavras em minúsculas e  
#retorna uma lista das palavras
def words_list(text):
    lowered_text = text.lower()
    split_text = lowered_text.split()
    return split_text

#conta a quantidade de palavras existentes no livro
def count_text(text):
    words = text.split()
    return len(words)

#abre o livro e retorna o texto
def book_text(book_path):
    with open(book_path) as f:
        return f.read()

#retira os caracteres especiais e adiciona/incrementa
#cada key (letra) 
def words_to_dict(list, dicio):
    import re
    for word in list:
        word = re.sub('[^a-zA-Z]+', '', word)
        for c in word:
            if c in dicio:
                dicio[c] += 1
            else:
                dicio[c] = 1
    #retorna o dicionário ordenado
    return dict(sorted(dicio.items()))

def print_report(livro, count):
    print ("################ BOOKBOT #################")
    print ("############### BOOKREPORT ###############")
    print 
    print (f"\n++ TODAY'S BOOK: {livro} ++")

    print (f"\nThis book contains {count} words")
    print ("\n\n++ It's letters count is as follows: ++\n")

def report_dict(dicio):
    for k in dicio:
        print(f"The letter {k} appears {dicio[k]} times")

main()