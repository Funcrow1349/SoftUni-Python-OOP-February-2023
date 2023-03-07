#   Create a class called EmailValidator. Upon initialization it should receive:
#   •	min_length (of the username; example: in "peter@gmail.com" "peter" is the username)
#   •	mails (list of the valid mails; example: "gmail", "abv")
#   •	domains (list of valid domains; example: "com", "net")
#   Create three methods that should not be accessed outside the class:
#   •	is_name_valid(name) - returns whether the name is greater than or equal to the min_length (True/False)
#   •	is_mail_valid(mail) - returns whether the mail is in the possible mails list (True/False)
#   •	is_domain_valid(domain) - returns whether the domain is in the possible domains list (True/False)
#   Create one public method:
#   •	validate(email) - using the three methods returns whether the email is valid (True/False)

from typing import List


class EmailValidator:
    def __init__(self, min_length: int, mails: List[str], domains: List[str]):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name) -> bool:
        return len(name) >= self.min_length

    def __is_mail_valid(self, mail) -> bool:
        return mail in self.mails

    def __is_domain_valid(self, domain) -> bool:
        return domain in self.domains

    def validate(self, email: str) -> bool:
        return all([
            self.__is_name_valid(email.split("@")[0]),
            self.__is_mail_valid(email.split("@")[1].split(".")[0]),
            self.__is_domain_valid(email.split("@")[1].split(".")[1]),
        ])

