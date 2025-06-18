import json
import struct
from datetime import datetime, date
from decimal import Decimal
from app.db.connection import get_db_connection
from tabulate import tabulate  # Optional: used for pretty terminal output


def custom_serializer(obj):
    """Converts datetime, Decimal, and bytearray to serializable formats."""
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, Decimal):
        return float(obj)
    elif isinstance(obj, bytearray):
        return obj.decode("utf-8")
    # elif isinstance(obj, (bytes, memoryview)):
    #     try:
    #         # Attempt to decode MySQL POINT (WKB format)
    #         # MySQL WKB POINT = [byte order][wkbType][X][Y]
    #         # Skip first 4 + 4 bytes → struct.unpack from byte 9
    #         if len(obj) >= 21:
    #             _, _, x, y = struct.unpack('<BIdd', obj[:21])
    #             return {"longitude": x, "latitude": y}
    #     except Exception:
    #         return str(obj)  # fallback to string if not a POINT
    return str(obj)  # fallback for unknown types

# Executes the provided SQL query using a database connection.
# If `return_json` is True, it returns the result as a JSON string with proper serialization (e.g., datetime).
# If `return_json` is False, it prints the result in a tabular format using `tabulate`.
# Handles connection management, query execution, error logging, and resource cleanup.

def run_user_service(query, return_json=False):
    conn = get_db_connection()
    if conn:
        try:
            # Use dictionary cursor for easier JSON conversion
            cursor = conn.cursor(dictionary=True)
            cursor.execute(query)

            result = cursor.fetchall()  # Already list of dicts

            if return_json:
                json_data = json.dumps(result, indent=2, default=custom_serializer)
                return json_data
            else:
                if result:
                    columns = result[0].keys()
                    rows = [row.values() for row in result]
                    print(tabulate(rows, headers=columns, tablefmt="grid"))
                else:
                    print("No data found.")

        except Exception as e:
            print("❌ Error executing query:", e)
            return None
        finally:
            conn.close()
    else:
        print("❌ Failed to connect to database.")
        return None
