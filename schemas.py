"""
Pydantic Schemas - API için veri validasyonu modelleri
"""

from pydantic import BaseModel, EmailStr, HttpUrl, Field
from typing import List, Optional, Dict, Any
from datetime import datetime


# ============== REQUEST SCHEMAS ==============

class GenerationConfig(BaseModel):
    """Bir veri türü için üretim konfigürasyonu"""
    count: int = Field(ge=1, le=1000, description="Kaç adet veri üretilsin")
    locale: str = Field(default="tr_TR", description="Veri dili")
    
    class Config:
        json_schema_extra = {
            "example": {
                "count": 100,
                "locale": "tr_TR"
            }
        }


class GenerateRequest(BaseModel):
    """Batch veri üretim isteği"""
    configurations: List[GenerationConfig] = Field(
        description="Üretilecek veri konfigürasyonları"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "configurations": [
                    {"count": 50, "locale": "tr_TR"},
                    {"count": 30, "locale": "en_US"}
                ]
            }
        }


# ============== USER SCHEMAS ==============

class UserResponse(BaseModel):
    """Kullanıcı verisi response modeli"""
    id: str
    username: str
    email: EmailStr | str
    first_name: str
    last_name: str
    phone: str
    date_of_birth: str
    gender: str
    address: str
    city: str
    country: str
    postal_code: str
    company: str
    job_title: str
    website: str
    created_at: str
    is_active: bool
    last_login: str
    profile_picture: str | None
    bio: str | None
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "username": "john_doe",
                "email": "john@example.com",
                "first_name": "John",
                "last_name": "Doe",
                "phone": "+1-123-456-7890",
                "date_of_birth": "1990-01-01",
                "gender": "M",
                "address": "123 Main St, New York, NY",
                "city": "New York",
                "country": "United States",
                "postal_code": "10001",
                "company": "Tech Corp",
                "job_title": "Software Engineer",
                "website": "https://example.com",
                "created_at": "2024-01-15T10:30:00",
                "is_active": True,
                "last_login": "2024-05-20T15:45:00",
                "profile_picture": "https://example.com/pic.jpg",
                "bio": "Software developer and tech enthusiast"
            }
        }


# ============== PRODUCT SCHEMAS ==============

class DimensionsModel(BaseModel):
    """Ürün boyutları"""
    length: float
    width: float
    height: float


class ProductResponse(BaseModel):
    """Ürün verisi response modeli"""
    id: str
    sku: str
    name: str
    description: str
    category: str
    price: float
    currency: str
    discount_percentage: int
    stock_quantity: int
    weight: float
    dimensions: DimensionsModel
    color: str
    material: str
    manufacturer: str
    rating: float
    reviews_count: int
    is_available: bool
    created_at: str
    tags: List[str]
    image_url: str | None
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "sku": "5901234123457",
                "name": "Premium Wireless Headphones",
                "description": "High-quality wireless headphones with noise cancellation",
                "category": "Electronics",
                "price": 199.99,
                "currency": "USD",
                "discount_percentage": 15,
                "stock_quantity": 250,
                "weight": 0.25,
                "dimensions": {
                    "length": 20.0,
                    "width": 18.0,
                    "height": 8.0
                },
                "color": "Black",
                "material": "Plastic",
                "manufacturer": "Tech Brand",
                "rating": 4.5,
                "reviews_count": 350,
                "is_available": True,
                "created_at": "2024-01-15T10:30:00",
                "tags": ["wireless", "headphones", "audio"],
                "image_url": "https://example.com/product.jpg"
            }
        }


# ============== ORDER SCHEMAS ==============

class OrderResponse(BaseModel):
    """Sipariş verisi response modeli"""
    id: str
    order_number: str
    customer_id: str
    customer_name: str
    customer_email: str
    shipping_address: str
    billing_address: str
    order_date: str
    expected_delivery: str
    actual_delivery: str | None
    items_count: int
    subtotal: float
    tax: float
    shipping_cost: float
    total_amount: float
    currency: str
    payment_method: str
    payment_status: str
    order_status: str
    notes: str | None
    tracking_number: str | None
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "order_number": "ORD-654321",
                "customer_id": "550e8400-e29b-41d4-a716-446655440001",
                "customer_name": "Jane Smith",
                "customer_email": "jane@example.com",
                "shipping_address": "456 Oak Ave, Los Angeles, CA 90001",
                "billing_address": "456 Oak Ave, Los Angeles, CA 90001",
                "order_date": "2024-05-01T10:30:00",
                "expected_delivery": "2024-05-08T00:00:00",
                "actual_delivery": "2024-05-07T14:20:00",
                "items_count": 3,
                "subtotal": 299.97,
                "tax": 29.99,
                "shipping_cost": 10.00,
                "total_amount": 339.96,
                "currency": "USD",
                "payment_method": "Credit Card",
                "payment_status": "Completed",
                "order_status": "Delivered",
                "notes": "Delivered to front porch",
                "tracking_number": "ABCD-1234-EFGH"
            }
        }


# ============== ADDRESS SCHEMAS ==============

class AddressResponse(BaseModel):
    """Adres verisi response modeli"""
    id: str
    street_address: str
    city: str
    state_province: str
    postal_code: str
    country: str
    country_full_name: str
    latitude: float
    longitude: float
    phone: str
    is_default: bool
    address_type: str
    created_at: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "street_address": "789 Pine St",
                "city": "Chicago",
                "state_province": "Illinois",
                "postal_code": "60601",
                "country": "US",
                "country_full_name": "United States",
                "latitude": 41.881832,
                "longitude": -87.629101,
                "phone": "+1-312-555-0123",
                "is_default": True,
                "address_type": "Residential",
                "created_at": "2024-01-15T10:30:00"
            }
        }


# ============== COMPANY SCHEMAS ==============

class SocialMediaModel(BaseModel):
    """Şirket sosyal medya linkleri"""
    linkedin: str | None = None
    twitter: str | None = None
    facebook: str | None = None


class CompanyResponse(BaseModel):
    """Şirket verisi response modeli"""
    id: str
    name: str
    industry: str
    website: str
    email: str
    phone: str
    founded_year: int
    employee_count: str
    revenue: float
    currency: str
    headquarters: str
    city: str
    country: str
    ceo_name: str
    description: str
    logo_url: str | None
    social_media: SocialMediaModel
    certifications: List[str]
    is_verified: bool
    created_at: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "550e8400-e29b-41d4-a716-446655440000",
                "name": "Innovation Technologies Inc",
                "industry": "Technology",
                "website": "https://innovationtech.com",
                "email": "info@innovationtech.com",
                "phone": "+1-415-555-0123",
                "founded_year": 2010,
                "employee_count": "201-500",
                "revenue": 5000000.00,
                "currency": "USD",
                "headquarters": "123 Tech Boulevard, San Francisco, CA",
                "city": "San Francisco",
                "country": "United States",
                "ceo_name": "John Innovation",
                "description": "A leading technology company specializing in AI and cloud solutions",
                "logo_url": "https://example.com/logo.png",
                "social_media": {
                    "linkedin": "https://linkedin.com/company/innovation-tech",
                    "twitter": "https://twitter.com/innovationtech",
                    "facebook": "https://facebook.com/innovationtech"
                },
                "certifications": ["ISO 9001", "SOC 2"],
                "is_verified": True,
                "created_at": "2024-01-15T10:30:00"
            }
        }


# ============== ERROR SCHEMAS ==============

class ErrorResponse(BaseModel):
    """API hata response modeli"""
    error: str
    status_code: int
    timestamp: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "error": "Invalid count parameter",
                "status_code": 400,
                "timestamp": "2024-05-21T10:30:00"
            }
        }


# ============== METADATA SCHEMAS ==============

class MetadataResponse(BaseModel):
    """Veri seti metadatası"""
    generated_at: str
    locale: str
    total_records: int


class CompleteDatasetResponse(BaseModel):
    """Eksiksiz veri seti response modeli"""
    users: List[UserResponse]
    products: List[ProductResponse]
    orders: List[OrderResponse]
    metadata: MetadataResponse
