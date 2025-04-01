from datetime import date
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from api.models import Employee, WorkInformation, PersonalInformation
from utils import pbdkf2_sha256

def add_sample_data():
    # Thêm các bản ghi cho bảng auth_user
    users_data = [
        {
            "id": 2,
            "username": "act_user_2",
            "email": "act_user_2@gmail.com",
            "password": "Matkhauhople1",
        },
        {
            "id": 3,
            "username": "act_user_3",
            "email": "act_user_3@gmail.com",
            "password": "Matkhauhople1",
        },
        {
            "id": 4,
            "username": "act_user_4",
            "email": "act_user_4@gmail.com",
            "password": "Matkhauhople1",
        },
        {
            "id": 5,
            "username": "act_user_5",
            "email": "act_user_5@gmail.com",
            "password": "Matkhauhople1",
        },
        {
            "id": 6,
            "username": "act_user_6",
            "email": "act_user_6@gmail.com",
            "password": "Matkhauhople1",
        },
        {
            "id": 7,
            "username": "act_user_7",
            "email": "act_user_7@gmail.com",
            "password": "Matkhauhople1",
        },
        {
            "id": 8,
            "username": "act_user_8",
            "email": "act_user_8@gmail.com",
            "password": "Matkhauhople1",
        },
    ]
    for user_data in users_data:
        user_data["password"] = make_password(user_data["password"])
        user_data["date_joined"] = date.today()
        User.objects.create(**user_data)

    # Thêm các bản ghi cho bảng employees
    employees_data = [
        {
            "id": 2,
            "code": "ACTVN02",
            "name": "Nguyễn Văn A",
            "email": "act_user_2@actvn.edu.vn",
            "gender": "male",
            "date_of_birth": "1992-02-02",
            "user_id": 2,
        },
        {
            "id": 3,
            "code": "ACTVN03",
            "name": "Nguyễn Văn B",
            "email": "act_user_3@actvn.edu.vn",
            "gender": "male",
            "date_of_birth": "1993-03-03",
            "user_id": 3,
        },
        {
            "id": 4,
            "code": "ACTVN04",
            "name": "Nguyễn Thị C",
            "email": "act_user_4@actvn.edu.vn",
            "gender": "female",
            "date_of_birth": "1994-04-04",
            "user_id": 4,
        },
        {
            "id": 5,
            "code": "ACTVN05",
            "name": "Nguyễn Thị E",
            "email": "act_user_5@actvn.edu.vn",
            "gender": "female",
            "date_of_birth": "1995-05-05",
            "user_id": 5,
        },
        {
            "id": 6,
            "code": "ACTVN06",
            "name": "Nguyễn Văn F",
            "email": "act_user_6@actvn.edu.vn",
            "gender": "male",
            "date_of_birth": "1996-06-06",
            "user_id": 6,
        },
        {
            "id": 7,
            "code": "ACTVN07",
            "name": "Nguyễn Thị G",
            "email": "act_user_7@actvn.edu.vn",
            "gender": "female",
            "date_of_birth": "1997-07-07",
            "user_id": 7,
        },
        {
            "id": 8,
            "code": "ACTVN08",
            "name": "Nguyễn Văn H",
            "email": "act_user_8@actvn.edu.vn",
            "gender": "male",
            "date_of_birth": "1998-08-08",
            "user_id": 8,
        },
    ]
    for employee_data in employees_data:
        Employee.objects.create(**employee_data)

    # Thêm các bản ghi cho bảng work_informations
    work_info_data = [
        {
            "id": 2,
            "probationary_start_date": "2023-02-02",
            "probationary_end_date": "2023-02-12",
            "official_start_date": "2023-02-12",
            "tax_code": "1234567890",
            "social_insurance_code": "0987654321",
            "type": "sse",
            "level": "jr",
            "employee_id": 2,
        },
        {
            "id": 3,
            "probationary_start_date": "2023-03-03",
            "probationary_end_date": "2023-03-13",
            "official_start_date": "2023-03-13",
            "tax_code": "0987654321",
            "social_insurance_code": "1234567890",
            "type": "cse",
            "level": "mid",
            "employee_id": 3,
        },
        {
            "id": 4,
            "probationary_start_date": "2023-04-04",
            "probationary_end_date": "2023-04-14",
            "official_start_date": "2023-04-14",
            "tax_code": "9876543210",
            "social_insurance_code": "0123456789",
            "type": "qa",
            "level": "sr",
            "employee_id": 4,
        },
        {
            "id": 5,
            "probationary_start_date": "2023-05-05",
            "probationary_end_date": "2023-05-15",
            "official_start_date": "2023-05-15",
            "tax_code": "5678901234",
            "social_insurance_code": "6789012345",
            "type": "pm",
            "level": "ex",
            "employee_id": 5,
        },
        {
            "id": 6,
            "probationary_start_date": "2023-06-06",
            "probationary_end_date": "2023-06-16",
            "official_start_date": "2023-06-16",
            "tax_code": "4567890123",
            "social_insurance_code": "7890123456",
            "type": "sse",
            "level": "sr",
            "employee_id": 6,
        },
        {
            "id": 7,
            "probationary_start_date": "2023-07-07",
            "probationary_end_date": "2023-07-17",
            "official_start_date": "2023-07-17",
            "tax_code": "3456789012",
            "social_insurance_code": "8901234567",
            "type": "cse",
            "level": "jr",
            "employee_id": 7,
        },
        {
            "id": 8,
            "probationary_start_date": "2023-08-08",
            "probationary_end_date": "2023-08-18",
            "official_start_date": "2023-08-18",
            "tax_code": "2345678901",
            "social_insurance_code": "9012345678",
            "type": "qa",
            "level": "mid",
            "employee_id": 8,
        },
    ]
    for work_info in work_info_data:
        WorkInformation.objects.create(**work_info)

    # Thêm các bản ghi cho bảng personal_informations
    personal_info_data = [
        {
            "id": 2,
            "phone_number": "0123456789",
            "citizen_identification_code": "1234567890",
            "personal_email": "nguyenvana@gmail.com",
            "birthplace": "Hà Nội",
            "current_address": "Tân Triều - Thanh Trì - Hà Nội",
            "permanent_address": "Tân Triều - Thanh Trì - Hà Nội",
            "bank_name": "Vietcombank",
            "bank_account_number": "0987654321",
            "education": "Học viện Kỹ thuật Mật Mã",
            "graduation_year": 2020,
            "employee_id": 2,
        },
        {
            "id": 3,
            "phone_number": "0987654321",
            "citizen_identification_code": "0987654321",
            "personal_email": "nguyenvanb@gmail.com",
            "birthplace": "Hà Nam",
            "current_address": "Cầu Giấy - Hà Nội",
            "permanent_address": "Thành phố Hải Phòng",
            "bank_name": "Vietcombank",
            "bank_account_number": "1234567890",
            "education": "Trường Đại học Khoa học Tự nhiên",
            "graduation_year": 2021,
            "employee_id": 3,
        },
        {
            "id": 4,
            "phone_number": "0976543210",
            "citizen_identification_code": "9876543210",
            "personal_email": "nguyenthic@gmail.com",
            "birthplace": "Hải Dương",
            "current_address": "Ba Đình - Hà Nội",
            "permanent_address": "Thành phố Quảng Ninh",
            "bank_name": "Vietcombank",
            "bank_account_number": "0123456789",
            "education": "Đại học Ngoại thương",
            "graduation_year": 2022,
            "employee_id": 4,
        },
        {
            "id": 5,
            "phone_number": "0901234567",
            "citizen_identification_code": "5678901234",
            "personal_email": "nguyenthide@gmail.com",
            "birthplace": "Nam Định",
            "current_address": "Đống Đa - Hà Nội",
            "permanent_address": "Thành phố Bắc Ninh",
            "bank_name": "Vietcombank",
            "bank_account_number": "6789012345",
            "education": "Học viện Bưu chính Viễn thông",
            "graduation_year": 2023,
            "employee_id": 5,
        },
        {
            "id": 6,
            "phone_number": "0965432109",
            "citizen_identification_code": "4567890123",
            "personal_email": "nguyenvanf@gmail.com",
            "birthplace": "Thái Bình",
            "current_address": "Tây Hồ - Hà Nội",
            "permanent_address": "Thành phố Thái Nguyên",
            "bank_name": "Vietcombank",
            "bank_account_number": "7890123456",
            "education": "Trường Đại học Sư phạm Hà Nội",
            "graduation_year": 2024,
            "employee_id": 6,
        },
        {
            "id": 7,
            "phone_number": "0943210876",
            "citizen_identification_code": "3456789012",
            "personal_email": "nguyenthigh@gmail.com",
            "birthplace": "Vĩnh Phúc",
            "current_address": "Hai Bà Trưng - Hà Nội",
            "permanent_address": "Thành phố Hà Tĩnh",
            "bank_name": "Vietcombank",
            "bank_account_number": "8901234567",
            "education": "Trường Đại học Ngoại thương",
            "graduation_year": 2025,
            "employee_id": 7,
        },
        {
            "id": 8,
            "phone_number": "0912345678",
            "citizen_identification_code": "2345678901",
            "personal_email": "nguyenvanh@gmail.com",
            "birthplace": "Hòa Bình",
            "current_address": "Hoàng Mai - Hà Nội",
            "permanent_address": "Thành phố Ninh Bình",
            "bank_name": "Vietcombank",
            "bank_account_number": "9012345678",
            "education": "Trường Đại học Kinh tế Quốc dân",
            "graduation_year": 2026,
            "employee_id": 8,
        },
    ]
    for personal_info in personal_info_data:
        PersonalInformation.objects.create(**personal_info)


add_sample_data()
