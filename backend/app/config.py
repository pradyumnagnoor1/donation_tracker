import os
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL= os.getenv("supabase_url")
SUPABASE_KEY= os.getenv("supabase_key")
SUPABASE_SERVICE_ROLE_KEY= os.getenv("supabase_service_role_key")
JWT_AUDIENCE= os.getenv("supabase_jwt_audience")