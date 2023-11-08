import dataclasses
from typing import Optional


@dataclasses.dataclass
class Authentication:
    username: Optional[str] = None
    password: Optional[str] = None
    token: Optional[str] = None
