import requests
from models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'postgres+psycopg2://demo:demo@db:5432/test'
engine = create_engine(DATABASE_URI)

# This line creates the table in the database
#User.metadata.create_all(engine)

# Create a database session
session = sessionmaker(bind=engine)
sess = session()

# URL for API call
# page is the GET parameter to get user data
DATA_URL = 'https://reqres.in/api/users?page={}'
try:
    for i in range(1,3):
        # Make a GET request to the url
        resp = requests.get(url=DATA_URL.format(i))
        # Convert the data to JSON
        data = resp.json()

        # Get the users data
        users = data["data"]
        print("Users: ")
        for user in users:
            print("User: ")
            print(user)
            # Create user object
            user = User(
                id=user["id"],
                email=user["email"],
                first_name=user["first_name"],
                last_name=user["last_name"]
            )
            # Add user to the database
            sess.add(user)
            # Commit changes to the database
            # You might want to commit once you have completed
            # a batch of rows
            sess.commit()
            print("[LOG] Updated to database")
except Exception as e:
    print("[ERR][LOG] Exception occurred. Breaking process")
    print(e)
# Close the session
sess.close()