from pydantic import BaseModel


class PostId(BaseModel):
    post_id: int
