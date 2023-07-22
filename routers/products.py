from fastapi import APIRouter
from config.database import connection
from schemas.products import productEntity, productsEntity, categoryEntity
from models.products import Product, Category
from bson import ObjectId
from fastapi.responses import JSONResponse
from .queries import categories, brand_category

product = APIRouter()

@product.get('/products', tags=['All Products'])
def get_all_products() -> list[Product]:

    result = productsEntity(connection.products.items.find())
    return JSONResponse(status_code=200, content=result)

@product.get('/product/{id}', tags=['Product by ids'])
def get_product_id(id: int) -> Product:

    query = {"id": id}
    try:
        result = productEntity(connection.products.items.find_one(query))
        return JSONResponse(status_code=200, content=result)
    
    except:
        return JSONResponse(status_code=404, content={'message': "Not found"})
    

@product.get('/product/mongo/{id}', tags=['Product by ids'])
def get_product_id_mongo(id: str):

    query = {"_id": ObjectId(id)}
    try:
        result = productEntity(connection.products.items.find_one(query))
        return JSONResponse(status_code=200, content=result)
    
    except:
        return JSONResponse(status_code=404, content={'message': "Not found"})

@product.get('/categories', tags=['Categories'])
def get_product_categories() -> Category:

    result = connection.products.items.aggregate(categories)
    result = categoryEntity([x for x in result][0])
    result['categories'] = sorted(result['categories'])
    print(result)
    return JSONResponse(status_code=200, content=result)

@product.get('/brand', tags=['Product by quality'])
def get_product_brand(brand: str, category: str) -> list[Product]:
    result = connection.products.items.aggregate(brand_category(brand, category))
    result = productsEntity([x for x in result])
    if result:
        return JSONResponse(status_code=200, content=result)
   
    return JSONResponse(status_code=404, content={
            'message': '''Not found. There're two brand PUMA and ADIDAS.
            The available categories are in /categories'''
            })