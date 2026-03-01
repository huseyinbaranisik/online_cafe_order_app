# <p align="center">🥐 BAKERY AUTOMATION SYSTEM</p>
## <p align="center">☕ Pastahane Satış ve Yönetim Otomasyonu</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PyQt5-41CD52?style=for-the-badge&logo=qt&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite3-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/Arayüz-Qt_Designer-blue?style=for-the-badge&logo=qt" />
</p>

---

### 📝 PROJE HAKKINDA
Bu çalışma, bir pastane işletmesinin uçtan uca satış ve personel yönetimini dijitalleştirmek amacıyla geliştirilmiş bir masaüstü otomasyonudur. Uygulama, müşteriler için kullanıcı dostu bir sipariş arayüzü sunarken, yöneticiler için personel performansı ve finansal verilerin takibini sağlayan çift katmanlı bir mimariye sahiptir.

Veritabanı yönetimi ve kullanıcı arayüzü entegrasyonu odaklı geliştirilen bu proje, küçük ölçekli işletmelerin operasyonel ihtiyaçlarını karşılamayı hedefler.

### 🌟 Temel Özellikler
* **🛡️ Güvenli Erişim:** Regex doğrulamalı kayıt sistemi ve şifreleme fonksiyonları içeren giriş paneli.
* **🛒 Dinamik Sepet:** Kategorize edilmiş ürünler (Tatlı, İçecek, Kahvaltı vb.), anlık fiyat hesaplama ve QR kod desteği.
* **💼 Yönetici Paneli:** Personel maaş verilerinin, satış adetlerinin ve primlerin izlenebildiği merkezi kontrol alanı.
* **📈 Otomatik Prim Hesaplama:** Her başarılı satıştan elde edilen tutarın %5'ini ilgili personele prim olarak yansıtan akıllı sistem.
* **📊 Veri Yönetimi:** SQLite3 altyapısı ile kullanıcı, personel ve sipariş verilerinin kalıcı olarak saklanması.

---

### 🛠️ TEKNOLOJİ YIĞINI

| Bileşen | Teknoloji | Kullanım Amacı |
| :--- | :--- | :--- |
| **Programlama Dili** | Python 3.x | Uygulama Mantığı ve Veritabanı İşlemleri |
| **Arayüz Tasarımı** | PyQt5 & Qt Designer | UI/UX Tasarımı ve Bileşen Yönetimi |
| **Veritabanı** | SQLite3 | Kullanıcı, Yönetici ve Personel Kayıtları |
| **Doğrulama** | Regex (re) | E-posta ve Veri Formatı Doğrulaması |

---

### 📂 PROJE YAPISI

* `main.py`: Uygulamanın çekirdek mantığı ve veritabanı CRUD işlemleri.
* `ui_interface.py`: Qt Designer üzerinden üretilen arayüz kodları.
* `database.db`: Kullanıcı ve personel verilerini içeren SQLite veritabanı.
* `assets/`: Uygulama içerisinde kullanılan görsel materyaller ve ikonlar.

---

### 🚀 KURULUM VE BAŞLATMA

1. **Gerekli kütüphaneleri yükleyin:**
   ```bash
   pip install PyQt5
