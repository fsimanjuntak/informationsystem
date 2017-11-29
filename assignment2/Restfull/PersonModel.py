class PersonModel:
    id = None
    first_name  = None
    last_name  = None
    email  = None
    gender  = None
    country = None
    friends_list = []

    def __init__ (self, input_id, input_firstname, input_lastname, input_email, input_gender, input_country, input_friends):
        self.id = input_id
        self.first_name = input_firstname
        self.last_name = input_lastname
        self.email = input_email
        self.gender = input_gender
        self.country = input_country
        self.friends_list = input_friends


    def setFriendList(self, input_personmodel):
        self.friends_list.append(input_personmodel)

    def getFriendList(self):
        return self.friends_list


