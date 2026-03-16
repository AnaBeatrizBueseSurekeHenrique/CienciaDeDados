contatos =[{
    "nome": "Pessoa",
    "contato": "email",
    "telefone": 10
},
           {
    "nome": "Pessoa2",
    "contato": "email",
    "telefone": 10
},{
    "nome": "Pessoa3",
    "contato": "email",
    "telefone": 10
}
           ]

nome = (input("Insira o nome"))
achou = False
i = 0
while(not achou and i < len(contatos)):
    if(contatos[i]["nome"] == nome):
        print(f"Contato: {contatos[i]["contato"]}")
        print(f"Telefone:{contatos[i]["telefone"]}")
        achou = True
    else:
        i += 1

if(not achou):
    print('Não há este nomes nos contatos!')