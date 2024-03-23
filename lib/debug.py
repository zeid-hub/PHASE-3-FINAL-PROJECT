from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model import Doctor, Patient, Department

fake = Faker()

if __name__ == '__main__':
    # Create engine and session
    engine = create_engine("sqlite:///hospitals.db")

    mysession = sessionmaker(bind=engine)
    session = mysession()

    import ipdb; ipdb.set_trace()