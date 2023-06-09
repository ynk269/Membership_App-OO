from typing import Dict
from dataclasses import dataclass

@dataclass
class Membership:
    typeOfMembership: str
    discount: float
    fees: float

class MembershipFactory:
    def __init__(self):
        self.pool: Dict[str, Membership] = {
            "GOLD": Membership("GOLD", 10.0, 25000),
            "SILVER": Membership("SILVER", 5.0, 20000),
            "PLATINUM": Membership("PLATINUM", 15.0, 30000)
        }

    def createMembership(self, typeOfMembership: str, fees: float, discount: float) -> Membership:
        mem = Membership(typeOfMembership, discount, fees)
        return mem

    def create(self, typeOfMembership: str) -> Membership:
        return self.pool.get(typeOfMembership)

    @staticmethod
    def getInstance() -> 'MembershipFactory':
        if not hasattr(MembershipFactory, "_instance"):
            MembershipFactory._instance = MembershipFactory()
        return MembershipFactory._instance