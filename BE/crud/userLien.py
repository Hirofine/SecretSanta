from sqlalchemy.orm import Session
from . import crud  # Importez ici le module crud générique
from models.index import UserLiens  # Importez ici le modèle Users

# Fonction spécifique pour créer un utilisateur
def create_userLien(db: Session, userLien_data):
    return crud.create(db, UserLiens, userLien_data)

# Fonction spécifique pour obtenir un utilisateur par ID
def get_userLien(db: Session, userLien_id):
    return crud.read(db, UserLiens, userLien_id)

# Fonction spécifique pour mettre à jour un utilisateur par ID
def update_userLien(db: Session, userLien_id, userLien_data):
    return crud.update(db, UserLiens, userLien_id, userLien_data)

# Fonction spécifique pour supprimer un utilisateur par ID
def delete_userLien(db: Session, userLien_id):
    try:
        crud.delete(db, UserLiens, userLien_id)
        return True  # Indique que l'utilisateur a été supprimé
    except:
        return False  # Indique que l'utilisateur n'a pas été trouvé
