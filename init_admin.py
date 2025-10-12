#!/usr/bin/env python3
import os
import sys

# Ajouter le chemin de Superset
sys.path.insert(0, '/app')

from superset import create_app
from superset.extensions import db
from superset.models.core import User
from superset.models.roles import Role
from flask_appbuilder.security.sqla.models import User as FABUser

# Créer l'application
app = create_app()

with app.app_context():
    # Vérifier si l'admin existe déjà
    admin_user = db.session.query(FABUser).filter_by(username='admin').first()
    
    if not admin_user:
        # Créer l'utilisateur admin
        admin_user = FABUser()
        admin_user.username = 'admin'
        admin_user.email = 'admin@example.com'
        admin_user.first_name = 'Admin'
        admin_user.last_name = 'User'
        admin_user.active = True
        admin_user.password = 'pbkdf2:sha256:600000$your_salt$your_hash'
        
        # Définir le mot de passe (admin)
        admin_user.set_password('admin')
        
        # Ajouter à la base de données
        db.session.add(admin_user)
        db.session.commit()
        
        # Obtenir le rôle admin
        admin_role = db.session.query(Role).filter_by(name='Admin').first()
        if admin_role:
            admin_user.roles.append(admin_role)
            db.session.commit()
        
        print("Admin user created successfully!")
    else:
        print("Admin user already exists!")
    
    print("Initialization completed!")
