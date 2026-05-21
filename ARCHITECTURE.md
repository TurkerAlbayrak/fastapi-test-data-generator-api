# 🏗️ Test Data Generation API - Sistem Mimarisi

## 📐 Genel Mimari Diyagram

```
┌─────────────────────────────────────────────────────────────┐
│                     İstemci Uygulamaları                      │
│  (Web Browser, Mobile App, Backend Service, Automated Tests) │
└──────────────────┬──────────────────────────────────────────┘
                   │
                   │ HTTP/HTTPS
                   │
┌──────────────────▼──────────────────────────────────────────┐
│                   FastAPI Uygulaması                         │
├──────────────────────────────────────────────────────────────┤
│  • CORS Middleware      • Request Validation                 │
│  • Error Handling       • Response Formatting                │
└──────────────────┬──────────────────────────────────────────┘
                   │
        ┌──────────┼──────────┬──────────┐
        │          │          │          │
┌───────▼────┐ ┌──▼──┐ ┌─────▼──┐ ┌────▼────┐
│    API      │ │Route│ │Schema  │ │ Helpers │
│  Endpoints  │ │Layer│ │Validate│ │ Exports │
└───────┬────┘ └──┬──┘ └─────┬──┘ └────┬────┘
        │         │          │         │
        └─────────┼──────────┼─────────┘
                  │          │
        ┌─────────▼──────────▼─────────┐
        │   Business Logic / Services  │
        ├──────────────────────────────┤
        │  UserDataGenerator           │
        │  ProductDataGenerator        │
        │  OrderDataGenerator          │
        │  AddressDataGenerator        │
        │  CompanyDataGenerator        │
        └─────────┬────────────────────┘
                  │
        ┌─────────▼──────────────────┐
        │   Faker Library            │
        │  (Fake Data Generation)    │
        └────────────────────────────┘
```

---

## 🔄 Request/Response Flow

```
1. İstemci İsteği Alınması
   ↓
2. URL Routing (FastAPI)
   ↓
3. Query Parametreleri Validasyonu (Pydantic)
   ↓
4. İş Mantığı (Servis Katmanı)
   ↓
5. Faker ile Veri Üretimi
   ↓
6. Response Formatlama (JSON/CSV/XML)
   ↓
7. HTTP Response Geri Döndürme
```

---

## 📦 Katmanlar (Layers)

### 1️⃣ Presentation Layer (API Endpoints)

**Dosya**: `test_data_api_main.py`

```python
# Görevleri:
- HTTP istekleri dinleme
- Route tanımlama
- Query parametrelerini kabul etme
- Response formatı seçme
- Error handling
```

**Endpoints Yapısı**:
```
GET /api/v1/users
GET /api/v1/products
GET /api/v1/orders
GET /api/v1/addresses
GET /api/v1/companies
GET /api/v1/complete-dataset
POST /api/v1/users/batch
```

### 2️⃣ Business Logic Layer (Services)

**Dosya**: `generators.py`

```python
# Sınıflar:
- UserDataGenerator
- ProductDataGenerator
- OrderDataGenerator
- AddressDataGenerator
- CompanyDataGenerator

# Görevler:
- Veri üretim algoritmaları
- Locale'e göre veri hazırlanması
- Veri geçerliliğini kontrol etme
```

### 3️⃣ Validation Layer (Schemas)

**Dosya**: `schemas.py`

```python
# Pydantic Models:
- UserResponse
- ProductResponse
- OrderResponse
- AddressResponse
- CompanyResponse
- GenerateRequest
- ErrorResponse

# Görevler:
- Input validasyonu
- Output schema tanımı
- Type checking
- Documentation
```

### 4️⃣ External Libraries

```python
# Faker:  Rastgele veri üretimi
# FastAPI: Web framework
# Pydantic: Data validation
# Uvicorn: ASGI server
```

---

## 🔧 Tasarım Desenleri

### 1. Strategy Pattern (Veri Üretimi)

```python
class BaseGenerator:
    """Temel strateji"""
    def generate(self, count, locale, **kwargs):
        raise NotImplementedError

class UserDataGenerator(BaseGenerator):
    def generate(self, count, locale, **kwargs):
        # Kullanıcı veri stratejisi
        
class ProductDataGenerator(BaseGenerator):
    def generate(self, count, locale, **kwargs):
        # Ürün veri stratejisi
```

### 2. Factory Pattern (Generator Üretimi)

```python
# Gelecekte eklenebilir
class GeneratorFactory:
    generators = {
        'user': UserDataGenerator,
        'product': ProductDataGenerator,
        'order': OrderDataGenerator,
    }
    
    @staticmethod
    def create(type_name):
        return GeneratorFactory.generators[type_name]()
```

### 3. Builder Pattern (Kompleks Veri Setleri)

```python
# Gelecekte eklenebilir
class DatasetBuilder:
    def add_users(self, count):
        # Kullanıcı ekle
        return self
    
    def add_products(self, count):
        # Ürün ekle
        return self
    
    def build(self):
        # Tamamını oluştur
        return dataset
```

---

## 🔐 Error Handling & Validation

```python
# 1. Input Validation
- FastAPI Query Parameters ile
- Pydantic Models ile
- Custom validators

# 2. Error Response
{
  "error": "Error message",
  "status_code": 400,
  "timestamp": "2024-05-21T10:30:00"
}

# 3. HTTP Status Codes
- 200: Başarılı
- 400: Kötü istek (invalid parameters)
- 422: Validation error
- 500: Server error
```

---

## 📊 Veri Modelleri

### User Model

```python
{
    "id": UUID,
    "username": str,
    "email": str,
    "first_name": str,
    "last_name": str,
    "phone": str,
    "date_of_birth": ISO8601,
    "gender": str,
    "address": str,
    "city": str,
    "country": str,
    "postal_code": str,
    "company": str,
    "job_title": str,
    "website": str,
    "created_at": ISO8601,
    "is_active": bool,
    "last_login": ISO8601,
    "profile_picture": URL | None,
    "bio": str | None
}
```

### Product Model

```python
{
    "id": UUID,
    "sku": str,
    "name": str,
    "description": str,
    "category": str,
    "price": float,
    "currency": str,
    "discount_percentage": int,
    "stock_quantity": int,
    "weight": float,
    "dimensions": {
        "length": float,
        "width": float,
        "height": float
    },
    "color": str,
    "material": str,
    "manufacturer": str,
    "rating": float,
    "reviews_count": int,
    "is_available": bool,
    "created_at": ISO8601,
    "tags": List[str],
    "image_url": URL | None
}
```

### Order Model

```python
{
    "id": UUID,
    "order_number": str,
    "customer_id": UUID,
    "customer_name": str,
    "customer_email": str,
    "shipping_address": str,
    "billing_address": str,
    "order_date": ISO8601,
    "expected_delivery": ISO8601,
    "actual_delivery": ISO8601 | None,
    "items_count": int,
    "subtotal": float,
    "tax": float,
    "shipping_cost": float,
    "total_amount": float,
    "currency": str,
    "payment_method": str,
    "payment_status": str,
    "order_status": str,
    "notes": str | None,
    "tracking_number": str | None
}
```

---

## 🗂️ Dosya Yapısı (Future)

```
test-data-api/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI app
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py          # Konfigürasyon
│   │   └── settings.py        # Environment vars
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── users.py
│   │   │   │   ├── products.py
│   │   │   │   ├── orders.py
│   │   │   │   ├── addresses.py
│   │   │   │   └── companies.py
│   │   │   └── schemas/
│   │   │       ├── __init__.py
│   │   │       └── models.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── base_generator.py
│   │   ├── user_generator.py
│   │   ├── product_generator.py
│   │   ├── order_generator.py
│   │   ├── address_generator.py
│   │   └── company_generator.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── formatters.py       # JSON/CSV/XML dönüştürme
│   │   └── validators.py       # Custom validators
│   └── exceptions/
│       ├── __init__.py
│       └── custom_exceptions.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py            # Pytest fixtures
│   ├── test_users.py
│   ├── test_products.py
│   ├── test_orders.py
│   └── test_integration.py
├── scripts/
│   ├── __init__.py
│   └── seed_data.py           # Test veri hazırlanması
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── docs/
│   ├── ARCHITECTURE.md        # Bu dosya
│   ├── API.md                 # API dokümantasyonu
│   └── DEPLOYMENT.md          # Deployment rehberi
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── LICENSE
```

---

## 🚀 Scalability (Ölçeklenebilirlik)

### Mevcut Durum (MVP)
- Single instance
- In-memory veri üretimi
- No caching

### Phase 2 - Caching Eklemesi

```python
from functools import lru_cache

@lru_cache(maxsize=128)
def generate_cached_users(count, locale):
    # Aynı parametrelerle istenen verileri cache et
    return user_generator.generate(count, locale)
```

### Phase 3 - Database Eklemesi

```python
# Redis caching
from redis import Redis

cache = Redis(host='localhost', port=6379)

def generate_users_with_cache(count, locale):
    key = f"users:{count}:{locale}"
    cached = cache.get(key)
    if cached:
        return json.loads(cached)
    
    users = user_generator.generate(count, locale)
    cache.set(key, json.dumps(users), ex=3600)
    return users
```

### Phase 4 - Horizontal Scaling

```
Load Balancer (Nginx)
    ↓
┌───────────────────────────┐
│  API Instance 1 (Port 8001)│
│  API Instance 2 (Port 8002)│
│  API Instance 3 (Port 8003)│
└────────┬────────┬────────┘
         │        │
         ▼        ▼
    Redis Cache  Database
```

---

## 🔒 Security Best Practices

### 1. Input Validation
```python
# Pydantic ile otomatik validation
count: int = Query(10, ge=1, le=1000)  # 1-1000 arasında
```

### 2. CORS Protection
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://example.com"],  # Whitelist
    allow_methods=["GET"],
    allow_headers=["*"],
)
```

### 3. Rate Limiting (Gelecek)
```python
from slowapi import Limiter

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.get("/api/v1/users")
@limiter.limit("100/minute")
async def generate_users(...):
    pass
```

### 4. API Key Authentication (Gelecek)
```python
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="X-API-Key")

async def verify_api_key(api_key: str = Depends(api_key_header)):
    if api_key not in VALID_API_KEYS:
        raise HTTPException(status_code=403)
    return api_key
```

---

## 📈 Performance Optimization

### 1. Response Compression
```python
from fastapi.middleware.gzip import GZIPMiddleware

app.add_middleware(GZIPMiddleware, minimum_size=1000)
```

### 2. Async Operations
```python
@app.get("/api/v1/users")
async def generate_users(...):  # async ile non-blocking
    users = await generate_users_async()
    return users
```

### 3. Batch Processing
```python
# Birden fazla isteği paralel işle
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=4)

def generate_users_batch(configs):
    results = []
    with executor:
        for config in configs:
            result = executor.submit(
                user_generator.generate,
                config.count,
                config.locale
            )
            results.append(result)
    return [r.result() for r in results]
```

---

## 🧪 Testing Strategy

### Unit Tests
```python
# Generators'ı test et
def test_user_generator_creates_valid_emails():
    generator = UserDataGenerator()
    users = generator.generate(10)
    for user in users:
        assert "@" in user["email"]
```

### Integration Tests
```python
# API endpoints'i test et
def test_users_endpoint():
    response = client.get("/api/v1/users?count=10")
    assert response.status_code == 200
    assert len(response.json()) == 10
```

### Load Tests
```python
# Performance kontrol
from locust import HttpUser, task

class APIUser(HttpUser):
    @task
    def get_users(self):
        self.client.get("/api/v1/users?count=100")
```

---

## 📊 Monitoring & Logging

```python
import logging

logger = logging.getLogger(__name__)

@app.get("/api/v1/users")
async def generate_users(count: int):
    logger.info(f"Generating {count} users")
    try:
        users = user_generator.generate(count)
        logger.info(f"Successfully generated {count} users")
        return users
    except Exception as e:
        logger.error(f"Error generating users: {str(e)}")
        raise
```

### Log Levels
```
DEBUG: Detaylı bilgi (development)
INFO: Genel bilgi
WARNING: Uyarı
ERROR: Hata
CRITICAL: Kritik hata
```

---

## 🔄 CI/CD Pipeline

```yaml
name: CI/CD

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
      - run: pip install -r requirements.txt
      - run: pytest
      - run: flake8 app/
      
  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v2
      - run: docker build -t test-data-api .
      - run: docker push yourregistry/test-data-api
```

---


## 🎓 Öğrenme Kaynakları

- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Faker Documentation](https://faker.readthedocs.io/)
- [Pydantic Validation](https://docs.pydantic.dev/)
- [System Design](https://en.wikipedia.org/wiki/Software_architecture)

---

**Document Version**: 1.0  
**Author**: Türker Albayrak
