from supabase import create_client, Client
from app.config import SUPABASE_KEY, SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

