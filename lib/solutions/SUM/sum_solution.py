import typing

import pydantic
from pydantic import BaseModel


class SumSolution:
    def compute(self, x: int, y: int) -> int:
        return SumOperation(addend1=x, addend2=y).sum()


class SumOperation(BaseModel):
    addend1: typing.Annotated[int, pydantic.Field(ge=0, le=100)]
    addend2: typing.Annotated[int, pydantic.Field(ge=0, le=100)]

    def sum(self) -> int:
        return self.addend1 + self.addend2




