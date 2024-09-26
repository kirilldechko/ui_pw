from faker import Faker
from my_pages.locators.create_account_locators import (first_name_x_path, last_name_x_path, password_field_path,
                                                    confirm_password_field_path, email_field_path)

fake = Faker()
first_name = fake.first_name()
last_name = fake.last_name()
test_email = fake.email()
password = fake.password(length=8)
page_form_name = "Create New Customer Account"
success_report_text = "Thank you for registering with Main Website Store."
requirement_fields = [first_name_x_path, last_name_x_path, email_field_path, password_field_path,
                      confirm_password_field_path]
