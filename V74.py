# @cikey b8c2f0e997296c4047aa90efbb14a388
# @sid 20251174010038
# @aid V7.4


contatos = {}

for i in range(3):
    chave_nome = input("Digite um nome: ")
    valor_tel = input("Digite um telefone: ")
    contatos[chave_nome] = valor_tel

print("Lista de contatos:")
print(contatos)

procura_nome = input("Qual o nome que voce quer consultar:")

if procura_nome in contatos:
    print(f"O telefone de {procura_nome} e {contatos[procura_nome]}")
else:
    print("Contato nao encontrado")