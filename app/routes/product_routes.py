
from bson import ObjectId
from bson.errors import InvalidId
from fastapi import APIRouter, HTTPException,File,UploadFile
from app.db import products_collection
from app.schemas.product_schema import Product
from app.utils.helpers import products_serializer
import cloudinary.uploader

router = APIRouter()


@router.post("/add")
async def add_products(product: Product):

    product_dict = product.dict()

    result = await products_collection.insert_one(
        product_dict
    )

    created_product = await products_collection.find_one(
        {"_id": result.inserted_id}
    )

    return {
        "message": "Product Added",
        "data": products_serializer(created_product)
    }


@router.get("/all")
async def get_all_products():

    products = []

    async for product in products_collection.find():

        products.append(
            products_serializer(product)
        )

    return products


@router.get("/search")
async def search_product(search: str):

    products = []

    query = {
        "name": {
            "$regex": search,
            "$options": "i"
        }
    }

    async for product in products_collection.find(query):

        products.append(
            products_serializer(product)
        )

    return products


@router.get("/low-stock")
async def low_stock_alert():

    products = []

    async for product in products_collection.find(
        {
            "quantity": {
                "$lt": 5
            }
        }
    ):

        products.append(
            products_serializer(product)
        )

    return products


@router.get("/category/{category}")
async def get_by_category(category: str):

    products = []

    async for product in products_collection.find(
        {
            "category": category
        }
    ):

        products.append(
            products_serializer(product)
        )

    return products


# GET PRODUCT BY ID
@router.get("/{prod_id}")
async def get_product_by_id(prod_id: str):

    try:
        object_id = ObjectId(prod_id)

    except InvalidId:

        raise HTTPException(
            status_code=400,
            detail="Invalid Product ID"
        )

    product = await products_collection.find_one(
        {"_id": object_id}
    )

    if not product:

        raise HTTPException(
            status_code=404,
            detail="Product Not Found"
        )

    return products_serializer(product)


@router.put("/{prod_id}")
async def update_product(
    prod_id: str,
    product: Product
):

    try:
        object_id = ObjectId(prod_id)

    except InvalidId:

        raise HTTPException(
            status_code=400,
            detail="Invalid Product ID"
        )

    result = await products_collection.update_one(
        {"_id": object_id},
        {
            "$set": product.dict()
        }
    )

    if result.matched_count == 0:

        raise HTTPException(
            status_code=404,
            detail="Product Not Found"
        )

    updated_product = await products_collection.find_one(
        {"_id": object_id}
    )

    return {
        "message": "Product Updated",
        "data": products_serializer(updated_product)
    }

@router.delete("/{prod_id}")
async def delete_product(prod_id: str):

    try:
        object_id = ObjectId(prod_id)

    except InvalidId:

        raise HTTPException(
            status_code=400,
            detail="Invalid Product ID"
        )

    result = await products_collection.delete_one(
        {"_id": object_id}
    )

    if result.deleted_count == 0:

        raise HTTPException(
            status_code=404,
            detail="Product Not Found"
        )

    return {
        "message": "Product Deleted"
    }

@router.post("/upload-image")
async def upload_image(file: UploadFile = File(...)):

    result = cloudinary.uploader.upload(
        file.file
    )

    return {
        "image_url": result["secure_url"]
    }