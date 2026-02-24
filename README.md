# <p align="center">🥐 BAKERY AUTOMATION SYSTEM</p>
## <p align="center">☕ Pastahane Satış ve Yönetim Otomasyonu</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PyQt5-41CD52?style=for-the-badge&logo=qt&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite3-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/UI_Design-Qt_Designer-blue?style=for-the-badge&logo=qt" />
</p>

---

# 🚀 PROJECT OVERVIEW (EN)

A comprehensive **Sales and Management Automation** application developed for a bakery. The system offers a dual-layered structure where customers can browse and order products, while administrators manage staff records and financial metrics.

### 🌟 Key Features
* **🔐 Secure Access:** User/Staff registration and login with **Regex** email validation.
* **🛒 Advanced Cart:** Real-time price calculation, item increment/decrement, and QR integration.
* **💼 Admin Dashboard:** Secure management panel for tracking employee salaries and bonuses.
* **📈 Automatic Bonus:** Intelligent system that transfers **5% of each sale** to the respective staff as a bonus.
* **🍰 Categorized Catalog:** Specialized sections for Beverages, Cookies, Breakfast, Sweets, and Ice Cream.

---

# 🚀 PROJE DETAYLARI (TR)

Bir pastahane işletmesi için geliştirilmiş, kapsamlı bir **Satış ve Yönetim Otomasyonu** uygulamasıdır. Kullanıcıların ürün sipariş edebileceği, yöneticilerin ise personel ve prim süreçlerini takip edebileceği modüler bir yapı sunar.

### 🌟 Temel Özellikler
* **🛡️ Kullanıcı ve Güvenlik:** **Regex** doğrulamalı kayıt sistemi ve şifre gizleme fonksiyonlu güvenli giriş.
* **🛒 Satış ve Market:** Kategorize edilmiş ürünler, anlık fiyat hesaplamalı sepet ve QR kod entegrasyonu.
* **💼 Yönetim Paneli:** Çalışanların maaş ve performans verilerini görüntüleme imkanı.
* **📈 Akıllı Prim Sistemi:** Yapılan her satıştan sepet tutarının **%5'i oranında** personele otomatik prim aktarımı.
* **🍰 Geniş Ürün Yelpazesi:** İçecekler, kurabiyeler, kahvaltılıklar, tatlılar ve dondurmalar için özel kategoriler.

---

# 🛠️ TECH STACK & ARCHITECTURE

| Bileşen / Component | Teknoloji / Technology | Kullanım Amacı / Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3.x | Core Application Logic |
| **Interface** | PyQt5 & Qt Designer | User Interface & UX Design |
| **Database** | SQLite3 | User, Admin & Staff Records |
| **Validation** | Regex (re) | Email Format Verification |

---

# 📂 PROJECT STRUCTURE

* `main.py`: Uygulamanın ana mantığı ve veritabanı CRUD işlemleri.
* `py_proje_v5.py`: Qt Designer üzerinden üretilen arayüz kodları.
* `db_kullanici.db`: Tüm kullanıcı ve personel verilerinin tutulduğu SQLite veritabanı.
* `icon/`: Uygulamada kullanılan görsel materyaller ve ikonlar.

---

# 🚀 INSTALLATION & USAGE

1. **Gereksinimleri Yükleyin / Install Requirements:**
   ```bash
   pip install PyQt5
