from typing import List

from pydantic import BaseModel, ConfigDict

from domain.enums.permission import Permission


class AccountShare(BaseModel):
    account_id: int
    username: str
    permissions: List[Permission]

    model_config = ConfigDict(extra='forbid')
