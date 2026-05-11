from typing import Optional

from pydantic import BaseModel, Field

class Product(BaseModel):

        name:str = Field(...,min_length=2)
        category : str
        price : float = Field(...,gt=0)
        quantity : int =Field(...,ge=0)
        description : Optional[str] = None
        image_url: Optional[str]=None



