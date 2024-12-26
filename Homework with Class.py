##                                                  HOMEWORK
#                                                   BankUser


class BankUser:
    def __init__(self, name, surname, age, account_number, money_count, password):
          if name.isalpha and surname.isalpha:
              print(True)
          elif age > 0:
              print(True)
          elif len(account_number) == 16:
              print(True)
          elif input(account_number) == 'xxxx xxxx xxxx xxxx':
              print(True)
          elif money_count > 0:
              print(True)
          elif input(len(password)) == 8:
              print(True)
          else:
              print(False)
          self.__name = name
          self.__surname = surname
          self.__age = age
          self.account_number = account_number
          self.money_count = money_count
          self.password = password


    def nsa(self):
        return self.__name, self.__surname, self.__age

    def am(self):
        if len(self.password) == 8:
            return self.account_number and self.money_count

    def sum_money(self, money):
        self.money_count += money
        print(f'{self.money_count} = {money}')

    def withdraw_money(self, money):
        self.money_count -= money
        if self.money_count == 0:
            return False
        print(f'{self.money_count} = {money}')
