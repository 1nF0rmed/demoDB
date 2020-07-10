from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()

"""
Defining the user model for the table user.
User has the following attributes:
- id:int: The ID the user
- email:string: The email of the user
- first_name: string: The first name of the user
- last_name: string: The last name of the user
"""
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    first_name = Column(String)
    last_name = Column(String)

    # Method that is called when printing
    # an object of the class
    def __repr__(self):
        return "<User(id={}, email='{}', first_name='{}', last_name='{}')>" \
            .format(self.id, self.email, self.first_name, self.last_name)
