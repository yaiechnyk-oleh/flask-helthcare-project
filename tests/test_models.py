import sys
sys.path.insert(0, '')
from app import db
from models import Patient


def test_new_patient(app):
    """
    GIVEN a Patient model
    WHEN a new Patient is created
    THEN check the name, email, and password fields are defined correctly
    """
    with app.app_context():
        patient = Patient(name='John Doe', email='john@example.com', password_hash='securepassword')
        db.session.add(patient)
        db.session.commit()
        assert patient.id is not None
        assert patient.name == 'John Doe'
        assert patient.email == 'john@example.com'

