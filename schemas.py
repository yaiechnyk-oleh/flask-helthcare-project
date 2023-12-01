from marshmallow import Schema, fields, validate
from datetime import datetime

class PatientSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    date_of_birth = fields.Date(required=True)
    # Password is write-only
    password = fields.Str(load_only=True, required=True, validate=validate.Length(min=6))
    appointments = fields.Nested('AppointmentSchema', many=True, exclude=('patient',))
    medical_records = fields.Nested('MedicalRecordSchema', many=True, exclude=('patient',))

class DoctorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    specialization = fields.Str(required=True)
    appointments = fields.Nested('AppointmentSchema', many=True, exclude=('doctor',))

class AppointmentSchema(Schema):
    id = fields.Int(dump_only=True)
    date_time = fields.DateTime(required=True, format='%Y-%m-%d %H:%M:%S')
    patient_id = fields.Int(load_only=True)
    doctor_id = fields.Int(load_only=True)
    description = fields.Str(missing=None)
    status = fields.Str(dump_only=True)
    patient = fields.Nested('PatientSchema', only=('id', 'name', 'email'), dump_only=True)
    doctor = fields.Nested('DoctorSchema', only=('id', 'name', 'specialization'), dump_only=True)

class MedicalRecordSchema(Schema):
    id = fields.Int(dump_only=True)
    details = fields.Str(required=True)
    date_recorded = fields.DateTime(dump_only=True, default=datetime.utcnow)
    patient_id = fields.Int(load_only=True)
    patient = fields.Nested('PatientSchema', only=('id', 'name', 'email'), dump_only=True)
