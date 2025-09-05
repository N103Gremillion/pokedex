from enum import Enum
from typing import Any
from dotenv import load_dotenv, dotenv_values
import os
from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from app_types import DetailedPokemonTypeKeys, PokedexKeys, PokemonRegionGymLeadersKeys
from dataclasses import dataclass


@dataclass(frozen=True)
class CollectionInfo:
    name: str
    key : str
    
# Helpful Types
class DatabaseCollections (Enum):
  POKEDEX = CollectionInfo("pokedex", PokedexKeys.GEN_NUMBER)
  POKEMON_REGION_GYM_LEADERS = CollectionInfo("pokemon_region_gym_leaders", PokemonRegionGymLeadersKeys.GEN_NUMBER)
  POKEMON_TYPE_INFO = CollectionInfo("pokemon_type_info", DetailedPokemonTypeKeys.TYPE_NAME)
  POKEMON_OF_TYPE = CollectionInfo("pokemon_of_type", DetailedPokemonTypeKeys.TYPE_NAME)
  MOVES_OF_TYPE = CollectionInfo("moves_of_type", DetailedPokemonTypeKeys.TYPE_NAME)

load_dotenv()

def getDb() -> Database:
    username : str = os.getenv('MONGO_DB_ATLAS_USER')
    password : str = os.getenv('MONGO_DB_ATLAS_PASSWORD')
    clusterId : str = os.getenv('MONGO_DB_ATLAS_CLUSTER')
    appName : str = os.getenv('MONGO_DB_ATLAS_App_NAME')
    dbName : str = os.getenv('MONGO_DB_ATLAS_DB_NAME')

    if not all([username, password, clusterId, dbName]):
        raise ValueError("One or more required environment variables are missing.")

    dBconnectionString : str = f"mongodb+srv://{username}:{password}@{clusterId}/?retryWrites=true&w=majority&appName={appName}"

    client : MongoClient = MongoClient(dBconnectionString)

    db : Database = client[dbName]
    return db

def setupCollections(db : Database):
    # setup collectoins if they dont already exists
    existing_collections : list[str] = db.list_collection_names()

    for collection in DatabaseCollections:
        colName : str = collection.value.name
        colKey : str = collection.value.key
        
        if colName not in existing_collections:
            print(f"Creating new collection: {colName}")
            db.create_collection(colName)
        else:
            print(f"Collection already exists: {colName}")
        
        colObj = db[colName]
        colObj.create_index(colKey, unique=True)

def existsInCollection(collection : Collection, key : str, value : Any) -> bool:
    # check if a document already exists with this key
    result = collection.find_one({key : value})
    return result is not None