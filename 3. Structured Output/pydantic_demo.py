from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'Rishu' # default value
    age: Optional[int] = None # put None for optional attributes
    email: EmailStr # validation
    cgpa: float = Field(gt=0, lt=10, default=5, description='A decimal value representing the cgpa of the student')
    # cgpa constraint 0-10


new_student = {'age':'21', 'email':'abc@gmail.com'}

student = Student(**new_student) # pydantic object

student_dict = dict(student)
print(student_dict['age'])

student_json = student.model_dump_json()
print(student_json)