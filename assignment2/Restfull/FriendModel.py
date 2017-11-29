class FriendModel:
    id = None
    first_name  = None
    last_name  = None
    email  = None
    gender  = None
    country = None

    def __init__ (self, input_id, input_firstname, input_lastname, input_email, input_gender, input_country):
        self.id = input_id
        self.first_name = input_firstname
        self.last_name = input_lastname
        self.email = input_email
        self.gender = input_gender
        self.country = input_country


