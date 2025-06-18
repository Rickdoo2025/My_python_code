#This file contains the query that need to be executed 


#####################################################
#THIS WILL CREATE A INNER JOIN QUERY
#SELECT * FROM ACTOR INNER JOIN ADDRESS ON ACTOR.ACTOR_ID = ADDRESS.ADDRESS_ID WHERE ACTOR_ID = 1 AND ADDRESS_ID = 1
#####################################################
def get_join_data(actor_id=None, address_id=None):
    base_query = "SELECT * FROM actor INNER JOIN address ON actor.actor_id = address.address_id"

    if actor_id & address_id:
        base_query+= f" WHERE actor_id = {actor_id} AND address_id = {address_id}"
        print(base_query)
        return base_query

######################################################
#THIS WILL CREATE ACTOR QUERY WITH WHERE CLAUSE
#SELECT * FROM actor WHERE ACTOR_ID = 1
######################################################
def get_actors(actor_id=None):
    base_query = "SELECT * FROM actor"

    if actor_id:
        base_query+= f" WHERE actor_id = {actor_id}"
        print(base_query)
    return base_query

def get_multi_actors(actor_id: list[int]):
    base_query = "SELECT * FROM actor"
    if actor_id:
        actor_ids = ", ".join(map(str, actor_id))
        base_query += f" WHERE actor_id IN ({actor_ids})" 
    return base_query

######################################################
#THIS WILL CREATE Address QUERY WITH WHERE CLAUSE
#SELECT * FROM actor WHERE ADDRESS_ID = 1
######################################################

def get_address(address_id=None):
    base_query = "SELECT * FROM address"

    if address_id:
        base_query+= f" WHERE address_id = {address_id}"
        print(base_query)
    return base_query

# GET_ACTORS = """ 
#    SELECT * FROM actor 
# """
# GET_ADDRESS = """ 
#    SELECT * FROM address 
# """