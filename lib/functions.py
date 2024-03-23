from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model import Doctor, Patient

engine = create_engine("sqlite:///hospitals.db")
mysession = sessionmaker(bind=engine)
session = mysession()

def list_doctors():
    print ("Listing all doctors:")
    doctors = session.query(Doctor).all()
    for doctor in doctors:
        print(doctor)

def find_doctor_by_name():
    name = input("Enter your Doctor's name:")
    doctor = session.query(Doctor).filter_by(doctor_name=name).first()
    print(
        "NAME: ", doctor.doctor_name,
        "SPECIALITY: ", doctor.speciality,
        "LICENSE NUMBER: ", doctor.license_number
    )  

def find_doctor_by_id():
    id_num = input("Enter your Doctor's ID number: ")
    doctor = session.query(Doctor).filter_by(id=id_num).first()
    print(
        "ID: ", doctor.id,
        "NAME: ", doctor.doctor_name,
        "SPECIALITY: ", doctor.speciality,
        "LICENSE NUMBER: ", doctor.license_number
    )  

def add_new_doctor():
    doctor_id = input("Enter the Doctor's unique ID number: ")
    doctor_name = input("Enter  the Doctor's Name: ")
    specialization = input("What is the Doctor's Specialty? ")
    license_no = input("Enter the License Number of this Doctor: ")

    new_doctor = Doctor(id=doctor_id, doctor_name=doctor_name, speciality=specialization, license_number=license_no)

    session.add(new_doctor)
    session.commit()
    print(f"The New doctor {doctor_name} has been added succesfully.")

def dismiss_doctor():
    dr_id = input("Enter the  ID of the doctor you want to delete: ")
    #dr_name = input("Enter the name of the doctor you want to delete: ")
    #dr_spec = input("Enter the specialty of the doctor you want to delete  : ")
    doctor_to_delete = session.query(Doctor).filter_by(id=dr_id).one()
    session.delete(doctor_to_delete)
    session.commit()
    print(f"The doctor with id {dr_id} has been deleted Successfully!")

def list_patients():
    print ("Listing all patients:")
    patients = session.query(Patient).all()
    for patient in patients:
        print(patient)

def find_patient_by_name():
    name = input("Enter your Patient's name:")
    patient = session.query(Patient).filter_by(patient_name=name).first()
    print(
        "NAME: ", patient.patient_name,
        "AGE: ", patient.age,
        "GENDER: ", patient.gender,
        "SICKNESS: ", patient.sickness,
        "PATIENT'S DOCTOR ID: ", patient.doctor_id
    )  

def find_patient_by_id():
    id_num = input("Enter your Patient's ID number:")
    patient = session.query(Patient).filter_by(id=id_num).first()
    print(
        "ID: ", patient.id ,
        "NAME: ", patient.patient_name ,
        "AGE: ", patient.age ,
        "GENDER: ", patient.gender ,
        "SICKNESS: ", patient.sickness ,
        "PATIENT'S DOCTOR ID: ", patient.doctor_id
    ) 

def admit_new_patient():
    patient_id = input("Enter the new patient's ID number: ")
    patient_name = input("Enter the new patient's Name : ")
    age = int(input("Enter the new patient's Age : "))
    gender = input("Is the new patient a Male or Female? ")
    sickness = input("What is the new patient's Sickness ? ")
    doctor_id = input("Enter the Doctor's ID who treats this patient: ")

    new_patient = Patient(id=patient_id, patient_name=patient_name, age=age, gender=gender, sickness=sickness, doctor_id=doctor_id)

    session.add(new_patient)
    session.commit()
    print(f"The new patient {patient_name} has been  added to the system!")

def discharge_patient():
    patient_id = input("Enter the ID of the patient you want to  Discharge: ")
    discharge_patient = session.query(Patient).filter_by(id=int(patient_id)).one()
    session.delete(discharge_patient)
    session.commit()
    print(f"The Patient with ID:{patient_id} has been successfully discharged from this Hospital")

def exit_program():
    print("GOODBYE!!!! THANK YOU!!!")
    exit()          
