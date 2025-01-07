from src.auth.auth import authenticate

if __name__ == "__main__":
  creds = authenticate()
  print("Authentication succesful:", creds)