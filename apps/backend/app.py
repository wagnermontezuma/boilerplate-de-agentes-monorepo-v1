from litestar import Litestar, get

@get("/")
def hello_world() -> dict[str, str]:
    """Handler for the root endpoint."""
    return {"hello": "world"}

app = Litestar([hello_world])
