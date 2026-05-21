"""
Test Data Generation API
FastAPI uygulaması - Geliştiriciler için rastgele test verileri sağlar
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
import json
import csv
import io
from typing import List, Optional
from datetime import datetime
import logging

# Local imports
# YENİ (✅ DOĞRU)
from generators import (
    UserDataGenerator,
    ProductDataGenerator,
    OrderDataGenerator,
    AddressDataGenerator,
    CompanyDataGenerator
)
from schemas import (
    GenerateRequest,
    UserResponse,
    ProductResponse,
    OrderResponse,
)

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI app initialization
app = FastAPI(
    title="Test Data Generation API",
    description="Geliştiriciler için rastgele test verileri üreten API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Generator instances
user_generator = UserDataGenerator()
product_generator = ProductDataGenerator()
order_generator = OrderDataGenerator()
address_generator = AddressDataGenerator()
company_generator = CompanyDataGenerator()


# ============== HEALTH CHECK ==============
@app.get("/health", tags=["Health"])
async def health_check():
    """API sağlığını kontrol et"""
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    }


# ============== USERS ENDPOINTS ==============
@app.get("/api/v1/users", tags=["Users"], response_model=List[UserResponse])
async def generate_users(
    count: int = Query(10, ge=1, le=1000, description="Kaç adet kullanıcı üretilsin (1-1000)"),
    locale: str = Query("tr_TR", description="Dil/Bölge (tr_TR, en_US, de_DE, vb.)"),
    format: str = Query("json", regex="^(json|csv|xml)$", description="Çıktı formatı")
):
    """
    Rastgele kullanıcı verileri üret
    
    - **count**: Üretilecek kullanıcı sayısı
    - **locale**: Veri dilini belirle
    - **format**: Çıktı formatı (json, csv, xml)
    """
    try:
        users = user_generator.generate(count=count, locale=locale)
        
        if format == "json":
            return JSONResponse(content=users)
        elif format == "csv":
            return _to_csv_response(users, "users.csv")
        elif format == "xml":
            return _to_xml_response(users, "users.xml")
            
    except Exception as e:
        logger.error(f"Error generating users: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/api/v1/users/batch", tags=["Users"])
async def generate_users_batch(request: GenerateRequest):
    """
    Batch operasyonunda birden fazla konfigürasyon ile kullanıcı üret
    """
    try:
        results = []
        for config in request.configurations:
            users = user_generator.generate(
                count=config.count,
                locale=config.locale
            )
            results.append({
                "config": config.dict(),
                "data": users,
                "count": len(users)
            })
        return results
    except Exception as e:
        logger.error(f"Error in batch generation: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


# ============== PRODUCTS ENDPOINTS ==============
@app.get("/api/v1/products", tags=["Products"], response_model=List[ProductResponse])
async def generate_products(
    count: int = Query(10, ge=1, le=1000),
    category: Optional[str] = Query(None, description="Ürün kategorisi"),
    locale: str = Query("tr_TR"),
    format: str = Query("json", regex="^(json|csv|xml)$")
):
    """Rastgele ürün verileri üret"""
    try:
        products = product_generator.generate(
            count=count,
            category=category,
            locale=locale
        )
        
        if format == "json":
            return JSONResponse(content=products)
        elif format == "csv":
            return _to_csv_response(products, "products.csv")
        elif format == "xml":
            return _to_xml_response(products, "products.xml")
            
    except Exception as e:
        logger.error(f"Error generating products: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


# ============== ORDERS ENDPOINTS ==============
@app.get("/api/v1/orders", tags=["Orders"], response_model=List[OrderResponse])
async def generate_orders(
    count: int = Query(10, ge=1, le=1000),
    locale: str = Query("tr_TR"),
    format: str = Query("json", regex="^(json|csv|xml)$")
):
    """Rastgele sipariş verileri üret"""
    try:
        orders = order_generator.generate(count=count, locale=locale)
        
        if format == "json":
            return JSONResponse(content=orders)
        elif format == "csv":
            return _to_csv_response(orders, "orders.csv")
        elif format == "xml":
            return _to_xml_response(orders, "orders.xml")
            
    except Exception as e:
        logger.error(f"Error generating orders: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


# ============== ADDRESSES ENDPOINTS ==============
@app.get("/api/v1/addresses", tags=["Addresses"])
async def generate_addresses(
    count: int = Query(10, ge=1, le=1000),
    country: Optional[str] = Query("TR", description="Ülke kodu (TR, US, DE, vb.)"),
    locale: str = Query("tr_TR"),
    format: str = Query("json", regex="^(json|csv|xml)$")
):
    """Rastgele adres verileri üret"""
    try:
        addresses = address_generator.generate(
            count=count,
            country=country,
            locale=locale
        )
        
        if format == "json":
            return JSONResponse(content=addresses)
        elif format == "csv":
            return _to_csv_response(addresses, "addresses.csv")
        elif format == "xml":
            return _to_xml_response(addresses, "addresses.xml")
            
    except Exception as e:
        logger.error(f"Error generating addresses: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


# ============== COMPANIES ENDPOINTS ==============
@app.get("/api/v1/companies", tags=["Companies"])
async def generate_companies(
    count: int = Query(10, ge=1, le=1000),
    industry: Optional[str] = Query(None),
    locale: str = Query("tr_TR"),
    format: str = Query("json", regex="^(json|csv|xml)$")
):
    """Rastgele şirket verileri üret"""
    try:
        companies = company_generator.generate(
            count=count,
            industry=industry,
            locale=locale
        )
        
        if format == "json":
            return JSONResponse(content=companies)
        elif format == "csv":
            return _to_csv_response(companies, "companies.csv")
        elif format == "xml":
            return _to_xml_response(companies, "companies.xml")
            
    except Exception as e:
        logger.error(f"Error generating companies: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


# ============== COMBINED DATA ENDPOINTS ==============
@app.get("/api/v1/complete-dataset", tags=["Combined"])
async def generate_complete_dataset(
    user_count: int = Query(5, ge=1, le=100),
    product_count: int = Query(5, ge=1, le=100),
    order_count: int = Query(5, ge=1, le=100),
    locale: str = Query("tr_TR"),
    format: str = Query("json", regex="^(json|csv|xml)$")
):
    """Eksiksiz test veri seti üret (kullanıcı + ürün + sipariş)"""
    try:
        dataset = {
            "users": user_generator.generate(count=user_count, locale=locale),
            "products": product_generator.generate(count=product_count, locale=locale),
            "orders": order_generator.generate(count=order_count, locale=locale),
            "metadata": {
                "generated_at": datetime.utcnow().isoformat(),
                "locale": locale,
                "total_records": user_count + product_count + order_count
            }
        }
        
        if format == "json":
            return JSONResponse(content=dataset)
        elif format == "csv":
            return _to_csv_response(dataset, "complete_dataset.csv")
        elif format == "xml":
            return _to_xml_response(dataset, "complete_dataset.xml")
            
    except Exception as e:
        logger.error(f"Error generating complete dataset: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


# ============== HELPER FUNCTIONS ==============
def _to_csv_response(data: List[dict] | dict, filename: str):
    """Veriyi CSV formatına dönüştür"""
    if isinstance(data, dict) and "users" in data:
        # Combined dataset durumu
        output = io.StringIO()
        for key, items in data.items():
            if key != "metadata" and isinstance(items, list):
                output.write(f"\n\n--- {key.upper()} ---\n")
                if items:
                    writer = csv.DictWriter(output, fieldnames=items[0].keys())
                    writer.writeheader()
                    writer.writerows(items)
        content = output.getvalue()
    else:
        # Single dataset durumu
        output = io.StringIO()
        if data:
            writer = csv.DictWriter(output, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        content = output.getvalue()
    
    return FileResponse(
        io.BytesIO(content.encode()),
        media_type="text/csv",
        filename=filename
    )


def _to_xml_response(data: List[dict] | dict, filename: str):
    """Veriyi XML formatına dönüştür"""
    import xml.etree.ElementTree as ET
    
    root = ET.Element("data")
    
    if isinstance(data, dict) and "users" in data:
        for key, items in data.items():
            if key != "metadata" and isinstance(items, list):
                parent = ET.SubElement(root, key)
                for item in items:
                    item_elem = ET.SubElement(parent, "item")
                    for k, v in item.items():
                        sub = ET.SubElement(item_elem, k)
                        sub.text = str(v)
    else:
        parent = ET.SubElement(root, "items")
        for item in data:
            item_elem = ET.SubElement(parent, "item")
            for k, v in item.items():
                sub = ET.SubElement(item_elem, k)
                sub.text = str(v)
    
    xml_str = ET.tostring(root, encoding="utf-8")
    
    return FileResponse(
        io.BytesIO(xml_str),
        media_type="application/xml",
        filename=filename
    )


# ============== ERROR HANDLERS ==============
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """HTTP exception handler"""
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.detail,
            "status_code": exc.status_code,
            "timestamp": datetime.utcnow().isoformat()
        }
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=True
    )
