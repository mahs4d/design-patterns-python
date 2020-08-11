"""
https://sourcemaking.com/design_patterns/factory_method
"""

OLD_PHONE_TYPE = 1
SMART_PHONE_TYPE = 2


class Phone:
    @staticmethod
    def create_phone(phone_type):
        if phone_type == OLD_PHONE_TYPE:
            return OldPhone()
        elif phone_type == SMART_PHONE_TYPE:
            return SmartPhone()
        else:
            raise Exception("bad type")


class OldPhone(Phone):
    def __str__(self):
        return "Old Phone"


class SmartPhone(Phone):
    def __str__(self):
        return "Smart Phone"


# region main

if __name__ == "__main__":
    phone1 = Phone.create_phone(OLD_PHONE_TYPE)
    phone2 = Phone.create_phone(SMART_PHONE_TYPE)

    print(phone1)
    print(phone2)

# endregion
