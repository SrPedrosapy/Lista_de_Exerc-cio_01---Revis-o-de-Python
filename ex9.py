nomes = input("Digite uma lista de nomes separados por espaço: ")
lista = nomes.split()

nomes_com_a = [nome for nome in lista if nome.lower().startswith('a')]

print("Nomes que começam com 'A':", nomes_com_a)