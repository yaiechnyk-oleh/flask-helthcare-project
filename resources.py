import paginate as paginate
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from models import Patient, Doctor, Appointment
from schemas import PatientSchema, DoctorSchema, AppointmentSchema
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash
from flask import request
from database import db
# Blueprint setup
patient_blp = Blueprint('patients', 'patients', url_prefix='/api/patients')
doctor_blp = Blueprint('doctors', 'doctors', url_prefix='/api/doctors')
appointment_blp = Blueprint('appointments', 'appointments', url_prefix='/api/appointments')

# Patient Resource
@patient_blp.route('/')
class Patients(MethodView):

    # POST - Register new patient
    @patient_blp.arguments(PatientSchema)
    @patient_blp.response(201, PatientSchema)
    def post(self, new_data):
        try:
            new_patient = Patient(**new_data)
            new_patient.set_password(new_data['password'])
            db.session.add(new_patient)
            db.session.commit()
            return new_patient
        except IntegrityError:
            db.session.rollback()
            abort(400, message="Email already exists.")

    # GET - Retrieve all patients with optional search
    # @paginate()
    @patient_blp.response(200, PatientSchema(many=True))
    def get(self):
        query = Patient.query
        search = request.args.get('search')
        if search:
            query = query.filter(Patient.name.contains(search))
        return query

# Patient Login
@patient_blp.route('/login', methods=['POST'])
class PatientLogin(MethodView):

    # POST - Patient login
    def post(self):
        email = request.json.get('email')
        password = request.json.get('password')
        patient = Patient.query.filter_by(email=email).first()
        if patient and check_password_hash(patient.password_hash, password):
            token = create_access_token(identity=patient.id)
            return {"token": token}
        else:
            abort(401, message="Invalid credentials.")

# Doctor Resource
@doctor_blp.route('/')
class Doctors(MethodView):

    # POST - Register new doctor
    @doctor_blp.arguments(DoctorSchema)
    @doctor_blp.response(201, DoctorSchema)
    def post(self, new_data):
        try:
            new_doctor = Doctor(**new_data)
            db.session.add(new_doctor)
            db.session.commit()
            return new_doctor
        except IntegrityError:
            db.session.rollback()
            abort(400, message="Email already exists.")

    # GET - Retrieve all doctors
    # @paginate()
    @doctor_blp.response(200, DoctorSchema(many=True))
    def get(self):
        return Doctor.query.all()

# Appointment Resource
@appointment_blp.route('/')
class Appointments(MethodView):

    # POST - Create new appointment
    @jwt_required()
    @appointment_blp.arguments(AppointmentSchema)
    @appointment_blp.response(201, AppointmentSchema)
    def post(self, new_data):
        current_user_id = get_jwt_identity()
        new_data['patient_id'] = current_user_id
        try:
            new_appointment = Appointment(**new_data)
            db.session.add(new_appointment)
            db.session.commit()
            return new_appointment
        except IntegrityError:
            db.session.rollback()
            abort(400, message="Error in creating appointment.")

    # GET - Retrieve all appointments for logged-in patient
    @jwt_required()
    # @paginate()
    @appointment_blp.response(200, AppointmentSchema(many=True))
    def get(self):
        current_user_id = get_jwt_identity()
        return Appointment.query.filter_by(patient_id=current_user_id)

# Appointment Status Update
@appointment_blp.route('/<int:appointment_id>/status')
class AppointmentStatus(MethodView):

    # PUT - Update appointment status
    @jwt_required()
    def put(self, appointment_id):
        appointment = Appointment.query.get_or_404(appointment_id)
        new_status = request.json.get('status')
        if new_status:
            appointment.status = new_status
            db.session.commit()
            return {"message": "Appointment status updated."}
        else:
            abort(400, message="Status not provided.")
