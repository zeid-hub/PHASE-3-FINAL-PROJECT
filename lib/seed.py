from faker import Faker
import random

from model import Doctor, Patient, Department, create_engine, sessionmaker

fake = Faker()

# Define a list of doctor specialties
doctor_specialties = [
    "Cardiology",
    "Orthopedics",
    "Pediatrics",
    "Dermatology",
    "Neurology",
    "Oncology",
    "Gynecology",
    "Urology",
    "Ophthalmology",
    "Psychiatry",
    "Radiology",
    "Anesthesiology",
    "Endocrinology",
    "Gastroenterology",
    "Hematology",
    "Nephrology",
    "Pulmonology",
    "Rheumatology",
    "Surgery",
    "Family Medicine",
    "Internal Medicine",
    "Emergency Medicine",
    "Pathology",
    "Otolaryngology",
    "Infectious Diseases",
    "Physical Medicine & Rehabilitation"
]

patient_sicknesses = [
    "Influenza (Flu)",
    "Common Cold",
    "Pneumonia",
    "Bronchitis",
    "Asthma",
    "Tuberculosis (TB)",
    "COVID-19 (Coronavirus)",
    "Malaria",
    "Dengue Fever",
    "Cholera",
    "Gastroenteritis",
    "Hepatitis",
    "HIV/AIDS",
    "Diabetes",
    "Hypertension (High Blood Pressure)",
    "Arthritis",
    "Cancer",
    "Stroke",
    "Alzheimer's Disease",
    "Depression"
]

# doctor = Doctor()

if __name__ == '__main__':
    # Create engine and session
    engine = create_engine("sqlite:///hospitals.db")

    mysession = sessionmaker(bind=engine)
    session = mysession()
    
    session.query(Doctor).delete()
    doctors = [
        Doctor(
            doctor_name = fake.name(),
            speciality = random.choice(doctor_specialties),
            license_number = random.randint(10000, 99999)
        )
    for i in range(50)]
    session.add_all(doctors)
    session.commit()
    all_doctors = session.query(Doctor).all()
    # print(all_doctors)

    patients = [
        Patient(
            patient_name = fake.name(),
            age = random.randint(0,100),
            gender = random.choice(['Male', 'Female']),
            sickness =  random.choice(patient_sicknesses),
            doctor_id = doctor.id
            )
    for doctor in all_doctors
    # for i in range(20)
    ]
    session.query(Patient).delete()
    session.commit()
    
    # doctors = session.query(Doctor).all()
    # for doctor in doctors:
    #     print(doctor.id)
    
    session.add_all(patients)
    session.commit()
    