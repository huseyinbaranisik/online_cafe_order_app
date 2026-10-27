# <p align="center">🥐 BAKERY AUTOMATION SYSTEM</p>
## <p align="center">☕ Bakery Sales and Management Automation</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PyQt5-41CD52?style=for-the-badge&logo=qt&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite3-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/UI-Qt_Designer-blue?style=for-the-badge&logo=qt" />
</p>

<p align="center">
  <a href="#-english"><b>🇬🇧 English</b></a> · <a href="#-türkçe"><b>🇹🇷 Türkçe</b></a>
</p>

---

## 🇬🇧 English

### 📝 About the Project
A desktop automation app built to digitise end-to-end sales and staff management for a bakery. It offers customers a friendly ordering interface, and gives managers a second layer for tracking staff performance and financial data.

Focused on database management and UI integration, the project targets the day-to-day needs of small businesses.

> 🎁 There is no official QR automation, but scan the code in the app — a little surprise is waiting for you!

### 🌟 Key Features
* **🛡️ Secure access:** Login panel with regex-validated sign-up and password protection.
* **🛒 Dynamic cart:** Categorised products (Desserts, Drinks, Breakfast, etc.), live price calculation and QR code support.
* **💼 Admin panel:** A central place to monitor staff salaries, sales counts and bonuses.
* **📈 Automatic bonus calculation:** Credits 5% of every successful sale to the staff member who made it.
* **📊 Data management:** User, staff and order data stored persistently with SQLite3.

### 🛠️ Tech Stack

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3.x | App logic and database operations |
| **UI design** | PyQt5 & Qt Designer | UI/UX design and widget management |
| **Database** | SQLite3 | User, admin and staff records |
| **Validation** | Regex (re) | Email and data format validation |

### 📂 Project Structure
All source files are inside `pastahane_uygulaması.zip`:

* `main.py`: Core app logic and database CRUD operations.
* `py_proje_v5.py` / `ui_proje.ui`: Interface code generated from Qt Designer and its source file.
* `db_kullanici.db`: SQLite database with user and staff data.
* `icon/`: Images and icons used in the app.

### 🚀 Installation and Running

1. **Unzip** `pastahane_uygulaması.zip`.
2. **Install the required library:**
   ```bash
   pip install PyQt5
   ```
3. **Start the app:**
   ```bash
   cd pastahane_uygulaması
   python main.py
   ```

---

## 🇹🇷 Türkçe

### 📝 Proje Hakkında
Bu çalışma, bir pastane işletmesinin uçtan uca satış ve personel yönetimini dijitalleştirmek amacıyla geliştirilmiş bir masaüstü otomasyonudur. Uygulama, müşteriler için kullanıcı dostu bir sipariş arayüzü sunarken, yöneticiler için personel performansı ve finansal verilerin takibini sağlayan çift katmanlı bir mimariye sahiptir.

Veritabanı yönetimi ve kullanıcı arayüzü entegrasyonu odaklı geliştirilen bu proje, küçük ölçekli işletmelerin operasyonel ihtiyaçlarını karşılamayı hedefler.

> 🎁 Resmi bir QR otomasyonu bulunmasa da, uygulamadaki kodu tarattığınızda sizi küçük bir sürpriz bekliyor!

### 🌟 Temel Özellikler
* **🛡️ Güvenli Erişim:** Regex doğrulamalı kayıt sistemi ve şifreleme fonksiyonları içeren giriş paneli.
* **🛒 Dinamik Sepet:** Kategorize edilmiş ürünler (Tatlı, İçecek, Kahvaltı vb.), anlık fiyat hesaplama ve QR kod desteği.
* **💼 Yönetici Paneli:** Personel maaş verilerinin, satış adetlerinin ve primlerin izlenebildiği merkezi kontrol alanı.
* **📈 Otomatik Prim Hesaplama:** Her başarılı satıştan elde edilen tutarın %5'ini ilgili personele prim olarak yansıtan akıllı sistem.
* **📊 Veri Yönetimi:** SQLite3 altyapısı ile kullanıcı, personel ve sipariş verilerinin kalıcı olarak saklanması.

### 🛠️ Teknoloji Yığını

| Bileşen | Teknoloji | Kullanım Amacı |
| :--- | :--- | :--- |
| **Programlama Dili** | Python 3.x | Uygulama Mantığı ve Veritabanı İşlemleri |
| **Arayüz Tasarımı** | PyQt5 & Qt Designer | UI/UX Tasarımı ve Bileşen Yönetimi |
| **Veritabanı** | SQLite3 | Kullanıcı, Yönetici ve Personel Kayıtları |
| **Doğrulama** | Regex (re) | E-posta ve Veri Formatı Doğrulaması |

### 📂 Proje Yapısı
Tüm kaynak dosyalar `pastahane_uygulaması.zip` içindedir:

* `main.py`: Uygulamanın çekirdek mantığı ve veritabanı CRUD işlemleri.
* `py_proje_v5.py` / `ui_proje.ui`: Qt Designer üzerinden üretilen arayüz kodları ve kaynak dosyası.
* `db_kullanici.db`: Kullanıcı ve personel verilerini içeren SQLite veritabanı.
* `icon/`: Uygulama içerisinde kullanılan görsel materyaller ve ikonlar.

### 🚀 Kurulum ve Başlatma

1. `pastahane_uygulaması.zip` dosyasını **zipten çıkarın**.
2. **Gerekli kütüphaneyi yükleyin:**
   ```bash
   pip install PyQt5
   ```
3. **Uygulamayı başlatın:**
   ```bash
   cd pastahane_uygulaması
   python main.py
   ```
