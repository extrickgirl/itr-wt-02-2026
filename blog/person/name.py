from dataclasses import dataclass


@dataclass(frozen=True)
class Name:
    first_name: str
    last_name: str

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
