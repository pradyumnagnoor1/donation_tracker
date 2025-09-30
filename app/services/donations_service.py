from app.deps.db import supabase


#inserts donation record into supabase table
def create_donation(data: dict):
    res = supabase.table('donations').insert(data).execute()
    return res.data[0]

#returns donation list from supabase table
def list_donations(limit: int = 50):
    return supabase.table('donations').select('*').order("id", desc=True).limit(limit).execute().data

