#Folder structure that i followed

my_project/
├── app/
│   ├── __init__.py
│   ├── config.py           # DB configs and other environment configs
│   ├── db/
│   │   ├── __init__.py
│   │   ├── connection.py   # MySQL connection logic
│   │   ├── models.py       # DB table models (if using raw SQL or SQLAlchemy)
│   │   └── queries.py      # SQL queries or ORM methods
│   ├── routes/
│   │   ├── __init__.py
│   │   └── user_routes.py  # API routes or CLI handlers
│   └── services/
│       ├── __init__.py
│       └── user_service.py # Business logic
├── tests/
│   ├── __init__.py
│   ├── test_db.py
│   └── test_user_service.py
├── scripts/
│   └── setup_db.py         # DB creation and seed scripts
├── .env                    # Environment variables (MySQL creds etc.)
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
└── main.py                 # Entry point (e.g., Flask app, CLI app)

############################################################
# Connecting the code of DB
File to write your DB connection code:
# app/db/connection.py
This file will act as the central place to configure and manage your database connection, which can then be reused across models, services, or repositories.
############################################################

############################################################
# Consuming connection code 
# app/services/user_services.py
This file contains logic for Query execution logic
############################################################

############################################################
# Contains all the queries 
# app/db/query.py
This file contains all SQL query
############################################################

#New modified folder structure 

your_project/
├── app/
│   ├── api/                    # <-- FastAPI routers go here
│   │   └── user_routes.py      # <-- Your user endpoint(s)
│   ├── db/
│   │   ├── connection.py
│   │   └── query.py
│   ├── services/
│   │   └── user_services.py
│   └── main.py                 # <-- FastAPI app lives here
├── .env
├── requirements.txt

