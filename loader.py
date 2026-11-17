import os


def load_settings():
    debug = os.environ.get("DEBUG", "false").lower() == "true"
    return {"debug": debug}


if __name__ == "__main__":
    print("Settings:", load_settings())
