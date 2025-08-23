from fastapi import FastAPI, Query, HTTPException, APIRouter
from schemas.hotels import Hotel, HotelPATCH
router = APIRouter(prefix="/hotels", tags=["Hotels"])

hotels = [
    {"id": 1, "title": "Sochi", "name": "Sochi"},
    {"id": 2, "title": "Moscow", "name": "Moscow"},
    {"id": 3, "title": "Panama","name": "Panama" },
    {"id": 4, "title": "Piter", "name": "Piter"},
    {"id": 4, "title": "Tel-aviv", "name": "Tel-aviv"},
    {"id": 4, "title": "Bat-yam", "name": "Bat-yam"},
]

@router.get("")
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

@router.delete("/{hotel_id}")
def delete_hotel(hotel_id: int):
   global hotels
   hotels = [hotel for hotel in hotels if hotel["id"] != hotel_id ]
   return {"staus":"OK"}


#reuest body
@router.post("")
def create_hotel(hotel_data: Hotel):
    global hotels
    hotels.append({
        "id": hotels[-1]["id"] + 1,
        "title": hotel_data.title,
        "name": hotel_data.name,
    })
    return {"status": "OK"}


@router.put("/{hotel_id}",
         summary="Update info about Hotel !!!!",
         description="**** Update info about Hotel ****"
)
def edit_hotel(hotel_id: int, hotel_data: Hotel):
    global hotels

    for h in hotels:
        if h["id"] == hotel_id:
                h["name"] = hotel_data.name
                h["title"] = hotel_data.title
                return {"message": "Hotel updated", "hotel": h}

    raise HTTPException(status_code=404, detail="Hotel not found")

@router.patch("/{hotel_id}")
def partially_edit_hotel(
        hotel_id: int,
        hotel_data: HotelPATCH,
):
    global hotels
    flag = True
    #hotel = [hotel for hotel in hotels if hotel["id"] != hotel_id][0]

    for h in hotels:
        if h["id"] == hotel_id:
            if hotel_data.title is not None:
                h["title"] = hotel_data.title
                flag = True
            if hotel_data.name is not None:
                h["name"] = hotel_data.name
                flag = True

    if flag:
       return {"message": "Hotel updated", "hotel": h}

    raise HTTPException(status_code=404, detail="Hotel not found")
