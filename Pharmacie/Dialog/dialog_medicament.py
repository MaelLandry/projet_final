# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.dialog_medicament
from PyQt5 import QtWidgets
from Classes.Medicament import Medicament
from Classes.Antibiotique import Antibiotique
from Classes.Analgesique import Analgesique

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

    def Reinitialiser_text(self):
        """
        Procédure qui permet de réinitialiser les lineEdits
        """
        self.lineEdit_prix.clear()
        self.lineEdit_nom_chimique.clear()
        self.lineEdit_nom_commercial.clear()
        self.lineEdit_code_medicament.clear()
        self.lineEdit_dose_quot_max.clear()
        self.lineEdit_duree_prise_max.clear()




    @pyqtSlot()
    def on_pushButton_ajouter_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Ajouter
        """
        medicament = Medicament()
         # Validation des entrées de l'utilisateur et affichage des messages d'erreur dans les labels d'erreur
        medicament.Code_medicament = self.lineEdit_prix.text()
        medicament.Nom_chimique = self.lineEdit_nom_chimique.text()
        medicament.Nom_commercial = self.lineEdit_nom_commercial.text()
        medicament.Prix = self.lineEdit_code_medicament.text()
        Antibiotique.Duree_prix_max = self.lineEdit_nom_commercial.text()
        Analgesique.Dose_quot_max = self.lineEdit_code_medicament.text()

        #Pas fini
        if medicament.Code_medicament == 0:
            self.label_erreur_code_medicament_existe_pas.setVisible(True)
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
            self.Reinitialiser_text()

    @pyqtSlot()
    def on_pushButton_rechercher_clicked(self):
        Medicament.Prix = self.lineEdit_code_medicament.text()
        Antibiotique.Duree_prix_max = self.lineEdit_nom_commercial.text()
        Analgesique.Dose_quot_max = self.lineEdit_code_medicament.text()

        if...


        for elt in Medicament.ls_medicaments:

