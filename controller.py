import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())


        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                        print(paroleErrate)
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def handleLanguageSelection(self, e):
        print("handle language selection called")
        self._view.txtOut.controls.append(ft.Text(value = "Lingua scelta correttamente: " + self._view.ddLanguage.value))
        self._view.update()

    def handleSearchSelection(self, e):
        print("handle research selection called")
        self._view.txtOut.controls.append(ft.Text(value="Metodo di ricerca scelto correttamente: " + self._view.ddSearchSelection.value))
        self._view.update()

    def handleSpellCheck(self, e):
        print("handle SpellCheck called")

        language = self._view.ddLanguage.value
        txtInput = self._view.txtIn.value
        modality = self._view.ddSearchSelection.value


        if language  == "" :
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text(value="Seleziona lingua !", color = "red"))
            return
        if modality == "":
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text(value="Seleziona modalità !", color="red"))
            return
        if txtInput == "":
            self._view.txtOut.controls.clear()
            self._view.txtOut.controls.append(ft.Text(value="Inserire testo !", color="red"))
            return

        parole, tempo = self.handleSentence(txtInput, language.lower(), modality)

        self._view.txtOut.controls.clear() #pulisco la schermata
        self._view.txtOut.controls.append(ft.Text("Frase inserita: " + txtInput))
        self._view.txtOut.controls.append(ft.Text("Parole errate: " + parole))
        self._view.txtOut.controls.append(ft.Text(f"Tempo trascorso :   {tempo}"))

        self._view.update()

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text


