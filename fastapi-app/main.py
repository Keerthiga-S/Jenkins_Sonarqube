from fastapi import FastAPI

app = FastAPI()

# ⚠️ Hardcoded secrets (for testing SonarQube & Jenkins detection)

password = "admin123"
api_key = "AKIAIOSFODNN7EXAMPLE"
secret_token = "ghp_1234567890abcdef1234567890abcdef"
strong_password = "P@ssw0rd123!"

@app.get("/")
def read_root():
    return {
        "message": "Hello World",
        "note": "This app contains hardcoded secrets for testing"
    }