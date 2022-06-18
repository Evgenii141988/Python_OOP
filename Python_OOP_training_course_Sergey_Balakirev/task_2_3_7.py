class ValidateString:
    def __init__(self, min_length=3, max_length=100):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, string):
        return isinstance(string, str) and self.min_length <= len(string) <= self.max_length


class StringValue:

    def __init__(self, validate):
        self.validate = validate

    def __set_name__(self, owner, name):
        self.name = f'_{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.validate.validate(value):
            setattr(instance, self.name, value)


class RegisterForm:
    login = StringValue(validate=ValidateString())
    password = StringValue(validate=ValidateString())
    email = StringValue(validate=ValidateString())

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

    def get_fields(self):
        return [self.login, self.password, self.email]

    def show(self):
        print(f'<form>\nЛогин: {self.login}\nПароль: {self.password}\nEmail: {self.email}\n</form>')


if __name__ == '__main__':
    form = RegisterForm("логин", "пароль", "email")
    print(form.get_fields())
    form.show()
