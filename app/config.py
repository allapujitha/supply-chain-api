import os
import yaml
from dotenv import load_dotenv

load_dotenv()

def load_config():
    with open("config/config.yaml") as f:
        cfg = yaml.safe_load(f)

    cfg["data_path"] = os.getenv("DATA_PATH")
    return cfg