from datetime import datetime
from entities.License import License
from DbConifg import engine, Base, session

def initialise():
    Base.metadata.create_all(engine)


def add_license(license_number, timestamp=None):
    try:
        new_license = License(
            license=license_number, timestamp=timestamp or datetime.utcnow()
        )
        session.add(new_license)
        session.commit()
        print("License added successfully to the database.")
    except Exception as e:
        print(f"Error: {e}")
        session.rollback()
    finally:
        session.close()


def getAll():
    return session.query(License).all()


def print_licences(licenses):
    for license in licenses:
        print(
            f"License ID: {license.id}, License Number: {license.license}, Timestamp: {license.timestamp}"
        )

##SAMPLE CALLS
# add_license("UP90 2434")
# print_licences(getAll())
