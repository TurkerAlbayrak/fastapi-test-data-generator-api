"""
Data Generators - Faker kütüphanesi ile test verisi üretme
"""

from faker import Faker
from typing import List, Optional
from datetime import datetime, timedelta
import random
import uuid


class BaseGenerator:
    """Tüm generatorlar için temel sınıf"""
    
    def __init__(self):
        self.fake = Faker()
    
    def set_locale(self, locale: str):
        """Faker'ın dilini ayarla"""
        try:
            self.fake = Faker(locale)
        except Exception:
            print(f"Warning: Locale {locale} not supported, using default")
            self.fake = Faker('en_US')
    
    def generate(self, count: int, locale: str = "en_US", **kwargs) -> List[dict]:
        """Türetilecek metot"""
        raise NotImplementedError


class UserDataGenerator(BaseGenerator):
    """Kullanıcı verileri üreten sınıf"""
    
    def generate(self, count: int, locale: str = "tr_TR", **kwargs) -> List[dict]:
        """Rastgele kullanıcı verileri üret"""
        self.set_locale(locale)
        users = []
        
        for _ in range(count):
            user = {
                "id": str(uuid.uuid4()),
                "username": self.fake.user_name(),
                "email": self.fake.email(),
                "first_name": self.fake.first_name(),
                "last_name": self.fake.last_name(),
                "phone": self.fake.phone_number(),
                "date_of_birth": self.fake.date_of_birth(minimum_age=18, maximum_age=80).isoformat(),
                "gender": random.choice(["M", "F", "Other"]),
                "address": self.fake.address().replace('\n', ', '),
                "city": self.fake.city(),
                "country": self.fake.country(),
                "postal_code": self.fake.postcode(),
                "company": self.fake.company(),
                "job_title": self.fake.job(),
                "website": self.fake.url(),
                "created_at": (datetime.utcnow() - timedelta(days=random.randint(1, 365))).isoformat(),
                "is_active": random.choice([True, False]),
                "last_login": (datetime.utcnow() - timedelta(days=random.randint(0, 30))).isoformat(),
                "profile_picture": self.fake.image_url(),
                "bio": self.fake.text(max_nb_chars=200),
            }
            users.append(user)
        
        return users


class ProductDataGenerator(BaseGenerator):
    """Ürün verileri üreten sınıf"""
    
    CATEGORIES = [
        "Electronics",
        "Clothing",
        "Home & Garden",
        "Sports & Outdoors",
        "Books",
        "Health & Beauty",
        "Toys & Games",
        "Food & Beverages",
        "Automotive",
        "Office Supplies"
    ]
    
    def generate(
        self,
        count: int,
        locale: str = "tr_TR",
        category: Optional[str] = None,
        **kwargs
    ) -> List[dict]:
        """Rastgele ürün verileri üret"""
        self.set_locale(locale)
        products = []
        
        for _ in range(count):
            selected_category = category or random.choice(self.CATEGORIES)
            price = round(random.uniform(10, 1000), 2)
            
            product = {
                "id": str(uuid.uuid4()),
                "sku": self.fake.ean13(),
                "name": self.fake.word() + " " + self.fake.word(),
                "description": self.fake.text(max_nb_chars=300),
                "category": selected_category,
                "price": price,
                "currency": "USD",
                "discount_percentage": random.choice([0, 5, 10, 15, 20, 25, 30]),
                "stock_quantity": random.randint(0, 500),
                "weight": round(random.uniform(0.1, 50), 2),
                "dimensions": {
                    "length": round(random.uniform(1, 100), 2),
                    "width": round(random.uniform(1, 100), 2),
                    "height": round(random.uniform(1, 100), 2)
                },
                "color": random.choice(["Red", "Blue", "Green", "Black", "White", "Silver"]),
                "material": random.choice(["Plastic", "Metal", "Wood", "Fabric", "Leather"]),
                "manufacturer": self.fake.company(),
                "rating": round(random.uniform(1, 5), 1),
                "reviews_count": random.randint(0, 1000),
                "is_available": random.choice([True, False]),
                "created_at": (datetime.utcnow() - timedelta(days=random.randint(1, 365))).isoformat(),
                "tags": [self.fake.word() for _ in range(random.randint(1, 5))],
                "image_url": self.fake.image_url(),
            }
            products.append(product)
        
        return products


class OrderDataGenerator(BaseGenerator):
    """Sipariş verileri üreten sınıf"""
    
    STATUS_CHOICES = ["Pending", "Processing", "Shipped", "Delivered", "Cancelled", "Returned"]
    PAYMENT_METHODS = ["Credit Card", "Debit Card", "PayPal", "Bank Transfer", "Cryptocurrency"]
    
    def generate(self, count: int, locale: str = "tr_TR", **kwargs) -> List[dict]:
        """Rastgele sipariş verileri üret"""
        self.set_locale(locale)
        orders = []
        
        for _ in range(count):
            order_date = datetime.utcnow() - timedelta(days=random.randint(1, 180))
            items_count = random.randint(1, 5)
            item_price = round(random.uniform(50, 500), 2)
            subtotal = round(item_price * items_count, 2)
            tax = round(subtotal * 0.1, 2)
            shipping = round(random.uniform(5, 50), 2)
            total = round(subtotal + tax + shipping, 2)
            
            order = {
                "id": str(uuid.uuid4()),
                "order_number": f"ORD-{random.randint(100000, 999999)}",
                "customer_id": str(uuid.uuid4()),
                "customer_name": self.fake.name(),
                "customer_email": self.fake.email(),
                "shipping_address": self.fake.address().replace('\n', ', '),
                "billing_address": self.fake.address().replace('\n', ', '),
                "order_date": order_date.isoformat(),
                "expected_delivery": (order_date + timedelta(days=random.randint(3, 14))).isoformat(),
                "actual_delivery": (order_date + timedelta(days=random.randint(3, 14))).isoformat() if random.choice([True, False]) else None,
                "items_count": items_count,
                "subtotal": subtotal,
                "tax": tax,
                "shipping_cost": shipping,
                "total_amount": total,
                "currency": "USD",
                "payment_method": random.choice(self.PAYMENT_METHODS),
                "payment_status": random.choice(["Pending", "Completed", "Failed", "Refunded"]),
                "order_status": random.choice(self.STATUS_CHOICES),
                "notes": self.fake.text(max_nb_chars=200) if random.choice([True, False]) else None,
                "tracking_number": self.fake.bothify(text='????-####-####') if random.choice([True, False]) else None,
            }
            orders.append(order)
        
        return orders


class AddressDataGenerator(BaseGenerator):
    """Adres verileri üreten sınıf"""
    
    COUNTRY_LOCALES = {
        "TR": "tr_TR",
        "US": "en_US",
        "GB": "en_GB",
        "DE": "de_DE",
        "FR": "fr_FR",
        "IT": "it_IT",
    }
    
    def generate(
        self,
        count: int,
        locale: str = "tr_TR",
        country: str = "TR",
        **kwargs
    ) -> List[dict]:
        """Rastgele adres verileri üret"""
        country_locale = self.COUNTRY_LOCALES.get(country, locale)
        self.set_locale(country_locale)
        
        addresses = []
        
        for _ in range(count):
            address = {
                "id": str(uuid.uuid4()),
                "street_address": self.fake.street_address(),
                "city": self.fake.city(),
                "state_province": self.fake.state(),
                "postal_code": self.fake.postcode(),
                "country": country,
                "country_full_name": self.fake.country(),
                "latitude": round(random.uniform(-90, 90), 6),
                "longitude": round(random.uniform(-180, 180), 6),
                "phone": self.fake.phone_number(),
                "is_default": random.choice([True, False]),
                "address_type": random.choice(["Residential", "Commercial", "Billing", "Shipping"]),
                "created_at": (datetime.utcnow() - timedelta(days=random.randint(1, 365))).isoformat(),
            }
            addresses.append(address)
        
        return addresses


class CompanyDataGenerator(BaseGenerator):
    """Şirket verileri üreten sınıf"""
    
    INDUSTRIES = [
        "Technology",
        "Finance",
        "Healthcare",
        "Retail",
        "Manufacturing",
        "Telecommunications",
        "Energy",
        "Transportation",
        "Construction",
        "Education",
        "Media & Entertainment",
        "Real Estate"
    ]
    
    def generate(
        self,
        count: int,
        locale: str = "tr_TR",
        industry: Optional[str] = None,
        **kwargs
    ) -> List[dict]:
        """Rastgele şirket verileri üret"""
        self.set_locale(locale)
        companies = []
        
        for _ in range(count):
            selected_industry = industry or random.choice(self.INDUSTRIES)
            
            company = {
                "id": str(uuid.uuid4()),
                "name": self.fake.company(),
                "industry": selected_industry,
                "website": self.fake.url(),
                "email": self.fake.company_email(),
                "phone": self.fake.phone_number(),
                "founded_year": random.randint(1980, 2024),
                "employee_count": random.choice(["1-10", "11-50", "51-200", "201-500", "500+"]),
                "revenue": round(random.uniform(100000, 10000000), 2),
                "currency": "USD",
                "headquarters": self.fake.address().replace('\n', ', '),
                "city": self.fake.city(),
                "country": self.fake.country(),
                "ceo_name": self.fake.name(),
                "description": self.fake.text(max_nb_chars=300),
                "logo_url": self.fake.image_url(),
                "social_media": {
                    "linkedin": f"https://linkedin.com/company/{self.fake.slug()}",
                    "twitter": f"https://twitter.com/{self.fake.user_name()}",
                    "facebook": f"https://facebook.com/{self.fake.slug()}",
                },
                "certifications": [self.fake.word() for _ in range(random.randint(0, 3))],
                "is_verified": random.choice([True, False]),
                "created_at": (datetime.utcnow() - timedelta(days=random.randint(1, 365))).isoformat(),
            }
            companies.append(company)
        
        return companies


# Convenience functions
def generate_users(count: int = 100, locale: str = "tr_TR") -> List[dict]:
    """Hızlı kullanıcı veri üretimi"""
    generator = UserDataGenerator()
    return generator.generate(count=count, locale=locale)


def generate_products(count: int = 100, locale: str = "tr_TR", category: Optional[str] = None) -> List[dict]:
    """Hızlı ürün veri üretimi"""
    generator = ProductDataGenerator()
    return generator.generate(count=count, locale=locale, category=category)


def generate_orders(count: int = 100, locale: str = "tr_TR") -> List[dict]:
    """Hızlı sipariş veri üretimi"""
    generator = OrderDataGenerator()
    return generator.generate(count=count, locale=locale)


def generate_addresses(count: int = 100, locale: str = "tr_TR", country: str = "TR") -> List[dict]:
    """Hızlı adres veri üretimi"""
    generator = AddressDataGenerator()
    return generator.generate(count=count, locale=locale, country=country)


def generate_companies(count: int = 100, locale: str = "tr_TR", industry: Optional[str] = None) -> List[dict]:
    """Hızlı şirket veri üretimi"""
    generator = CompanyDataGenerator()
    return generator.generate(count=count, locale=locale, industry=industry)
