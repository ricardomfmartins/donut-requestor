from donut_requestor.model.donut import DonutBox, Flavour
from donut_requestor.model.requests import DonutRequest
from fastapi import FastAPI

app = FastAPI()


@app.get("/donuts/flavours")
async def get_donut_flavours():
    list_of_flavours = Flavour._member_names_
    return {"flavours":list_of_flavours}


@app.post("/donuts")
async def donut_request(donuts_request:DonutRequest):
    donut_box= DonutBox(amount=donuts_request.boxSize)
    for donut in donuts_request.donuts:
        donut_box.add_donut(donut=donut)

    return {"donut_box":donut_box,
            "price":donut_box.box_price()}