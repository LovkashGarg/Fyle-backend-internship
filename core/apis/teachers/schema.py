from sqlalchemy import Column, Integer, String, Date, Enum, Text, Boolean, DateTime


class Teacher(Base):
    __tablename__ = 'teacher'

    teacher_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone_number = Column(String(20))
    date_of_birth = Column(Date)
    gender = Column(Enum('Male', 'Female', 'Other'))
    address = Column(Text)
    city = Column(String(50))
    state = Column(String(50))
    country = Column(String(50))
    zip_code = Column(String(20))
    department = Column(String(50))
    subject_specialization = Column(String(50))
    years_of_experience = Column(Integer)
    qualification = Column(String(100))
    hire_date = Column(Date)
    salary = Column(String(10))  # Adjust data type as needed
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)