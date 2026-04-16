import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth, firestore_async, firestore, messaging
import asyncio

def mudarPreco(id, precoNovo):
    data = {"preco": precoNovo}
    print("Tratamento de Exceções")
    try:
        db.collection('exercicio').document(id).set(data)
    except ValueError as e:
        print(f'{e} Valor errado!')
print("Configuração e Inicialização")
cred = credentials.Certificate("ciencias-dados-firebase-adminsdk-fbsvc-0e394c7d74.json")
app = firebase_admin.initialize_app(cred)
print(app.name)
print("Gerenciamento de Usuários")
user = auth.create_user(
 email="anabeatriz.sureke9@gmail.com",
 password="braspress",
 display_name="Ana Beatriz"
)

id = user.uid

print(auth.get_user(id))
token = auth.create_custom_token(id)
db = firestore.client()
produtos_ref = db.collection("exercicio")

print('Operações de Firestore')
mudarPreco('pao', 500)
print("Consultas avançadas de firestore")
prec = produtos_ref.where("preco",">", 15)
for doc in prec.stream():
    print(f"ID do Documento: {doc.id}")
    print(f"Dados do Documento: {doc.to_dict()}")
    print("-" * 30)
    
registration_token = 'token'

print("Envio de Notificação")
message = messaging.Message(
    data={
        'score': '850',
        'time': '2:45',
    },
    token=registration_token,
)

response = messaging.send(message)
print('Successfully sent message:', response)
