# Liste qui contiendra tous les contacts
contacts = []

def ajouter_contact():
    nom = input("Entrez le nom du contact :")
    prenom = input("Entrez le prénom :")
    telephone = input("Entrez le numéro de téléphone :")
    email = input("Entrez votre email :")

    # Création d'un dictionnaire pôur le contact
    contact = {
        "nom": nom,
        "prenom": prenom,
        "telephone": telephone,
        "email": email
    }

    # Ajouter le contact à la liste
    contacts.append(contact)
    print("Contact ajouté avec succès !")

def afficher_contacts():
    if not contacts:
        print("Aucun contact à afficher.")
        return
    
    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}:")
        print(f"Nom: {contact['nom']}")
        print(f"Prenom: {contact['prenom']}")
        print(f"Telephone: {contact['telephone']}")
        print(f"Email: {contact['email']}")

def supprimer_contact():
    nom = input("Entrez le nom du contact à supprimer :")
    # Filtrer pour garder uniquement les contacts qui ne correspondent pas au nom
    global contacts
    contacts = [c for c in contacts if c["nom"] != nom]
    print("Contact supprimé(s'il existait)!")

def menu():
    while True:
        print("\nCarnet d'Adresse - Choisissez une option :")
        print("1: Ajouter un contact")
        print("2: Afficher les contacts")
        print("3: Supprimer un contact")
        print("4: Quitter")

        choix = input("Entrez votre choix :")

        if choix == '1':
            ajouter_contact()
        elif choix == '2':
            afficher_contacts()
        elif choix == '3':
            supprimer_contact()
        elif choix == '4':
            print("Au revoir!")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    menu()