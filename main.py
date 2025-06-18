import sys
import os

# Add app/ to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__)))

from app.services.user_services import run_user_service  # Import your function
from app.db.query import JOIN_QUERY
from app.db.query import GET_ACTORS
from app.db.query import GET_ADDRESS

choice = input("Enter choice (1/2/3): ").strip()

def main():
    print("🚀 Running User Service...\n")
    if choice == "1":
        json_result = run_user_service(JOIN_QUERY, return_json=True)
        # Optionally, write to file
        with open("Join.json", "w") as f:
            f.write(json_result)
    elif choice == "2":
        json_result = run_user_service(GET_ACTORS, return_json=True)
        # Optionally, write to file
        with open("Actor.json", "w") as f:
            f.write(json_result)
    elif choice == "3":
        json_result =  run_user_service(GET_ADDRESS, return_json=True)
        with open("Address.json", "w") as f:
            f.write(json_result)
    else:
        print("Only 1/2/3 is avail illetrate.")

if __name__ == "__main__":
    main()