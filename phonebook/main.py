from os.path import exists
import save_read as sv
import ui


path = 'Phonebook.csv'
valid = exists(path)
if not valid:
    sv.creating()
sv.writing_scv()
sv.writing_txt()
ui.read_csv("Phonebook.csv")