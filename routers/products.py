from fastapi import APIRouter
from config.database import collection
from schemas.products import productEntity, productsEntity
from models.products import Product
from fastapi.responses import JSONResponse

product = APIRouter()

@product.get('/products', tags=['All Products'])
def get_all_products() -> list[Product]:
    result = productsEntity(collection.find())
    return JSONResponse(status_code=200, content=result)

@product.get('/product/id/{id}', tags=['Product by ids'])
def get_product_id(id: int) -> list[Product]:
    query = {"id": id}
    result = productsEntity(collection.find(query))
    if result:
        return JSONResponse(status_code=200, content=result)
    
    return JSONResponse(status_code=404, content={'message': f"Not found id = {id}"})
    

@product.get('/product/pid/{pid}', tags=['Product by ids'])
def get_product_id_mongo(pid: int) -> Product:
    query = {"pid": pid}
    try:
        result = productEntity(collection.find_one(query))
        return JSONResponse(status_code=200, content=result)
    
    except:
        return JSONResponse(status_code=404, content={'message': "Not found"})

@product.get('/categories', tags=['Categories'])
def get_all_categories() -> dict:
    query = {'_id': 0, 'category_path': 1}
    result = collection.find({}, query)
    words = [y for x in result for y in x['category_path'].split(' > ')]
    words = list(set(words))
    return JSONResponse(status_code=200, content={'categories': sorted(words)})