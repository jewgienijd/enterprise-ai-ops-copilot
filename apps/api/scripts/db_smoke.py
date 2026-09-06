
import sys
from pathlib import Path

from sqlalchemy.orm import Session

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.db.engine import engine
from app.db.models.customer import CustomerORM


with Session(engine) as session:
    customer = CustomerORM(
        name="Alice Morgan",
        email="alice@acme.example",
        company_name="Acme Cloud",
        is_active=True,
    )

    session.add(customer)
    session.commit()

    print(customer.id)
