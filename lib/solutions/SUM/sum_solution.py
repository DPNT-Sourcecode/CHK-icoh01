import typing

import pydantic
from pydantic import BaseModel

type Addend = typing.Annotated[int, pydantic.Field(strict=True, ge=0, le=100)]


class SumSolution:
    def compute(self, x: int, y: int) -> int:
        return SumOperation(addend1=x, addend2=y).sum()


class SumOperation(BaseModel):
    addend1: Addend
    addend2: Addend

    def sum(self) -> int:
        return self.addend1 + self.addend2
