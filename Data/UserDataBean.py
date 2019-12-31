import random
import string

domains = ["mailinator.com"]
ascii_lowercase_letters = string.ascii_lowercase[:26]
ascii_uppercase_letters = string.ascii_uppercase[:26]
print(ascii_lowercase_letters)
print(ascii_uppercase_letters)
digits = string.digits
phone_digits = '023456789'


class UserDataBean:
    def get_random_user_data(self, email_id_type='get_random_string'):
        user_info = {}

        method_to_call = getattr(self, email_id_type)
        username = method_to_call()

        email = self.random_email(username)
        user_info['email'] = email

        firstname = method_to_call()
        user_info['firstname'] = firstname

        lastname = self.get_random_string()
        user_info['lastname'] = lastname

        password = self.generate_password()
        user_info['password'] = password

        company = self.get_random_string()
        user_info['company'] = company

        address = self.get_random_string()
        user_info['address'] = address

        city = self.get_random_string()
        user_info['city'] = city

        zipcode = self.random_number(length=5)
        user_info['zipcode'] = zipcode

        mobile_no = self.random_phone_number()
        user_info['mobile_no'] = mobile_no

        address_alias = self.get_random_string_start_with_uppercase()
        user_info['address_alias'] = address_alias

        user_info['birthDate'] = '1978-01-01'

        return user_info

    @staticmethod
    def get_random_string():
        random_string = ''.join(random.choice(ascii_lowercase_letters) for _ in range(7))
        return 'auto_' + random_string

    @staticmethod
    def get_random_string_in_uppercase():
        random_string = ''.join(random.choice(ascii_uppercase_letters) for _ in range(7))
        return 'AUTO_' + random_string

    @staticmethod
    def get_random_string_start_with_uppercase():
        random_string = ''.join(random.choice(ascii_lowercase_letters) for _ in range(7))
        return 'Auto_' + random_string

    @staticmethod
    def get_random_alpha_numeric_value():
        random_string = ''.join(
            random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
        return random_string

    @staticmethod
    def get_random_join_numeric_value():
        random_string = ''.join(random.choice(ascii_lowercase_letters) for _ in range(7))
        random_string = random_string + '_'
        random_string = random_string + ''.join(random.choice(digits) for _ in range(10))
        return random_string

    @staticmethod
    def random_number(length=5):
        random_no = ''.join(random.choice(digits) for _ in range(length))
        return random_no

    @staticmethod
    def random_phone_number(length=10):
        random_no = ''.join(random.choice(phone_digits) for _ in range(length))
        return random_no

    @staticmethod
    def random_email(username):
        return username + "@" + random.choice(domains)

    @staticmethod
    def generate_password():
        password = ''

        required_string_length = 5
        password = password + ''.join(
            random.choice(ascii_lowercase_letters) for _ in range(required_string_length)) \
                   + ''.join(random.choice(ascii_uppercase_letters) for _ in range(1)) \
                   + ''.join(random.choice(digits) for _ in range(1)) + '!'
        return password


print(UserDataBean().get_random_user_data())
