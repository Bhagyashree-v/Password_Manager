class BasePasswordManager(object):
    old_passwords = ["Bhagyashree"]
    old_passwords = ["Bhagya0809"]
    old_passwords = ["123B"]
                                                          
    def get_password(self):
        return self.old_passwords[-1]

    def is_correct(self, password):                           
        return self.get_password() == password                 

class PasswordManager(BasePasswordManager):                                                                       

    def set_password(self, new_password):
        if self.get_level() < self.get_level(new_password) and len(new_password) >= 10:
            self.old_passwords.append(new_password)
            print("Password changed Successfully.")
        else:
            print("Password cannot be changed.")
# returns the security level of the current password.
    def get_level(self, password = None):     
        if password == None:
            password = self.get_password()

        if password.isalpha() or password.isnumeric():
            level = 0
        elif password.isalnum():
            level = 1
        else:
            level = 2
        return level


Pass= BasePasswordManager()
new_pass = input("Enter new Password: ")
print(f"New password and current password Same: {Pass.is_correct(new_pass)}")

mange= PasswordManager()
mange.set_password(new_pass)
print(f"password Security level: {mange.get_level()}")