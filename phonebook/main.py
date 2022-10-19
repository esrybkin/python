from os.path import exists
import ui
import save_read
from save_read import creating
from save_read import writing_scv
from save_read import writing_txt

path = 'Phonebook\Phonebook.csv'
valid = exists(path)
if not valid:
    creating()

writing_scv()
writing_txt()