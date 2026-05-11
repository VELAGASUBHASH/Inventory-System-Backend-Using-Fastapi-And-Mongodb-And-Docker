# this helps to send mongodb data into python dictionary (json)

def products_serializer(product):
    return {
        "id":str(product["_id"]),
        "name":product["name"],
        "category": product["category"],
        "price": product["price"],
        "quantity": product["quantity"],
        #get is used becuase if description is null then we may get error (it is define as Optional)
        "description": product.get("description"),
        "image_url": product.get("image_url")

    }