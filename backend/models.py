from pydantic import BaseModel
from typing import List

class Student(BaseModel):
    id: str
    name: str

class Topic(BaseModel):
    id: str
    title: str
    description: str

class StudySession(BaseModel):
    id: str
    topics: List[Topic]
    score: int = 0
    duration: int  # in seconds

class Card(BaseModel):
    id: str
    concept: str
    definition: str
    answer: str
    main_words: List[str]
    topic: Topic

