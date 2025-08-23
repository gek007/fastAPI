from fastapi import FastAPI, Query, Body, HTTPException
import uvicorn
from hotels import router as hotels_router
app = FastAPI()
app.include_router(hotels_router, tags=["hotels"])
#@app.get("/docs", include_in_schema=False)
#async def custom_swagger_ui_html():

if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

   """  Test script
 
import asyncio 
import aiohttp

async def get_data(i: int, endpoint: str ) :
  print (f"Started running {i}")
  url = f"http://127.0.0.1:8000/{endpoint}/{i}"
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
      print (f"Finished running {i}")
   
  import asyncio

  asyncio.gather(
      *[get_data(i, "async") for i in range(30)]
    )

   """
   
   
   
