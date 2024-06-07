from typing import Protocol, runtime_checkable

@runtime_checkable
class Combinable(Protocol):
  

  def can_combine(self, other: "Combinable") -> bool:
    ...


  def combine(self, other: "Combinable") -> "Combinable":
    ...


#Mark both methods as abstract. A precondition of calling combine successfully is that can_combine() would return True for the two items.