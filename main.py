from fastapi import FastAPI
from routers.products import product
from documentation import tags_metadata

app = FastAPI(
    title="Crawling Engineer FastAPI",
    description='''This API aims to consume data extracted through the 
                    Python framework Scrapy.This data is from the ADIDAS
                    and PUMA's website (https://www.adidas.es/ & 
                    https://eu.puma.com/), which contains info about each 
                    product available in these stores. For example it extracts
                    the title, description, brand, color, current price,
                    original price, sizes, images' url, availibility and 
                    categorical path. \\
                    \\
                    You can reach the scraper in the GitHub repository: 
                    https://github.com/jpradas1/Crawling_Engineer_Challenge''',
    openapi_tags = tags_metadata
)

app.include_router(product)