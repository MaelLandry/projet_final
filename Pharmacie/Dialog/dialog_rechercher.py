# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.dialog_recherche
from PyQt5 import QtWidgets
from Classes.Fournisseur import Fournisseur

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################


class Fenetrerechercher(QtWidgets.QDialog, UI_PY.dialog_recherche.Ui_Dialog_Recherche):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetrerechercher, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Rechercher")
        Fournisseur.ls_fournisseur = self.comboBox_nom_fournisseur

    @pyqtSlot()
    def on_pushButton_Afficher_clicked(self):
        #pas fini
        fournisseur = Fournisseur()
        fournisseur.Ls_patient = self.listView_list_patients_fournisseur

