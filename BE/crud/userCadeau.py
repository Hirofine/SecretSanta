from sqlalchemy.orm import Session
from . import crud  # Importez ici le module crud générique
from models.index import UserCadeaux  # Importez ici le modèle Users

# Fonction spécifique pour créer un utilisateur
def create_userCadeau(db: Session, userCadeau_data):
    return crud.create(db, UserCadeaux, userCadeau_data)

# Fonction spécifique pour obtenir un utilisateur par ID
def get_userCadeau(db: Session, userCadeau_id):
    return crud.read(db, UserCadeaux, userCadeau_id)

# Fonction spécifique pour mettre à jour un utilisateur par ID
def update_userCadeau(db: Session, userCadeau_id, userCadeau_data):
    return crud.update(db, UserCadeaux, userCadeau_id, userCadeau_data)

# Fonction spécifique pour supprimer un utilisateur par ID
def delete_userCadeau(db: Session, userCadeau_id):
    try:
        crud.delete(db, UserCadeaux, userCadeau_id)
        return True  # Indique que l'utilisateur a été supprimé
    except:
        return False  # Indique que l'utilisateur n'a pas été trouvé
