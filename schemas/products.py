
def productEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "id": int(item["id"]),
        "title": item["title"],
        "description": item["description"],
        "brand": item["brand"],
        "inventory": item["inventory"],
        "colors": item["colors"],
        "current_price": item["current_price"],
        "original_price": item["original_price"],
        "sizes": item["sizes"],
        "url_pictures": item["url_pictures"],
        "category path": item["category path"]
    }

def productsEntity(entity) -> dict:
    return [productEntity(item) for item in entity]

def categoryEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "categories": item["distinctWords"]
    }