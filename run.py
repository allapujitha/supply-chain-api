import uvicorn
import os

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=os.getenv("HOST"),
        port=int(os.getenv("PORT"))
    )