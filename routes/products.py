from fastapi import APIRouter
from app.config import load_config
from services.data_service import read_data
import os

router = APIRouter()

@router.get("/products")
def get_products():
    cfg = load_config()
    file_path = os.path.join(cfg["data_path"], cfg["files"]["products"])
    return read_data(file_path)