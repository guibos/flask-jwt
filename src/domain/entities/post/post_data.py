from pydantic import BaseModel


class PostData(BaseModel):
    title: str
    description: str