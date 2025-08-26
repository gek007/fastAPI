from fastapi import Query, HTTPException, APIRouter, Body

from repositories.hotels import HotelsRepository
from src.api.dependencies import PaginationDep
from src.database import async_session_maker, engine
from src.models.hotels import HotelsOrm
from src.schemas.hotels import Hotel, HotelPATCH
from sqlalchemy import insert, select, func

router = APIRouter(prefix="/hotels", tags=["Hotels"])

@router.get("")
async def get_hotels(
        pagination: PaginationDep,
        location: str | None = Query(None, description="location"),
        title: str | None = Query(None, description="Название отеля"),
):
    per_page = pagination.per_page or 5
    async with async_session_maker() as session:
            return await HotelsRepository(session).get_all(
            location=location,
            title=title,
            limit=per_page,
            offset=per_page * (pagination.page - 1)
        )

@router.delete("/{hotel_id}")
def delete_hotel(hotel_id: int):
   global hotels
   hotels = [hotel for hotel in hotels if hotel["id"] != hotel_id ]
   return {"staus":"OK"}


#reuest body
@router.post("")
async def create_hotel(hotel_data: Hotel = Body(openapi_examples={
    "1": {
        "summary": "Сочи",
        "value": {
            "title": "Отель Сочи 5 звезд у моря",
            "name": "sochi_u_morya",
            "location": "ул. Моря, 1",
        }
    },
    "2": {
        "summary": "Дубай",
        "value": {
            "title": "Отель Дубай У фонтана",
            "name": "dubai_fountain",
            "location": "ул. Шейха, 2",
        }
    }
})
):

    async with async_session_maker() as session:
            await HotelsRepository(session).add(**hotel_data.model_dump())
            await session.commit()

    # async with async_session_maker() as session:
    #     add_hotel_stmt = insert(HotelsOrm).values(**hotel_data.model_dump())
    #     print(add_hotel_stmt.compile(engine, compile_kwargs={"literal_binds": True}))
    #     await session.execute(add_hotel_stmt)
    #     await session.commit()

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
