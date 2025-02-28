import json
import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from models import Student, Topic, StudySession, Card
origins = [
    "http://localhost:3000",
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
client = AsyncIOMotorClient(os.getenv("MONGO_URL", "mongodb://localhost:27017"))
db = client.flashcard_db

@app.get("/cards")
async def get_cards():
    cards_cursor = db.cards.find()
    cards = []
    async for doc in cards_cursor:
        # Convert the ObjectId to string
        doc["_id"] = str(doc["_id"])
        cards.append(doc)
    return cards


@app.get("/cards/{topic_id}")
async def get_card(topic_id: str):
    card = await db.cards.find_one({"topic_id": topic_id})
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    return card

# Additional CRUD endpoints for Student, StudySession, and Card would be added here.

