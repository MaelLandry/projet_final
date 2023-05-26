# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.dialog_medicament
from PyQt5 import QtWidgets
from Classes.Medicament import Medicament

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################


class Fenetremedicament(QtWidgets.QDialog, UI_PY.dialog_medicament.Ui_Dialog_Medicament):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetremedicament, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Médicament")


    def cacher_erreur_medicament(self):
        self.label_erreur_code_medicament_existe_pas.setVisible(False)
        self.label_erreur_code_medicamen_existe.setVisible(False)
        self.label_erreur_code_medicament_invalide.setVisible(False)
        self.label_erreur_nom_commercial.setVisible(False)
        self.label_erreur_dose_quot_max.setVisible(False)
        self.label_erreur_nom_chimique.setVisible(False)
        self.label_erreur_prix.setVisible(False)
        self.label_erreur_duree_prise_max.setVisible(False)



    @pyqtSlot()
    def on_pushButton_ajouter_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Ajouter
        """
         medicament = Medicament()
         # Validation des entrées de l'utilisateur et affichage des messages d'erreur dans les labels d'erreur
        medicament.Code_medicament = self.lineEdit_numero_medicament.text()
        medicament.Nom_chimique = self.lineEdit_nom_medicament.text()
        medicament.Nom_commercial = self.lineEdit_prenom_medicament.text()
        medicament.Prix = self.dateEdit_date_naiss_medicament.date()

        if medicament.Numero_medicament == 0:
            self.label_erreur_num_medicament_valider.setVisible(True)
        else:
            verif_num = Verifier_numero_medicament_existe(medicament.Numero_medicament)
            if verif_num == True :
                self.label_erreur_num_medicament_existe.setVisible(True)
        if medicament.Nom == "":
            self.label_erreur_nom_medicament.setVisible(True)
        if medicament.Prenom == "":
            self.label_erreur_prenom_medicament.setVisible(True)
        if medicament.Date_naiss == "":
            self.label_erreur_date_naiss.setVisible(True)

            # Ajouter le medicament à la liste des medicaments
            medicament.ls_medicaments.append(medicament)

    @pyqtSlot()
    def on_pushButton_rechercher_clicked(self):
