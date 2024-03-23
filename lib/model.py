from sqlalchemy import  Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, backref, relationship

Base = declarative_base()

# doctor_patient_association = Table(
#     'doctor_patient_association',
#     Base.metadata,
#     Column('doctor_id', Integer, ForeignKey('doctors.id')),
#     Column('patient_id', Integer, ForeignKey('patients.id'))
# )

class Doctor(Base):

    __tablename__ = "doctors"

    id = Column(Integer(), primary_key=True)
    doctor_name = Column(String())
    speciality = Column(String())
    license_number = Column(String())

    patients = relationship("Patient", backref="doctor")

    def __repr__(self):
        return f"<Doctor(id={self.id}, name={self.doctor_name}, specialization={self.speciality}, license_number={self.license_number})>"
    


class Patient(Base):

    __tablename__ = "patients"

    id = Column(Integer(), primary_key=True)
    patient_name = Column(String())
    age = Column(Integer())
    gender = Column(String())
    sickness = Column(String())
    doctor_id = Column(Integer(), ForeignKey("doctors.id"))

    def __repr__(self):
        return f"<Patient(id={self.id}, name={self.patient_name}, age= {self.age}, gender={self.gender}, sickness={self.sickness}, patients_doctor={self.doctor_id})>"


# class Appointment(Base):

#     __tablename__ = "appointments"

#     id = Column(Integer, primary_key=True)
#     doctor_id = Column(Integer(), ForeignKey('doctors.id'))
#     patient_id = Column(Integer(), ForeignKey('patients.id'))
#     appointment_time = Column(DateTime)
#     appointment_type = Column(String())
#     status = Column(String())
#     room_location = Column(String())


    