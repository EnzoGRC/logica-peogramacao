while True:
    string_digitada = input("digite uma palavra: ")
    if string_digitada.lower () == "sair":
        print("fim!")
        break
if len(string_digitada) < 2:
        print("string muito pequena")
        continue
        print("tente digitar \ 'sair\ '")