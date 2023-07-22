categories = [
    {
        '$project': {
            'slicedWords': {
                '$slice': ["$category path", 0, { '$subtract': [{ '$size': "$category path" }, 1] }]
            }
        }
    },
    { '$unwind': "$slicedWords" },
    {
        '$group': {
            '_id': 0, 'distinctWords': { '$addToSet': "$slicedWords" } 
        }
    }
]

def brand_category(brand: str, category: str):
    return [
        {
            '$match': {
                "category path": { '$in': [category] },
                "brand": brand
            }
        }
    ]