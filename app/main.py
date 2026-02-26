import sys
import os
from fastapi import FastAPI
from routes import products, orders, suppliers


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

app = FastAPI(title="Supply Chain API")

app.include_router(products.router)
app.include_router(orders.router)
app.include_router(suppliers.router)