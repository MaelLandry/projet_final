# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.dialog_fournisseur
from PyQt5 import QtWidgets
from Classes.Fournisseur import Fournisseur

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetrefournisseur(QtWidgets.QDialog, UI_PY.dialog_fournisseur.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetrefournisseur, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Fournisseur")


    @pyqtSlot()
    def on_pushButton_Serialiser_fournisseur_clicked(self):
        #pas fini
        fournisseur = Fournisseur()
        fournisseur.Ls_patient = self.comboBox_numero_patient
        serialisation dans 321 decolage
