from sqlalchemy import Column, String, Date, Text, Numeric, Integer
from sqlalchemy.dialects.postgresql import UUID
from app.database.database import Base

class Patient(Base):
    __tablename__ = "patients"
    __table_args__ = {"schema": "emr_schema"}  # 🔥 VERY IMPORTANT

    id = Column(UUID(as_uuid=True), primary_key=True)
    mrn = Column(String, unique=True, index=True)
    full_name = Column(Text)
    gender = Column(Text)
    dob = Column(Date)


class Visit(Base):
    __tablename__ = "visits"
    __table_args__ = {"schema": "emr_schema"}

    id = Column(UUID(as_uuid=True), primary_key=True)
    patient_id = Column(UUID(as_uuid=True))
    visit_date = Column(Date)
    diagnosis = Column(Text)


class Allergy(Base):
    __tablename__ = "allergies"
    __table_args__ = {"schema": "emr_schema"}

    id = Column(UUID(as_uuid=True), primary_key=True)
    patient_id = Column(UUID(as_uuid=True))
    allergy_name = Column(String)
    reaction = Column(String)
    severity = Column(String)
    recorded_at = Column(Date)


class LabResult(Base):
    __tablename__ = "lab_results"
    __table_args__ = {"schema": "emr_schema"}

    id = Column(UUID(as_uuid=True), primary_key=True)
    patient_id = Column(UUID(as_uuid=True))
    test_name = Column(String)
    value = Column(String)
    normal_range = Column(String)
    test_date = Column(Date)

class VitalSign(Base):
    __tablename__ = "vital_signs"
    __table_args__ = {"schema": "emr_schema"}

    id = Column(UUID(as_uuid=True), primary_key=True)
    patient_id = Column(UUID(as_uuid=True))
    systolic_bp = Column(Integer)
    diastolic_bp = Column(Integer)
    heart_rate = Column(Integer)
    respiratory_rate = Column(Integer)
    temperature = Column(Numeric(4, 1))
    oxygen_saturation = Column(Integer)
    notes = Column(Text)