#%%---------------- import kısmı

import sys
import sqlite3
import re

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QLineEdit

from py_proje_v5 import Ui_proje
from PyQt5.QtCore import Qt

#%%---------------- ana class yapısı
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_proje()
        self.ui.setupUi(self)
        
        
        # şifrenin gizlilik ayarı
        self.sifre_oturum_ac_gizli = True
        self.sifre_yonetici_gizli = True
        self.sifre_hesap_olustur_gizli = True
        self.sifre_hesap_olustur_2_gizli = True
               
#%%---------------- veri tabanı yolu 

        # tabloların bulunduğu dosyanın adı ve kısayolu
        self.veritabani_yolu = "db_kullanici.db"

#%%---------------- urun listesi

        # ürünler ile eşleşen group boxlarının isimleri ve katagori dağılımları
        self.urunler = {
            "kahve": {"widget": self.ui.gb_kahve, "kategori": "icecek"},
            "cay": {"widget": self.ui.gb_cay, "kategori": "icecek"},
            "bubble_tea": {"widget": self.ui.gb_bubble_tea, "kategori": "icecek"},
            "cikolatali_kurabiye": {"widget": self.ui.gb_cikolatali_kurabiye, "kategori": "kurabiye"},
            "simit": {"widget": self.ui.gb_simit, "kategori": "tuzlu"},
            "kruvasan": {"widget": self.ui.gb_kruvasan, "kategori": "kahvaltilik"},
            "macarone": {"widget": self.ui.gb_macarone, "kategori": "tatli"},
            "donut": {"widget": self.ui.gb_donut, "kategori": "tatli"},
            "cup_cacke": {"widget": self.ui.gb_cup_cacke, "kategori": "tatli"},
            "karisik_sandivic": {"widget": self.ui.gb_karisik_sandivic, "kategori": ["tuzlu", "kahvaltilik"]},
            "peynirli_sandivic": {"widget": self.ui.gb_peynirli_sandivic, "kategori": ["tuzlu", "kahvaltilik"]},
            "karisik_tost": {"widget": self.ui.gb_karisik_tost, "kategori": ["tuzlu", "kahvaltilik"]},
            "peynrili_tost": {"widget": self.ui.gb_peynirli_tost, "kategori": ["tuzlu", "kahvaltilik"]},
            "tuzlu_kurabiye": {"widget": self.ui.gb_tuzlu_kurabiye, "kategori": ["tuzlu", "kurabiye"]},
            "cilekli_kurabiye": {"widget": self.ui.gb_cilekli_kurabiye, "kategori": ["tatli", "kurabiye"]},
            "cikolatali_dondurma": {"widget": self.ui.gb_cikolatali_dondurma, "kategori": ["tatli", "dondurma"]},
            "cilekli_dondurma": {"widget": self.ui.gb_cilekli_dondurma, "kategori": ["tatli", "dondurma"]},
            "vanilyali_dondurma": {"widget": self.ui.gb_vanilyali_dondurma, "kategori": ["tatli", "dondurma"]},
        }
        
#%%---------------- urun katagorileme işlemi 

        # ürün katagorizaysonu
        self.kategori_listesi = {
            
            "icecek":       ["kahve", "cay", "bubble_tea"],
            "kurabiye":     ["cikolatali_kurabiye", "tuzlu_kurabiye", "cilekli_kurabiye"],
            "kahvaltilik":  ["cay", "simit", "kruvasan", "karisik_sandivic", "peynirli_sandivic", "karisik_tost", "peynrili_tost"],
            "tuzlu":        ["simit", "karisik_sandivic", "peynirli_sandivic", "karisik_tost", "peynrili_tost", "tuzlu_kurabiye"],
            "tatli":        ["macarone", "donut", "cup_cacke", "cilekli_kurabiye","vanilyali_dondurma", "cilekli_dondurma", "cikolatali_dondurma"],
            "dondurma":     ["cikolatali_dondurma", "vanilyali_dondurma", "cilekli_dondurma"],
            
                                }
        
#%%---------------- urun fiyatları 
         # urun fiyatlandırması
        self.urun_fiyatlari = {
            
                                "cay": 10,
                                "kahve": 120,
                                "bubble_tea": 150,
                                
                                "simit": 15,
                                "peynirli_sandivic": 55,
                                "karisik_sandivic": 55,
                                "peynirli_tost": 30,
                                "karisik_tost": 30,
                                "kruvasan": 25,
                                
                                "cikolatali_kurabiye": 10,
                                "cilekli_kurabiye": 10,
                                "tuzlu_kurabiye": 10,
                                
                                "macarone": 20,
                                "donut": 70,
                                "cup_cacke": 70,
                                
                                "cikolatali_dondurma": 60,
                                "vanilyali_dondurma": 60,
                                "cilekli_dondurma": 60
                                
                              }
        
        for urun, fiyat in self.urun_fiyatlari.items():
            
            #ürün adedi arttırma ve azaltma fonkiyonu kısaltılmış
            getattr(self.ui, f"btn_urun_adedi_arttirma_{urun}_market").clicked.connect(lambda _, u=urun, f=fiyat: self.urun_adet_arttir(u, f))
            getattr(self.ui, f"btn_urun_adedi_eksiltme_{urun}_market").clicked.connect(lambda _, u=urun, f=fiyat: self.urun_adet_azalt(u, f))
            
        # toplam sepet tutarının ortlanma işlemi    
        self.ui.le_sepet_tutatri_market.setAlignment(Qt.AlignCenter)
        self.ui.le_sepet_tutatri_sepet.setAlignment(Qt.AlignCenter)
        
#%%---------------- katagori butonları 
        
        # tüm ürünlerin gösterilmesi
        self.tum_urunleri_goster()

        # katagori butonları
        self.kategori_butonlari = [
            
            self.ui.rd_btn_icecek_katagori_market,
            self.ui.rd_btn_tatli_katagori_market,
            self.ui.rd_btn_tuzlu_katagori_market,
            self.ui.rd_btn_dondurma_katagori_market,
            self.ui.rd_btn_kurabiye_katagori_market,
            self.ui.rd_btn_kahvaltilik_katagori_market,
            self.ui.rd_btn_tum_urunler_katagori_market
            
                                  ]
        # katagori seçme işlemi
        for buton in self.kategori_butonlari:
            buton.toggled.connect(self.kategori_secildi)
            
#%%---------------- geçiş butonları 

        self.ui.btn_giris_giris_ekrani.clicked.connect(lambda: self.ui.pencereler.setCurrentIndex(1))
        self.ui.btn_hesap_olustur_giris_ekrani.clicked.connect(lambda: self.ui.pencereler.setCurrentIndex(2))
        self.ui.btn_hesap_olustur_oturum_ac.clicked.connect(lambda: self.ui.pencereler.setCurrentIndex(2))
        self.ui.btn_giris_oturum_yonetici_giris.clicked.connect(self.yonetici_giris)
        self.ui.btn_yonetici_girisi_giris_ekrani.clicked.connect(self.giristen_yoneticiye)
        self.ui.btn_geri_prim_tablo.clicked.connect(self.yoneticiden_girise)
        self.ui.btn_geri_oturum_yonetici_giris.clicked.connect(self.yoneticiden_girise)
        self.ui.btn_onay_sepet.clicked.connect(self.sepeti_onayla_ve_prim_ekle)       
        self.ui.btn_geri_oturum_yonetici_giris.clicked.connect(self.yoneticiden_girise)
        self.ui.btn_geri_hesap_olusturma.clicked.connect(self.geri_hesap_olsutur)
        self.ui.btn_geri_oturum_acma.clicked.connect(self.geri)
        self.ui.btn_onay_market.clicked.connect(self.sepete_git)
        self.ui.btn_red_market.clicked.connect(self.sepet_bosalt)
        self.ui.btn_giris_oturum_yonetici_giris.clicked.connect(self.calisan_bilgilerini_goster)
        self.ui.btn_sifre_goster_oturum_ac.clicked.connect(self.goster_sifre_oturum_ac)
        self.ui.btn_sifre_goster_yonetici_giris.clicked.connect(self.goster_sifre_yonetici)
        self.ui.btn_sifre_goster_hesap_olsuturma.clicked.connect(self.goster_sifre_hesap_olustur)
        self.ui.btn_sifre_goster_hesap_olsuturma_2.clicked.connect(self.goster_sifre_hesap_olustur_2)
        self.ui.btn_hizli_giris_giris_ekrani.clicked.connect(self.hizli_giris)
        self.ui.btn_giris_oturum_ac.clicked.connect(self.giris_yap)
        self.ui.btn_hesap_olustur_hesap_olusturma.clicked.connect(self.hesap_olustur)
        self.ui.btn_geri_sepet.clicked.connect(self.sepetten_markete)
        self.ui.btn_onay_sepet.clicked.connect(self.sepetten_qra)
        self.ui.btn_geri_qr.clicked.connect(self.qrdan_markete)
        
#%%---------------- başlangıçtaki ürün sayısı 

        # başlangıç adetleri
        self.kahve_adet = 0
        self.cay_adet = 0
        self.bubble_tea_adet = 0        
        self.simit_adet = 0
        self.cup_cacke_adet = 0
        self.peynirli_sandivic_adet = 0
        self.karisik_sandivic_adet = 0
        self.peynirli_tost_adet = 0
        self.karisik_tost_adet = 0
        self.kruvasan_adet = 0
        self.cikolatali_kurabiye_adet = 0
        self.cilekli_kurabiye_adet = 0
        self.macarone_adet = 0
        self.tuzlu_kurabiye_adet = 0
        self.donut_adet = 0
        self.cikolatali_dondurma_adet = 0
        self.vanilyali_dondurma_adet = 0
        self.cilekli_dondurma_adet = 0
        self.cup_cacke_adet = 0
        
        self.sepet_tutari_market = 0
        self.sepet_tutari_sepet = 0

        self.cart = {} # sepet kısmı
        
        #onay tuşunun sepet boşken çalışmaması için
        self.ui.btn_onay_market.setEnabled(False)
        
#%%---------------- ürün butınu arttırma pasifleştirme
        
        #tüm ürün adedi azaltma butonlarının erişebilirliğini kısıtlama kısmı
        for urun in self.urunler.keys():
            
            try:
                # sıra ile tüm ürünlerin adedini kontrol etme
                getattr(self.ui, f"btn_urun_adedi_eksiltme_{urun}_market").setEnabled(False)
                adet = getattr(self, f"{urun}_adet", 0)
                getattr(self.ui, f"le_urun_adedi_{urun}_market").setText(str(adet))
                
            except AttributeError:
                pass   
        
#%%---------------- Sepet scroll area içindeki layout 

        #widget kontrol 
        self.sepet_scroll_area_widget = self.ui.scrollAreaWidgetContents_2
        self.sepet_layout = self.sepet_scroll_area_widget.findChild(QtWidgets.QVBoxLayout, "verticalLayout_2")
        
        if self.sepet_layout is None:
            self.sepet_layout = self.sepet_scroll_area_widget.layout()
            
#%%---------------- urun adedi arttırma azaltma

    def urun_adet_arttir(self, urun_adi, fiyat):
        adet_attr = f"{urun_adi}_adet" # çoklu kontorl :D
        yeni_adet = getattr(self, adet_attr) + 1
        setattr(self, adet_attr, yeni_adet) 
        
        #tek tek kontrol ve arttırma 
        line_edit = getattr(self.ui, f"le_urun_adedi_{urun_adi}_market") # yeni adeterli tanıt ayarla
        azalt_buton = getattr(self.ui, f"btn_urun_adedi_eksiltme_{urun_adi}_market")
        
        line_edit.setText(str(yeni_adet)) #yeni adedi yazdır
        azalt_buton.setEnabled(True) # adet 0 dan büyük ve buton aktifleş
        
        self.guncelle_sepet(urun_adi, yeni_adet, fiyat)
        self.guncelle_toplam_tutar(fiyat)
        
#%%---------------- urun adedi azaltma 

    def urun_adet_azalt(self, urun_adi, fiyat):
        adet_attr = f"{urun_adi}_adet"
        mevcut_adet = getattr(self, adet_attr)
        if mevcut_adet > 0:
            yeni_adet = mevcut_adet - 1
            setattr(self, adet_attr, yeni_adet)

            line_edit = getattr(self.ui, f"le_urun_adedi_{urun_adi}_market")
            azalt_buton = getattr(self.ui, f"btn_urun_adedi_eksiltme_{urun_adi}_market")

            line_edit.setText(str(yeni_adet))
        if yeni_adet == 0:
            azalt_buton.setEnabled(False)

        self.guncelle_sepet(urun_adi, yeni_adet, fiyat)
        self.guncelle_toplam_tutar(-fiyat)
        
#%%---------------- sepet fonksiyonu 

    def guncelle_sepet(self, urun_adi, adet, fiyat):
        
        #ürün adedi 0 olunca o ürünün sepetten çıkarılması
        if adet == 0:
            
            if urun_adi in self.cart:
                self.cart.pop(urun_adi)
        else:
            self.cart[urun_adi] = {"adet": adet, "fiyat": fiyat}
        
        #sepetin içini temizleme
        self.sepet_layout_temizle()
        
        for urun, data in self.cart.items():
            box = QtWidgets.QGroupBox(urun)
            h_layout = QtWidgets.QHBoxLayout()

            label_adet = QtWidgets.QLabel(f"Adet: {data['adet']}")
            label_fiyat = QtWidgets.QLabel(f"Fiyat: {data['fiyat']}₺ x {data['adet']} = {data['fiyat']*data['adet']}₺")

            h_layout.addWidget(label_adet)
            h_layout.addWidget(label_fiyat)
            box.setLayout(h_layout)

            self.sepet_layout.addWidget(box)

        self.sepet_layout.addStretch(1)
#%%------------

    def sepet_layout_temizle(self):
        while self.sepet_layout.count():
            item = self.sepet_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
                
#%%---------------- çalışan bilgi gösterimi (GPT)

    def calisan_bilgilerini_goster(self):
        # Layout temizleme
        self.calisan_layout_temizle()
    
        try:
            conn = sqlite3.connect("db_kullanici.db")
            cursor = conn.cursor()
        
            cursor.execute("SELECT * FROM calisan_bilgi")
            calisanlar = cursor.fetchall()
        
            # Sütun adları
            column_names = [desc[0] for desc in cursor.description]
        
            for calisan in calisanlar:
                box = QtWidgets.QGroupBox("Çalışan Bilgisi")
                h_layout = QtWidgets.QVBoxLayout()
            
                for i, bilgi in enumerate(calisan):
                    label = QtWidgets.QLabel(f"{column_names[i]}: {bilgi}")
                    h_layout.addWidget(label)
                
                box.setLayout(h_layout)
                self.ui.verticalLayout_4.addWidget(box)
            
            self.ui.verticalLayout_4.addStretch(1)
            conn.close()
        
        except sqlite3.Error as e:
            print("Veritabanı hatası:", e)
            
#%%----------------
            
    def calisan_layout_temizle(self):
        while self.ui.verticalLayout_4.count():
            item = self.ui.verticalLayout_4.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

                
#%%---------------- toplam tutar değişimi

    def guncelle_toplam_tutar(self, miktar_degisim):
        
        self.sepet_tutari_market += miktar_degisim
        self.sepet_tutari_sepet += miktar_degisim
        
        # tutatın gösterimi
        self.ui.le_sepet_tutatri_market.setText(f"{self.sepet_tutari_market} ₺")
        self.ui.le_sepet_tutatri_sepet.setText(f"{self.sepet_tutari_sepet} ₺")
        
        # yazı ortalama
        self.ui.le_sepet_tutatri_market.setAlignment(Qt.AlignCenter)
        self.ui.le_sepet_tutatri_sepet.setAlignment(Qt.AlignCenter)
        
        #onay tuşunu aktifleştirme
        self.ui.btn_onay_market.setEnabled(self.sepet_tutari_market > 0)
           
#%%---------------- Veritabanı bağlantısı

    def baglanti_olustur(self):
        return sqlite3.connect(self.veritabani_yolu)
    
#%%---------------- ürün gösterimi

    def tum_urunleri_goster(self):
        for urun in self.urunler.values():
            urun["widget"].show()
            
#%%---------------- kategori seçimi fonksiyonu

    def kategori_secildi(self):
        secilen_buton = self.sender()
        if secilen_buton.isChecked():
            #çoklu bıton seçimi
            kategori_adi = secilen_buton.objectName().replace("rd_btn_", "").replace("_katagori_market", "")
            #seçilen ley tümü ise her şeyi göster
            if kategori_adi == "tum_urunler":
                self.tum_urunleri_goster()
            else:
                gosterilecek = self.kategori_listesi.get(kategori_adi, [])
                for urun_adi, urun_bilgisi in self.urunler.items():
                    urun_bilgisi["widget"].setVisible(urun_adi in gosterilecek)

    def sepete_git(self):
        self.ui.pencereler.setCurrentIndex(5)
        
#%%---------------- sepetten markete gitme

    def sepetten_markete(self):
        self.ui.pencereler.setCurrentIndex(3)
        
#%%---------------- sepetten qr'a

    def sepetten_qra(self):
        self.ui.pencereler.setCurrentIndex(4)
           
        
#%%---------------- şarkıyı basa sar
       
    def sarki_sona_geldi(self, status):
        from PyQt5.QtMultimedia import QMediaPlayer
        if status == QMediaPlayer.EndOfMedia:
            self.player.play()
            
            
            
            
#%%---------------- sifre gosterme fonkisyonları      


    def goster_sifre_oturum_ac(self):
        if self.sifre_oturum_ac_gizli:
            self.ui.le_sifre_oturum_ac.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.le_sifre_oturum_ac.setEchoMode(QLineEdit.Password)
        self.sifre_oturum_ac_gizli = not self.sifre_oturum_ac_gizli

    def goster_sifre_hesap_olustur(self):
        if self.sifre_hesap_olustur_gizli:
            self.ui.le_sifre_hesap_olusturma.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.le_sifre_hesap_olusturma.setEchoMode(QLineEdit.Password)
        self.sifre_hesap_olustur_gizli = not self.sifre_hesap_olustur_gizli


    def goster_sifre_hesap_olustur_2(self):
        if self.sifre_hesap_olustur_2_gizli:
            self.ui.le_sifre_tekrar_hesap_olusturma.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.le_sifre_tekrar_hesap_olusturma.setEchoMode(QLineEdit.Password)
        self.sifre_hesap_olustur_2_gizli = not self.sifre_hesap_olustur_2_gizli

    def goster_sifre_yonetici(self):
        if self.sifre_yonetici_gizli:
            self.ui.le_sifre_yonetici_giris.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.le_sifre_yonetici_giris.setEchoMode(QLineEdit.Password)
        self.sifre_yonetici_gizli = not self.sifre_yonetici_gizli
            
#%%---------------- sepeti boşaltma 
    
    def sepet_bosalt(self):
        # Ürün adedi değişkenlerini sıfırla
        for urun in self.urunler.keys():
            setattr(self, f"{urun}_adet", 0)

            try:
                # Arayüzdeki LineEdit alanını sıfırla
                line_edit = getattr(self.ui, f"le_urun_adedi_{urun}_market")
                line_edit.setText("0")
                
            except AttributeError:
                pass  # eğer ilgili LineEdit tanımlı değilse hata verme

            try:
                # Azaltma butonunu pasifleştir
                azalt_buton = getattr(self.ui, f"btn_urun_adedi_eksiltme_{urun}_market")
                azalt_buton.setEnabled(False)
                
            except AttributeError:
                pass  # eğer azaltma butonu yoksa hata verme

        # Sepet bilgilerini sıfırla
        self.cart = {}
        self.sepet_layout_temizle()
        self.guncelle_toplam_tutar(-self.sepet_tutari_market)  # toplamı 0’a çek
        self.sepet_tutari_market = 0
        self.sepet_tutari_sepet = 0

        self.ui.le_sepet_tutatri_market.setText("0")
        self.ui.le_sepet_tutatri_sepet.setText("0")
        self.ui.btn_onay_market.setEnabled(False)

#%%---------------- ZAMAAAAAAN GERİYE AKSIIIIIIIIIIIN

    def tum_siparis_verisini_temizle(self): 
            print("Tüm veriler sıfırlandı.")
            # Ürün adetlerini sıfırlar burası
            for urun in self.urunler.keys():
                setattr(self, f"{urun}_adet", 0)

                try:
                    line_edit = getattr(self.ui, f"le_urun_adedi_{urun}_market")
                    line_edit.setText("0")
                except AttributeError:
                    pass

                try:
                    azalt_buton = getattr(self.ui, f"btn_urun_adedi_eksiltme_{urun}_market")
                    azalt_buton.setEnabled(False)
                except AttributeError:
                    pass

            # Sepeti ve toplam fiyatları sıfırla
            self.cart = {}
            self.sepet_layout_temizle()
            
            self.sepet_tutari_market = 0
            self.sepet_tutari_sepet = 0
            self.ui.le_sepet_tutatri_market.setText("0 ₺")
            self.ui.le_sepet_tutatri_sepet.setText("0 ₺")
            self.ui.le_sepet_tutatri_market.setAlignment(Qt.AlignCenter)
            self.ui.le_sepet_tutatri_sepet.setAlignment(Qt.AlignCenter)
            
            self.ui.btn_onay_market.setEnabled(False)
 
#%%---------------- qr dan markete

    def qrdan_markete(self):
        self.ui.pencereler.setCurrentIndex(3)
        self.tum_siparis_verisini_temizle()
        
        
#%%---------------- giristen_yoneticiye
      
    def giristen_yoneticiye(self):
        self.ui.pencereler.setCurrentIndex(7)

#%%---------------- hesap oluşturma  
 
    def hesap_olustur(self):
        kullanici_adi = self.ui.le_kullanici_adi_hesap_olusturma.text()
        eposta = self.ui.le_eposta_hesap_olusturma.text()
        telefon = self.ui.le_telefon_numarai_hesap_olusturma.text()
        sifre = self.ui.le_sifre_hesap_olusturma.text()
        sifre_tekrar = self.ui.le_sifre_tekrar_hesap_olusturma.text()
        
        kullanici_adi_prim = self.ui.le_kullanici_adi_hesap_olusturma.text()
        telefon_prim = self.ui.le_telefon_numarai_hesap_olusturma.text()

        if not (kullanici_adi and eposta and telefon and sifre and sifre_tekrar):
            QMessageBox.warning(self, "Eksik Bilgi", "Lütfen tüm alanları doldurun!")
            return

        if sifre != sifre_tekrar:
            QMessageBox.warning(self, "Şifre Hatası", "Şifreler uyuşmuyor!")
            return
        
        if not self.kontrol_email(eposta):
            QMessageBox().warning(self, "e posta hatalı", "lütfen geçerli bir e posts griniz")
            return

        baglanti = self.baglanti_olustur()
        cursor = baglanti.cursor()

        try:
            cursor.execute("INSERT INTO kullanicilar (kullanici_adi, eposta, telefon, sifre) VALUES (?, ?, ?, ?)",
                           (kullanici_adi, eposta, telefon, sifre))
            
            cursor.execute("INSERT INTO calisan_bilgi (isim,  telefon, maas, prim ) VALUES (?, ?, 25000,0)",
                           (kullanici_adi_prim, telefon_prim))
            baglanti.commit()
            QMessageBox.information(self, "Başarılı", "Hesap başarıyla oluşturuldu!")
            self.ui.pencereler.setCurrentIndex(0)
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Hata", "Bu kullanıcı adı zaten kayıtlı.")
        finally:
            baglanti.close()
            
            
#%%--------------- gmail kontrol 

    def kontrol_email(self, email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(email_regex, email):
            return True
        else:
            return False
        
            
#%%---------------- hızlı giriş yapma

    # Giriş yapma kontrolü
    def hizli_giris(self):
        self.ui.pencereler.setCurrentIndex(3)
        
#%%---------------- giris yap

    def giris_yap(self):
        
        kullanici_adi = self.ui.le_kullanici_adi_oturum_ac.text()
        sifre = self.ui.le_sifre_oturum_ac.text()

        if not (kullanici_adi and sifre):
            # Hızlı girişte boş gelirse uyarı vermesin
            if self.sender() == self.ui.btn_giris_oturum_ac:
                QMessageBox.warning(self, "Eksik Bilgi", "Kullanıcı adı ve şifreyi giriniz!")
                return

        baglanti = self.baglanti_olustur()
        cursor = baglanti.cursor()

        cursor.execute("SELECT * FROM kullanicilar WHERE kullanici_adi = ? AND sifre = ?", (kullanici_adi, sifre))
        kullanici = cursor.fetchone()
        baglanti.close()

        if kullanici:
            # Başarılı girişte mesaj kutusu gösterme
            self.ui.pencereler.setCurrentIndex(3)
            
        else:
            if self.sender() == self.ui.btn_giris_oturum_ac:
                QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre yanlış!")
                
        self.aktif_kullanici = kullanici_adi
                
#%%---------------- sepeti onaylatıp prim ekleme

    def sepeti_onayla_ve_prim_ekle(self):

        toplam_tutar = sum(urun["fiyat"] * urun["adet"] for urun in self.cart.values())
        prim = int(toplam_tutar * 0.05) 
        

        kullanici_adi = getattr(self, "aktif_kullanici", None)
        if not kullanici_adi:
            QMessageBox.warning(self, "Hata", "Aktif kullanıcı bulunamadı!")
            return
        
        try:
            conn = sqlite3.connect("db_kullanici.db")
            cursor = conn.cursor()
            
            cursor.execute("SELECT prim FROM calisan_bilgi WHERE isim = ?", (kullanici_adi,))
            sonuc = cursor.fetchone()
            
            if sonuc is not None:
                eski_prim = sonuc[0] or 0
                yeni_prim = eski_prim + prim
                
                QMessageBox.information(self, "Başarılı", f"Sepet onaylandı.\n{prim}₺ prim eklendi.")
                
                cursor.execute("UPDATE calisan_bilgi SET prim = ? WHERE isim = ?", (yeni_prim, kullanici_adi))
                conn.commit()
                
        finally:
            conn.close()
#%%---------------- yonetici giris yapınca çalışan fonk

    def yonetici_giris(self):
        kullanici_adi_yonetici = self.ui.le_kullanici_adi_yonetici_giris.text()
        sifre_yonetici = self.ui.le_sifre_yonetici_giris.text()

        if not (kullanici_adi_yonetici and sifre_yonetici):

            if self.sender() == self.ui.btn_giris_oturum_yonetici_giris:
                QMessageBox.warning(self, "Eksik Bilgi", "Kullanıcı adı ve şifreyi giriniz!")
                return

        baglanti = self.baglanti_olustur()
        cursor = baglanti.cursor()
        
        #bu tablo elle hazırlandı unutma 
        cursor.execute("SELECT * FROM yonetici_bilgi WHERE yonetici_adi = ? AND yonetici_sifre = ?", (kullanici_adi_yonetici, sifre_yonetici))
        kullanici = cursor.fetchone()
        baglanti.close()

        if kullanici:

            self.ui.pencereler.setCurrentIndex(6)
            
        else:
            if self.sender() == self.ui.btn_giris_oturum_yonetici_giris:
                QMessageBox.warning(self, "Hata", "Kullanıcı adı veya şifre yanlış!")
        # buraya le temizleme şeyi ekle !!!!!!!!!!!    <---- ekledim kızma nfksdnkdn   
        self.ui.le_kullanici_adi_yonetici_giris.setText("")
        self.ui.le_sifre_yonetici_giris.setText("") 
             
#%%---------------- geri gitme fonksiyonu

    # Geri butonu
    def geri(self):
        mevcut_index = self.ui.pencereler.currentIndex()
        
        if mevcut_index > 0:
            self.ui.pencereler.setCurrentIndex(mevcut_index - 1) #fazla kullanamdım ama olsun :D
            
#%%---------------- yoneticiden girise giden fonksiyon            
    def yoneticiden_girise(self):
        self.ui.pencereler.setCurrentIndex(0)
            
#%%---------------- geri gitme fonksiyonu hesap oluştur

    def geri_hesap_olsutur(self):
        self.ui.pencereler.setCurrentIndex(0) #ana menüye gidenzi
    
#%%---------------- çalıştır

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    window.show()
    sys.exit(app.exec_())
    