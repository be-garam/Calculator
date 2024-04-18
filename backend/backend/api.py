from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}

@api.get("/sub")
def sub(request, a:int, b:int):
    return {"result": a - b}

@api.get("/mul")
def mul(request, a:int, b:int):
    return {"result": a * b}

@api.get("/div")
def div(request, a:int, b:int):
    return {"result": a / b}