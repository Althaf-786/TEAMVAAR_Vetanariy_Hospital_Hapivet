# backend/routes/inventory.py
from fastapi import APIRouter
from backend.database import inventory_db

router = APIRouter(prefix="/api/inventory", tags=["Inventory"])

@router.get("/list")
async def list_inventory():
    """
    Return all items in the veterinary inventory.
    """
    if not inventory_db:
        # Sample starter data
        inventory_db.extend([
            {"id": 1, "item": "Deworming Tablet", "stock": 120, "price": 25},
            {"id": 2, "item": "Flea Shampoo", "stock": 45, "price": 80},
            {"id": 3, "item": "Vitamin Syrup", "stock": 75, "price": 50}
        ])
    return inventory_db
