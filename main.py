import requests
import json
import time

def envoyer_message_via_webhook(session, url_webhook, contenu_message):
    headers = {'Content-Type': 'application/json'}
    payload = {'content': contenu_message}

    try:
        response = session.post(url_webhook, json=payload, headers=headers)
        response.raise_for_status()

        if response.status_code == 204:
            print("Message envoyé avec succès via le webhook.")
        else:
            print(f"Erreur lors de l'envoi du message. Code d'état : {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Une erreur s'est produite lors de l'envoi du message : {e}")

session = requests.Session()

print("""
          ______ _____    
         |  ____|   __ \   
         | |__  | |__) |
         |  __| |  _  /
         | |    | | \ \   
         |_|    |_|  \_\  
         
         """)

url_webhook = input("Veuillez entrer l'URL du webhook : ")
contenu_message = input("Veuillez entrer le message à envoyer : ")
temps_entre_envois = int(input("Veuillez entrer le temps entre chaque envoi (en secondes, 0=Spam) : "))

print(f"Démarrage du script. Envoi de messages toutes les {temps_entre_envois} secondes...\n")

while True:
    envoyer_message_via_webhook(session, url_webhook, contenu_message)
    time.sleep(temps_entre_envois)
