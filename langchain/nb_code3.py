import os
from langchain.chat_models import init_chat_model
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
model = init_chat_model("groq:llama-3.3-70b-versatile")
model
from pydantic import BaseModel, Field

class Movie(BaseModel):
    title:str=Field(description="Title of the movie")
    year:int=Field(description="This year movie was released")
    rating:float=Field(description="Rating of this movie")
    deirector:str=Field(description="The direstor of this movie")

model_structured_output = model.with_structured_output(Movie)
model_structured_output
model.invoke("Provide me the details about movie inception")
response = model_structured_output.invoke("Provide me details about the movie inception")
response
from pydantic import BaseModel, Field

class Movie(BaseModel):
    title:str=Field(description="Title of the movie")
    year:int=Field(description="This year movie was released")
    rating:float=Field(description="Rating of this movie")
    deirector:str=Field(description="The direstor of this movie")

model_structured_output = model.with_structured_output(Movie, include_raw=True)
response = model_structured_output.invoke("Provide me details about the movie inception")
response
from pydantic import BaseModel, Field

class Actor(BaseModel):
    name:str
    role:str

class MovieDetails(BaseModel):
    title: str
    year: int
    cast: list[Actor]
    genres: list[str]
    budget: float | None = Field(None, description="Budget in Milloins USD")

model_structured_output = model.with_structured_output(MovieDetails)

response = model_structured_output.invoke("Provide me details about movie Inception.")
response
from typing_extensions import TypedDict, Annotated
class MovieDict(TypedDict):
    """A Movie with Details"""
    title: Annotated[str, ..., "The title of the Movie"]
    year: Annotated[int, ..., "The year movie was released"]
    director: Annotated[str, ..., "The director of the Movie"]
    rating: Annotated[float, ..., "The rating of the movie out of 10"]


model_type_dict = model.with_structured_output(MovieDict)
response = model_type_dict.invoke("Provide details about movie Avengers.")
response
from pydantic import BaseModel, Field

class Actor(TypedDict):
    name:str
    role:str

class MovieDetails(TypedDict):
    title: str
    year: int
    cast: list[Actor]
    genres: list[str]
    budget: float | None 

model_structured_output = model.with_structured_output(MovieDetails)

response = model_structured_output.invoke("Provide me details about movie Inception.")
response

