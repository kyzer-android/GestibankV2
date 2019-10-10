#Classe Client  héritant du compte User et contenant les methodes:
#Afficher les compte bancaires,Réaliser des virements,afficher historique des transaction
#sur un mois donné,imprimer des transactions
from webapp import db
from webapp.gestibank.models.user import User
from flask import flash
from webapp.extension import db
from webapp.gestibank.models.CompteBancaire import TypeCompte, Comptes

class Client(User):
    __tablename__ = 'client'
    id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    tel = db.Column(db.String(20))
    adresse = db.Column(db.String(140))
    justificatif = db.Column(db.String(20))
    id_agent = db.Column(db.String(50), db.ForeignKey('agent.id'))
    compte = db.relationship('Comptes', backref='compte', primaryjoin='Client.id==Comptes.id_client', lazy='dynamic')

    __mapper_args__ = {
        'polymorphic_identity':'client',
    }

    def to_dict(self):
        return {
                "id": self.id,
                "nom":self.nom,
                "prenom":self.prenom,
                "email":self.email,
                "tel": self.tel,
                "adresse": self.adresse,
                "justificatif": self.justificatif
                }

    def affche_compte(self):
        return self.compte.query.all()


    def lister_comptes(self):
        comptes=Comptes.query.filter_by(id_client=self.id).all()
        list_comptes=[]
        for cpt in comptes:
            list_comptes.append(cpt.to_dict())
        return list_comptes

    def virement_d(self, montant):
        if (self.solde < montant):
            return flash("Solde insufissant pour effectuer le virement")
        else:
            self.solde = (self.solde) - (montant)
            print("Opération effectuer avec succés ")
            return self.solde