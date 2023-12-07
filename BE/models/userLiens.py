from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from config.db import Base

# Modèle SQLAlchemy pour la table "Users"
class UserLiens(Base):
    __tablename__ = "UserLien"

    id = Column(Integer, primary_key=True, index=True)
    user1id = Column(Integer, unique=True, index=True)
    user2id = Column(Integer, ForeignKey("Users.id"))
    typeLien = Column(Integer, ForeignKey("Users.id"))

    # Autres colonnes d'utilisateur, ajoutez-les ici si nécessaire

