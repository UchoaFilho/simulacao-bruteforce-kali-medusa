usuarios = ["user", "msfadmin", "admin", "root"]
senhas = ["123456", "password", "qwerty", "msfadmin"]

with open("wordlist.txt", "w") as arquivo:
    for u in usuarios:
        for s in senhas:
            combinacao = f"{u}:{s}"
            
            # Mostra na tela
            print(combinacao)
            
            # Salva no arquivo
            arquivo.write(combinacao + "\n")
