import requests
import smtplib

SHEETY_API_URL = "https://api.sheety.co/0fc5274f5d6063f6846b098b6f9ed159/eligibleStudents/sheet1"


def get_student_data():
    

    response = requests.get(SHEETY_API_URL)
    data = response.json()
    return data.get("eligible students")

def send_admission_email(name, father_name, student_class, student_email):
    sender_email = "your@gmail.com"  
    password = "xxxx xxxx xxxx"  
    subject = "Congratulations! Admission Eligibility Confirmation"
    body = f""" 
    Dear {name},

    Congratulations! We are pleased to inform you that you are eligible for admission to our school in {student_class} based on your interview and academic performance.

    We are excited to have you join us and look forward to your contribution to our school community.

    Best Regards,
    School Admission Team
    """

    message = f"Subject: {subject}\n\n{body}"
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, student_email, message)
        print(f"Admission eligibility email sent to {student_email} successfully!")

students = get_student_data()


for student in students:
    name = student["Names"]
    father_name = student["FatherName"]
    student_class = student["CLASS"]
    student_email = student["StudentsEmails"]

    
    send_admission_email(name, father_name, student_class, student_email)
