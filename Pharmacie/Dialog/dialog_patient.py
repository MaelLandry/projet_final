# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
from Classes.Patient import Patient
from PyQt5.QtCore import QDate
from datetime import date

import UI_PY.dialog_patient
from UI_PY.dialog_patient import Ui_Dialog
# Importer la boite de dialogue

from PyQt5 import QtWidgets

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ###### Maël Landry
######################################################


def Verifier_numero_patient_existe(p_numero_patient):
    for elt in Patient.ls_patients:
        if elt.numero == p_numero_patient:
            return True
        else:
            return False

class Fenetrepatient(QtWidgets.QDialog, UI_PY.dialog_patient.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetrepatient, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Patient")

    def cacher_erreur_patient(self):
        self.label_erreur_num_patient_existe.setVisible(False)
        self.label_errreur_num_patient_existe_pas.setVisible(False)
        self.label_erreur_num_patient_valider.setVisible(False)
        self.label_erreur_nom_patient.setVisible(False)
        self.label_erreur_prenom_patient.setVisible(False)
        self.label_erreur_date_naiss.setVisible(False)

    def Reinitialiser_text(self):
        """
        Procédure qui permet de réinitialiser les lineEdits
        """
        self.lineEdit_numero_patient.clear()
        self.lineEdit_nom_patient.clear()
        self.lineEdit_prenom_patient.clear()
        self.dateEdit_date_naiss_patient.setDate(QDate(2000, 1, 1))

    @pyqtSlot()
    def on_pushButton_Ajouter_patient_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Ajouter
        """
         # Instancier un objet Eudiant
        patient = Patient()
        # Validation des entrées de l'utilisateur et affichage des messages d'erreur dans les labels d'erreur
        patient.Numero_patient = self.lineEdit_numero_patient.text()
        patient.Nom = self.lineEdit_nom_patient.text()
        patient.Prenom = self.lineEdit_prenom_patient.text()
        patient.Date_naiss = self.dateEdit_date_naiss_patient.date()

        if patient.Numero_patient == 0:
            self.label_erreur_num_patient_valider.setVisible(True)
        else:
            verif_num = Verifier_numero_patient_existe(patient.Numero_patient)
            if verif_num == True :
                self.label_erreur_num_patient_existe.setVisible(True)
        if patient.Nom == "":
            self.label_erreur_nom_patient.setVisible(True)
        if patient.Prenom == "":
            self.label_erreur_prenom_patient.setVisible(True)
        if patient.Date_naiss == "":
            self.label_erreur_date_naiss.setVisible(True)

            # Ajouter le patient à la liste des patients
            Patient.ls_patients.append(patient)
            self.Reinitialiser_text()

    @pyqtSlot()
    def on_pushButton_supprimer_patient_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Supprimer
        """
        patient = Patient()
        # Validation des entrées de l'utilisateur et affichage des messages d'erreur dans les labels d'erreur
        patient.Numero_patient = self.lineEdit_numero_patient.text()
        patient.Nom = self.lineEdit_nom_patient.text()
        patient.Prenom = self.lineEdit_prenom_patient.text()
        patient.Date_naiss = self.dateEdit_date_naiss_patient.date()

        if patient.Numero_patient == 0:
            self.label_erreur_num_patient_valider.setVisible(True)
        else:
            verif_num = Verifier_numero_patient_existe(patient.Numero_patient)
            if verif_num == True:
                self.label_errreur_num_patient_existe_pas.setVisible(True)

        if patient.Nom == "":
            self.label_erreur_nom_patient.setVisible(True)
        if patient.Prenom == "":
            self.label_erreur_prenom_patient.setVisible(True)
        if patient.Date_naiss == "":
            self.label_erreur_date_naiss.setVisible(True)

            # Ajouter le patient à la liste des patients
            Patient.ls_patients.remove(patient)
            self.Reinitialiser_text()
