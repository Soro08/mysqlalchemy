from sqlalchemy.orm.exc import NoResultFound
from .student import Utilisateur
import pickle, os

SESSION_FILE = "keys/sessions.pkl"


class Authentication:
    def __init__(self, session):
        self.session = session


def authenticate_user(session, name, password):
    try:
        # Récupérer l'utilisateur par son nom d'utilisateur
        utilisateur = session.query(Utilisateur).filter_by(name=name).one()

        # Vérifier le mot de passe
        if utilisateur.check_password(password):
            return utilisateur  # Authentification réussie
    except NoResultFound:
        pass  # L'utilisateur n'existe pas

    return None  # Authentification échouée


def sauvegarder_session(session_id):
    # Fonction pour sauvegarder la session
    with open(SESSION_FILE, "wb") as file:
        pickle.dump(session_id, file)


def recuperer_session():
    # Fonction pour récupérer la session
    try:
        with open(SESSION_FILE, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return None


def authentification_initiale(session, name, password):
    # Authentification initiale
    utilisateur = authenticate_user(session, name, password)
    if utilisateur:
        session_id = f"{name}_{utilisateur.id}"  # Créer un ID de session unique
        sauvegarder_session(session_id)
        print("Authentification réussie.")
        return utilisateur.id
    else:
        print("Authentification échouée.")
        return None


def auto_login(session):
    # Vérification de l'authentification au lancement suivant
    session_id = recuperer_session()
    if session_id:
        return session_id.split("_")[1]
    else:
        print("Aucune session trouvée. Veuillez vous authentifier.")
        return None


def is_admin(session, user_id):
    utilisateur = session.query(Utilisateur).filter_by(id=user_id).one()
    if utilisateur:
        return utilisateur.role
    else:
        return None


def logout_user():
    if os.path.exists(SESSION_FILE):
        os.remove(SESSION_FILE)
    print("User has been succefull logout!")


def admin_required(session):
    return auto_login(session) and is_admin(session, auto_login(session)) == "admin"
