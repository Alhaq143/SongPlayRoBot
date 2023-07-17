import os
API_ID = int(os.getenv("27730948"))
API_HASH = os.getenv("5a59be7f1753e4a0c21d3b68c89efaf8")
BOT_TOKEN = os.getenv("6124433807:AAFLeTMZQGQ0W5xjkLQ3I_pQcDSuXGgY_Cs")
DATABASE_URL = os.getenv("DATABASE_URL")
OWNER_ID = list({int(x) for x in os.environ.get("OWNER_ID", "6114275366").split()})
