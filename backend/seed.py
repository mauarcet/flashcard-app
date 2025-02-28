# seed.py
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def seed():
    client = AsyncIOMotorClient("mongodb://mongo:27017")  # Use "mongodb://localhost:27017" if running locally
    db = client.flashcard_db

    # Optional: Clear existing collections
    await db.students.delete_many({})
    await db.topics.delete_many({})
    await db.cards.delete_many({})

    # Insert one student
    student = {
        "id": "student1",
        "name": "John Doe"
    }
    await db.students.insert_one(student)

    # Insert 3 topics related to Python programming
    topics = [
        {"id": "topic1", "title": "Python Basics", "description": "Fundamentals of Python programming."},
        {"id": "topic2", "title": "Advanced Python", "description": "Deep dive into advanced Python features."},
        {"id": "topic3", "title": "Python Libraries", "description": "Overview of popular Python libraries."}
    ]
    await db.topics.insert_many(topics)

    # For each topic, insert 10 cards
    for topic in topics:
        topic_id = topic["id"]
        cards = []
        for i in range(1, 11):
            card = {
                "id": f"{topic_id}-card{i}",
                "topic_id": topic_id,
                "concept": f"{topic['title']} Concept {i}",
                "definition": f"This is the definition for {topic['title']} Concept {i}.",
                "answer": f"Expected answer for {topic['title']} Concept {i}.",
                "main_words": [f"word{i}", "python"]
            }
            cards.append(card)
        await db.cards.insert_many(cards)

    print("Database seeding completed.")

if __name__ == "__main__":
    asyncio.run(seed())
