from .student import Utilisateur


def enregistrer_utilisateur(session, name,lastname, password, role):
    nouvel_utilisateur = Utilisateur(name=name, lastname=lastname, password=password, role=role)
    nouvel_utilisateur.set_password(password)  # Hache le mot de passe
    session.add(nouvel_utilisateur)
    session.commit()


    

