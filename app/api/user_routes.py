# app/api/user_routes.py
from fastapi import APIRouter, Query
import json
from app.services.user_services import run_user_service
from app.db.query import get_actors
from app.db.query import get_address
from app.db.query import get_join_data
from app.db.query import get_multi_actors

router = APIRouter()

@router.get("/")
def root():
    return {"message": "✅ FastAPI backend is running. Use endpoints like /actors, /address, or /join"}

# Endpoint to fetch actor data from the database.
# If `actor_id` is provided as a query parameter, it filters the result accordingly.
# The query is generated using `get_actors()`, and results are fetched via `run_user_service()`.
# Returns JSON data if found, otherwise an error message.

@router.get("/actor")
def get_actor(actor_id: int = Query(None)):
    query = get_actors(actor_id)
    actors = run_user_service(query, return_json=True)
    return json.loads(actors) if actors else {f" error: No actors found with this actor_id:{actor_id}"}

# Endpoint to fetch address data from the database.
# If `address_id` is provided as a query parameter, it filters the result accordingly.
# The SQL query is constructed using `get_address()`, and data is retrieved using `run_user_service()`.
# Returns the result in JSON format if found, otherwise returns an error message.

@router.get("/address")
def get_addresses(address_id: int = Query(None)):
    query = get_address(address_id)
    address = run_user_service(query, return_json=True)
    return json.loads(address) if address else {f" error: No address found with this address_id:{address_id}"}

# Endpoint to fetch joined data from multiple tables (e.g., actor and address).
# Accepts optional query parameters `actor_id` and `address_id` to filter the join result.
# Constructs the SQL join query using `get_join_data()` and executes it via `run_user_service()`.
# Returns the result as JSON if found, otherwise returns an appropriate error message.

@router.get("/join")
def get_join(actor_id: int = Query(None), address_id: int = Query(None)):
    query = get_join_data(actor_id, address_id)
    join = run_user_service(query, return_json=True)
    return json.loads(join) if join else {f" error: No data found with this address_id: {address_id} & actor_id: {actor_id}"}



@router.get("/actor/multi")
def get_actors_multi(actor_id: list[int] = Query(None)):
    query = get_multi_actors(actor_id)
    multi_actor = run_user_service(query, return_json=True)
    return json.loads(multi_actor)

