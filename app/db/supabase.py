from supabase import create_client, Client
from app.core.config import settings


print("DEBUG URL:", settings.SUPABASE_URL)
print("DEBUG KEY LENGTH:", len(settings.SUPABASE_SECRET_KEY))
if not settings.SUPABASE_URL or not settings.SUPABASE_SECRET_KEY:
    raise ValueError("SUPABASE_URL and SUPABASE_SECRET_KEY must be set in environment variables.")

supabase_client: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_SECRET_KEY)

if not settings.SUPABASE_URL or not settings.SUPABASE_SECRET_KEY:
    raise ValueError("SUPABASE_URL and SUPABASE_SECRET_KEY must be set in environment variables.")

# Initializing with the SECRET_KEY gives your backend admin privileges to access the table
supabase_client: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_SECRET_KEY)