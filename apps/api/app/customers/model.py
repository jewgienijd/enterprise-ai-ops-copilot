from dataclasses import dataclass

@dataclass
class Customer:
    id: int
    name: str
    email: str
    company_name: str
    is_active: bool

    @property
    def display_name(self) -> str:
        return f"{self.company_name} — {self.name}"
