# ⚡ Hızlı Başlangıç Rehberi

**5 dakikada Test Data Generation API'yi çalıştırıp ilk verilerinizi oluşturun!**

---

## 📋 Ön Koşullar

- ✅ Python 3.10+
- ✅ pip (Python paket yöneticisi)
- ✅ Git (opsiyonel)

---

## 🚀 Step 1: Projeyi Hazırla 

### Seçenek A: Git ile İndir

```bash
git clone https://github.com/TurkerAlbayrak/fastapi-test-data-generator-api.git
```

### Seçenek B: Dosyaları İndir

Dosyaları projeden indirin ve bir klasöre koyun.

---

## 📦 Step 2: Virtual Environment Kur 

```bash
# Linux/Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

---

## 💾 Step 3: Bağımlılıkları Yükle 

```bash
pip install -r requirements.txt
```

---

## 🎯 Step 4: API'yi Başlat 

```bash
python test_data_api_main.py
veya
python -m uvicorn test_data_api_main:app --reload --host 127.0.0.1 --port 8000
```

Çıktı şuna benzer olmalı:

```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Application startup complete
```

✅ **Tebrikler! API çalışıyor!**

---

## 🧪 Step 5: İlk İsteğini Yap (Seçenek Seçin)

### Option A: Browser

Tarayıcıyı aç ve ziyaret et:

```
http://localhost:8000/api/v1/users?count=10
```

Sonuç: 10 rastgele kullanıcı JSON formatında!

### Option B: cURL (Terminal)

```bash
curl "http://localhost:8000/api/v1/users?count=10"
```

### Option C: Python

```python
import requests

response = requests.get(
    "http://localhost:8000/api/v1/users",
    params={"count": 10, "locale": "tr_TR"}
)

users = response.json()
print(users[0])  # İlk kullanıcıyı yazdır
```

### Option D: JavaScript/Node.js

```javascript
fetch('http://localhost:8000/api/v1/users?count=10')
  .then(res => res.json())
  .then(users => console.log(users[0]))
```

---

## 📖 API Dokümantasyonı

Interaktif API dokümantasyonunu aç:

```
http://localhost:8000/docs
```

Burada tüm endpoints'i görüp test edebilirsin!

---

## 🎯 Yaygın Örnekler

### 1️⃣ 50 Ürün Üret

```bash
curl "http://localhost:8000/api/v1/products?count=50&locale=en_US"
```

### 2️⃣ Siparişleri CSV'ye Kaydet

```bash
curl "http://localhost:8000/api/v1/orders?count=100&format=csv" -o orders.csv
```

### 3️⃣ Adresleri JSON'a Kaydet

```bash
curl "http://localhost:8000/api/v1/addresses?count=50&country=US" > addresses.json
```

### 4️⃣ Eksiksiz Veri Seti Üret

```bash
curl "http://localhost:8000/api/v1/complete-dataset?user_count=100&product_count=100&order_count=100"
```

### 5️⃣ Farklı Dile Göre Veri Üret

```bash
# Türkçe
curl "http://localhost:8000/api/v1/users?count=50&locale=tr_TR"

# Almanca
curl "http://localhost:8000/api/v1/users?count=50&locale=de_DE"

# Rusça
curl "http://localhost:8000/api/v1/users?count=50&locale=ru_RU"
```

---

## 🔗 Tüm Endpoints'ler

```
GET  /health                          # API sağlık kontrol
GET  /api/v1/users                    # Kullanıcı verileri
GET  /api/v1/products                 # Ürün verileri
GET  /api/v1/orders                   # Sipariş verileri
GET  /api/v1/addresses                # Adres verileri
GET  /api/v1/companies                # Şirket verileri
GET  /api/v1/complete-dataset         # Eksiksiz veri seti
POST /api/v1/users/batch              # Batch kullanıcı üretimi
```

---

## 📝 Query Parametreleri

Tüm endpoints'e aşağıdaki parametreleri ekleyebilirsin:

| Parametre | Açıklama | Örnek | Varsayılan |
|-----------|----------|-------|-----------|
| `count` | Kaç veri üret | `?count=100` | 10 |
| `locale` | Dil kodu | `?locale=tr_TR` | tr_TR |
| `format` | Çıktı formatı | `?format=csv` | json |
| `category` | Ürün kategorisi | `?category=Electronics` | Random |
| `country` | Ülke kodu | `?country=US` | Locale'ye göre |

---

## 💡 Pratik Kullanım Senaryoları

### 📱 Mobile App Testing

```bash
# 1000 test kullanıcısı oluştur
curl "http://localhost:8000/api/v1/users?count=1000&locale=tr_TR" > test_users.json

# Android/iOS uygulamanızda bu verileri kullanın
```

### 🌐 Web App Testing

```javascript
// React component'inde
import { useEffect, useState } from 'react';

function TestComponent() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/api/v1/users?count=50')
      .then(r => r.json())
      .then(data => setUsers(data));
  }, []);

  return <pre>{JSON.stringify(users, null, 2)}</pre>;
}
```

### 📊 Database Seeding

```python
import requests
import sqlite3

# API'den veri al
response = requests.get('http://localhost:8000/api/v1/products?count=1000')
products = response.json()

# Veritabanına kaydet
conn = sqlite3.connect('test.db')
for product in products:
    conn.execute(
        'INSERT INTO products VALUES (?, ?, ?)',
        (product['id'], product['name'], product['price'])
    )
conn.commit()
```

### 🤖 Automated Testing

```python
import pytest
import requests

def test_api_returns_valid_users():
    response = requests.get('http://localhost:8000/api/v1/users?count=50')
    assert response.status_code == 200
    users = response.json()
    assert len(users) == 50
    
    for user in users:
        assert 'email' in user
        assert '@' in user['email']
```

---

## 🛑 Sorun Giderme

### ❌ "Port 8000 zaten kullanımda"

```bash
# Farklı portu kullan
uvicorn test_data_api_main:app --port 8001
```

### ❌ "Module not found" hatası

```bash
# Bağımlılıkları kontrol et
pip install -r requirements.txt
```

### ❌ "Import error" hatası

Tüm dosyaların aynı klasörde olup olmadığını kontrol et:
- `test_data_api_main.py`
- `generators.py`
- `schemas.py`

### ❌ Endpoint çalışmıyor

API'nin çalışıp çalışmadığını kontrol et:
```bash
curl http://localhost:8000/health
```

Çıktı:
```json
{"status":"healthy","timestamp":"...","version":"1.0.0"}
```

---

## 🎓 Sonraki Adımlar

1. **📚 Detaylı Dokümantasyonu Oku**
   - README.md dosyasını incele
   - ARCHITECTURE.md ile sistem mimarisini öğren

2. **🧪 Tüm Endpoints'i Dene**
   - http://localhost:8000/docs adresindeki Swagger UI'ı kullan

3. **🔧 Kendi Projesine Entegre Et**
   - Uygulamanızdan API'yi çağırın
   - Test verilerini kullanın

4. **📦 Deployment Yap**
   - Heroku'ya deploy et
   - Docker ile containerize et
   - Kendi sunucunuza kur

5. **🤝 Katkı Sağla**
   - Yeni features ekle
   - Bug'ları bildir
   - Dokümantasyonu geliştir

---

## 🆘 Yardım Gerekirse

- 📖 [README.md](./README.md) dosyasını oku
- 🏗️ [ARCHITECTURE.md](./ARCHITECTURE.md) ile mimariye bak
- 🐛 GitHub Issues'te soru sor
- 💬 Discussions bölümünde tartış

---

## ⭐ Başarıyla Kurdum!

Eğer işe yararsadır, lütfen ⭐ yıldız ver!

Happy Coding! 🚀

Türker Albayrak
---

**Created**: May 21, 2024  
