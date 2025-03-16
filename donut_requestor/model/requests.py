from donut_requestor.model.donut import Donut
from pydantic import BaseModel


class DonutRequest(BaseModel):
    boxSize: int
    donuts: list[Donut]

