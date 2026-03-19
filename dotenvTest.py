# Import the necessary module
from dotenv import load_dotenv
import os

# Load environment variables from the .env file (if present)
load_dotenv()

# Access environment variables as if they came from the actual environment
mongoDBConnection = os.getenv('mongoDBConnection')

# Example usage
print(f'mongoDBConnection: {mongoDBConnection}')