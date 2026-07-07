from dotenv import load_dotenv
import os

print("🚀 ConfigBot Challenge Solution - Episode 65\n")

# Step 1: Load .env file
load_dotenv()

# Step 2: List of required variables
REQUIRED_VARS = ["DB_HOST", "DB_PORT", "API_KEY", "DEBUG"]

# Step 3: Validate + Fail Fast
print("🔍 Validating required environment variables...")
for key in REQUIRED_VARS:
    if key not in os.environ:
        raise RuntimeError(f"❌ Missing required environment variable: {key}")
    print(f"✅ {key} = {os.environ[key][:4] + '****' if len(os.environ[key]) > 8 else os.environ[key]}")

# Step 4: Type casting
db_port = int(os.environ["DB_PORT"])
debug_mode = os.environ.get("DEBUG", "False").lower() == "true"

print(f"\n✅ DB_PORT as integer: {db_port}")
print(f"✅ DEBUG as boolean: {debug_mode}")

# Step 5: Config object
config = {
    "db_host": os.environ["DB_HOST"],
    "db_port": db_port,
    "api_key": os.environ["API_KEY"],
    "debug": debug_mode,
}

print("\n🎉 Config loaded successfully!")
print("   Ready for production use.")

# Reminder about .env and .gitignore
print("\n💡 Remember: .env must be in .gitignore!")
