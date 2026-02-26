from fastapi import APIRouter
from app.config import load_config
from services.data_service import read_data
import os

router = APIRouter()

@router.get("/orders")
def get_orders():
    cfg = load_config()
    file_path = os.path.join(cfg["data_path"], cfg["files"]["orders"])
    return read_data(file_path)