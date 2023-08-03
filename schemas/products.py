
def productEntity(item) -> dict:
    return {
        "id": int(item["id"]),
        "title": item["title"],
        "brand": item["brand"],
        "description": item["description"],
        "pid": int(item["pid"]),
        "color": item["colors"],
        "current_price": float(item["current_price"]),
        "original_price": float(item["original_price"]),
        "currency": item["currency"],
        "inventory": item["inventory"],
        "sizes": item["sizes"],
        "category_path": item["category path"],
        "URL_images": item["URL_images"],
        "URL_product": item["URL_product"]
    }

def productsEntity(entity) -> dict:
    return [productEntity(item) for item in entity]

# def categoryEntity(item) -> dict:
#     return {
#         "_id": str(item["_id"]),
#         "categories": item["distinctWords"]
#     }