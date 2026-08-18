class Customer:
    def __init__(self, id: int, name: str, email: str, company_name: str, is_active: bool):
        self.id = id
        self.name = name
        self.email = email
        self.company_name = company_name
        self.is_active = is_active

    def __repr__(self) -> str:
        return (
            "Customer("
            f"id={self.id}, "
            f"name={self.name!r}, "
            f"email={self.email!r}, "
            f"company_name={self.company_name!r}, "
            f"is_active={self.is_active}"
            ")"
        )