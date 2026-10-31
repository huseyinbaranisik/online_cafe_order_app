###

from PyQt5 import uic

with open("py_proje_v5.py",'w', encoding="utf-8") as fout:
    uic.compileUi("ui_proje.ui", fout)

