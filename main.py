from fastapi import FastAPI, Query
import uvicorn

hotels = [
    {"id": 1, "title": "Sochi"},
    {"id": 2, "title": "Moscow"},
    {"id": 3, "title": "Panama"},
    {"id": 4, "title": "Piter"},
    {"id": 4, "title": "Tel-aviv"},
    {"id": 4, "title": "Bat-yam"},
]
app = FastAPI()
@app.get("/hotels")
def func(
            id: int | None =  Query(None, Description = "Id of Hotel"),
            title: str | None = Query(None, Description = "Hotel Name"),
        ):

    hotels_ = []
    for hotel in hotels:
        if id and hotel["id"] != id:
            continue
        if title and hotel["title"] != title:
            continue
        hotels_.append(hotel)

    return hotels_

@app.delete("/hotels/{hotel_id}")
def delete_hotel(hotel_id: int):
   global hotels
   hotels = [hotel for hotel in hotels if hotel["id"] != hotel_id ]
   return {"staus":"OK"}




#@app.get("/docs", include_in_schema=False)

if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", reload=True, port=8000)