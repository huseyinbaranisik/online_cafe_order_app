"""Drives the real PyQt5 app (pastahane_uygulaması/main.py) without showing it and saves screenshots.

A copy of the app folder is used, so the demo database in the repository is not changed by the run.
Message boxes are recorded instead of opened, so nothing waits for a click.

usage: python tools/capture_app.py <out_dir>      (needs PyQt5; writes frames/NNNN.png and named shots)
Flow: welcome -> log in as demo user "ayse" -> add products -> cart -> confirm (5 % bonus) -> QR page
      -> admin login "yonetici" -> staff bonus table.
"""
import os, shutil, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.abspath(sys.argv[1])
os.makedirs(os.path.join(OUT, "frames"), exist_ok=True)
os.environ.setdefault("QT_SCALE_FACTOR", "2")

work = os.path.join(tempfile.mkdtemp(), "app")
shutil.copytree(os.path.join(ROOT, "pastahane_uygulaması"), work)
os.chdir(work)
sys.path.insert(0, work)

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMessageBox

messages = []
QMessageBox.information = lambda parent, title, text, *a, **k: messages.append(("info", title, text))
QMessageBox.warning = lambda parent, title, text, *a, **k: messages.append(("warning", title, text))

app = QApplication(sys.argv)
import main  # the app module; its __main__ block does not run on import

win = main.MainWindow()
win.setAttribute(Qt.WA_DontShowOnScreen)
win.resize(472, 840)
win.show()
app.processEvents()
n = 0

def grab(repeat=1, name=None):
    global n
    app.processEvents()
    img = win.grab()
    for _ in range(repeat):
        img.save(os.path.join(OUT, "frames", f"{n:04d}.png")); n += 1
    if name:
        img.save(os.path.join(OUT, f"{name}.png"))

def click(button, hold=6):
    button.click(); grab(hold)

def type_into(line_edit, text):
    line_edit.setText("")
    for i in range(1, len(text) + 1):
        line_edit.setText(text[:i]); grab()

ui = win.ui
grab(10, "welcome")
click(ui.btn_giris_giris_ekrani)
type_into(ui.le_kullanici_adi_oturum_ac, "ayse")
type_into(ui.le_sifre_oturum_ac, "demo123")
grab(4)
click(ui.btn_giris_oturum_ac, hold=8)
grab(1, "shop")
for product, times in [("cay", 2), ("vanilyali_dondurma", 1), ("cilekli_dondurma", 1)]:  # the first three cards on screen
    for _ in range(times):
        click(getattr(ui, f"btn_urun_adedi_arttirma_{product}_market"), hold=3)
grab(6, "shop_filled")
click(ui.btn_onay_market, hold=12)
grab(1, "cart")
click(ui.btn_onay_sepet, hold=12)
grab(1, "qr")
ui.pencereler.setCurrentIndex(0); grab(4)
click(ui.btn_yonetici_girisi_giris_ekrani)
type_into(ui.le_kullanici_adi_yonetici_giris, "yonetici")
type_into(ui.le_sifre_yonetici_giris, "admin123")
grab(4)
click(ui.btn_giris_oturum_yonetici_giris, hold=16)
grab(1, "staff")
print(n, "frames; messages:", messages)
