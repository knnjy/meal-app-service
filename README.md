# FastAPI + Supabase Project (Layered Architecture)

## Setup Instructions

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment Variables:**
   Create a `.env` file based on `.env.example`:
   ```bash
   cp .env.example .env
   ```
   Fill in your actual `SUPABASE_URL` and `SUPABASE_KEY`.

3. **Run the Application:**
   ```bash
   uvicorn app.main:app --reload
   ```

4. **Access API Documentation:**
   Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.
