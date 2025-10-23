  import os
    from dotenv import load_dotenv

    # Load environment variables from .env file
    load_dotenv()

    # Access the variables
    api_key = os.getenv("API_KEY")
    database_url = os.getenv("DATABASE_URL")

    print(f"API Key: {api_key}")
    print(f"Database URL: {database_url}")