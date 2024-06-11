class Club:
    init_cid = 0
    def __init__(self, name, tel, weight, height, balance=5000, is_trial=False):
        self.name = name
        self.tel = tel
        self.__balance = balance
        self.weight = weight
        self.height = height
        self.clubID = None
        self.is_trial = is_trial
        self.is_member = False

        if not is_trial and balance < 5000:
            print("Insufficient balance to join the club. Minimum 5000 is required.")
            self.clubID = "error"
            return

        if self.clubID is not None:
            raise ValueError("ERROR: clubID should not be set during initialization.")

    def tel_check(self):
        if self.clubID is None:
            if str(self.tel)[:2] == "09" and len(str(self.tel)) == 10:
                Club.init_cid += 1
                self.clubID = 'AB' + str(Club.init_cid).zfill(5)
                if not self.is_trial and self.__balance >= 5000:
                    self.is_member = True  # 通过初始审核成为会员
                print(f"{self.name}'s ID is {self.clubID} with balance: {self.__balance}")
            else:
                self.clubID = "error"
                print("Wrong Mobile Phone Number!")
        else:
            return

    def __str__(self):
        if self.clubID == "error":
            return 'not available'
        else:
            return f'ID:{self.clubID} Name:{self.name} Balance={self.__balance}'

    def bmi(self):
        if self.clubID == "error":
            print('not available')
        else:
            bmi = round(self.weight / self.height**2 * 100 * 100, 1)
            print(bmi)

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        print('ERROR: The balance amount cannot be changed directly')

    def deposit(self, amount):
        if amount <= 0:
            print('ERROR: The deposit amount <= 0')
        else:
            self.__balance += amount

    def withdraw(self, n):
        if n < 1 or n > 10:
            print("ERROR: Incorrect number of people")
            return
        if n * 500 > self.__balance:
            print('ERROR: Insufficient balance')
        else:
            self.__balance -= 500 * n

    def purchase_coaching(self, level="basic"):
        if self.is_trial:
            print("ERROR: Trial members are not eligible for coaching sessions.")
        elif level == 'advanced':
            print("ERROR: Access denied. You do not qualify to purchase this product.")
        elif self.__balance < 1000:
            print('ERROR: Insufficient balance')
        else:
            self.__balance -= 1000

    def purchase_inbody(self):
        print("Platinum's purchase_inbody called")
        if self.is_trial:
            print("ERROR: Trial members cannot participate in Inbody measurement.")
        elif self.__balance >= 300:
            self.__balance -= 300
        else:
            print("ERROR: Insufficient balance")

    @classmethod
    def create_trial_member(cls, name, tel, weight, height):
        return cls(name, tel, weight, height, balance=0, is_trial=True)

    def upgrade_to_level(self, coach=None):
        if self.balance < 10000:
            print("ERROR: Cannot upgrade to Gold,because minimum 10000 is required.Current status is not eligible.")
            return None
        return Gold(self.name, self.tel, self.weight, self.height, self.__balance, coach, is_member=self.is_member)

    def purchase_super_coach(self):
        print("ERROR: Access denied. You do not qualify to purchase this product.")


class Gold(Club):
    init_cid = 0
    def __init__(self, name, tel, weight, height, balance=10000, coach=None, is_member=False):
        super().__init__(name, tel, weight, height, balance)
        self.coach = coach
        self.goldID = None
        self.is_trial = False  # 初始化 is_trial 属性为 False
        self.is_member = is_member  # 继承 Club 类的会员状态

        if not self.is_member and balance < 10000:
            print("Insufficient balance to join the club. Minimum 10000 is required.")
            self.goldID = "error"
            return
        self.is_member = True  # 通过初始审核成为会员

        if self.goldID is not None:
            raise ValueError("ERROR: goldID should not be set during initialization.")

    def tel_check(self):
        if self.goldID is None:
            if str(self.tel)[0:2] == "09" and len(str(self.tel)) == 10:
                self.goldID = 'AG' + str(Gold.init_cid).zfill(3) + '68'
                Gold.init_cid += 1
                print(f"{self.name}'s ID is {self.goldID} with balance: {self.balance}")
            else:
                self.goldID = "error"
                print("Wrong Mobile Phone Number!")
        else:
            return

    def __str__(self):
        if self.goldID == "error":
            return 'not available'
        else:
            return f'ID: {self.goldID}, Name: {self.name}, Balance: {self.balance}, Coach: {self.coach}'

    def bmi(self):
        if self.goldID == "error":
            print('not available')
        else:
            bmi = round(self.weight / self.height**2 * 100 * 100, 1)
            print(bmi)

    def modify_balance(self, value):
        if value >= 0:
            self._Club__balance = value
        else:
            print("ERROR: Balance cannot be negative")

    def deposit(self, amount=1000):
        if amount < 1000:
            print('ERROR: The deposit amount < 1000')
        else:
            self.modify_balance(self.balance + amount)

    def withdraw(self, n=1):
        if n < 1 or n > 3:
            print('ERROR: Incorrect number of people')
            return
        if self.balance - 400 * n < 0:
            print('ERROR: Insufficient balance')
        else:
            self.modify_balance(self.balance - 400 * n)

    def purchase_coaching(self, level="basic"):
        cost = 1000 if level == "basic" else 2000 if level == "advanced" else 0
        if self.balance >= cost:
            self.modify_balance(self.balance - cost)
        else:
            print("ERROR: Insufficient balance")

    def purchase_inbody(self):
        if self.balance >= 240:
            self.modify_balance(self.balance - 240)
        else:
            print("ERROR: Insufficient balance")
    def upgrade_to_level(self, coach=None):
        if self.balance < 15000:
            print("ERROR: Cannot upgrade to Platinum,because minimum 15000 is required.Current status is not eligible.")
            return None
        return Platinum(self.name, self.tel, self.weight, self.height, self.balance, coach, is_member=self.is_member)

    def purchase_super_coach(self):
        print("ERROR: Access denied. You do not qualify to purchase this product.")

#白金會員區
class Platinum(Gold):
    init_cid = 0
    def __init__(self, name, tel, weight, height, balance=15000, coach=None, is_member=False):
        super().__init__(name, tel, weight, height, balance, coach, is_member)
        self.platinumID = None
        self.is_trial = False
        self.is_member = is_member

        if not self.is_member and balance < 15000:
            print("Insufficient balance to join the club. Minimum 15000 is required.")
            self.platinumID = "error"
            return
        self.is_member = True

        if self.platinumID is not None:
            raise ValueError("ERROR: platinumID should not be set during initialization.")

        print('I Love Health Gym !!')

    def tel_check(self):
        if self.platinumID is None:
            if str(self.tel)[0:2] == "09" and len(str(self.tel)) == 10:
                self.platinumID = 'AP' + str(Platinum.init_cid).zfill(3) + '78'
                Platinum.init_cid += 1
                print(f"{self.name}'s ID is {self.platinumID} with balance: {self.balance}")
            else:
                self.platinumID = "error"
                print("Wrong Mobile Phone Number!")
        else:
            return

    def __str__(self):
        if self.platinumID == "error":
            return 'not available'
        else:
            return f'ID: {self.platinumID}, Name: {self.name}, Balance: {self.balance}, Coach: {self.coach}'

    def deposit(self, amount):
        if amount < 3000:
            print('ERROR: The deposit amount <= 3000')
        else:
            self.modify_balance(self.balance + amount)

    def withdraw(self, n):
        if n < 1 or n > 3:
            print('ERROR: Incorrect number of people')
            return
        if self.balance < 400 * n:
            print('ERROR: Insufficient balance')
        else:
            self.modify_balance(self.balance - 400 * n)

    def purchase_inbody(self):
        cost = round(240 * 0.7)
        if self.balance >= 240:
            self.modify_balance(self.balance - cost)
        else:
            print("ERROR: Insufficient balance")

    def purchase_super_coach(self):
        if not isinstance(self, Platinum):
            print("ERROR: Access denied. You do not qualify to purchase this product.")
            return
        if self.balance >= 4000:
            self.modify_balance(self.balance - 4000)
        else:
            print("ERROR: Insufficient balance")

#---------------------------------------------------------
#第二題開始：
#---------------------------------------------------------
#第二題開始：
class HotelMember:
    init_cid = 0  # Assuming this is needed for ID generation

    def __init__(self, name, tel, balance=6000, weight=0, height=0, is_member=False):
        self.name = name
        self.tel = tel
        self.__balance = balance
        self.weight = weight
        self.height = height
        self.memberID = None
        self.is_member = is_member  # 初始化 is_member 属性

        if not self.is_member and balance < 6000:
            print("Insufficient balance to join the club. Minimum 6000 is required.")
            self.memberID = "error"
            return

        self.is_member = True  # 通过初始审核成为会员

        if self.memberID is not None:
            raise ValueError("ERROR: memberID should not be set during initialization.")

    def tel_check(self):
        if self.memberID is None:
            if str(self.tel)[:2] == "09" and len(str(self.tel)) == 10:
                self.memberID = 'HM' + str(HotelMember.init_cid).zfill(5)
                HotelMember.init_cid += 1
                print(f"{self.name}'s ID is {self.memberID} with balance: {self.__balance}")
            else:
                self.memberID = "error"
                print("Wrong Mobile Phone Number!")
        else:
            return

    def __str__(self):
        if self.memberID == "error":
            return 'not available'
        else:
            return f'ID:{self.memberID} Name:{self.name} Balance={self.__balance}'

    def deposit(self, amount):
        if amount <= 0:
            print('ERROR: The deposit amount <= 0')
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print('ERROR: Insufficient balance')
        else:
            self.__balance -= amount

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        print('ERROR: The balance amount cannot be changed directly')

    def upgrade_to_level(self, weight, height):
        return HotelPrivilegesMember(self.name, self.tel, self.__balance, weight, height, is_member=True)

class HotelPrivilegesMember(HotelMember):
    init_cid = 0

    def __init__(self, name, tel, balance=12000, weight=0, height=0, is_member=False):
        super().__init__(name, tel, balance, weight, height, is_member)
        self.hpmID = None

        if not self.is_member and balance < 12000:
            print("Insufficient balance to join the club. Minimum 12000 is required.")
            self.hpmID = "error"
            return

        self.is_member = True  # 通过初始审核成为会员

        if self.hpmID is not None:
            raise ValueError("ERROR: hpmID should not be set during initialization.")
        print('I Love Caesar Hotel !!')
    
    def tel_check(self):
        if self.hpmID is None:
            if str(self.tel)[:2] == "09" and len(str(self.tel)) == 10:
                self.hpmID = 'CaesarP' + str(HotelPrivilegesMember.init_cid).zfill(3) + '777'
                HotelPrivilegesMember.init_cid += 1
                print(f"{self.name}'s ID is {self.hpmID} with balance: {self.balance}")
            else:
                self.hpmID = "error"
                print("Wrong Mobile Phone Number!")
        else:
            return

    def __str__(self):
        if self.hpmID == "error":
            return 'not available'
        else:
            return f'ID:{self.hpmID} Name:{self.name} Balance={self.balance}'

    def reserve_room(self):
        cost = 3000
        if self.balance >= cost:
            self.withdraw(cost)
            print(f"Room reserved. Your new balance is {self.balance}.")
        else:
            print("ERROR: Your balance is insufficient to complete this transaction.")

    def book_spa(self):
        cost = 2000
        if self.balance >= cost:
            self.withdraw(cost)
            print(f"SPA booked. Your new balance is {self.balance}.")
        else:
            print("ERROR: Your balance is insufficient to complete this transaction.")

    def purchase_super_coach(self):
        cost = 3000
        if self.balance >= cost:
            self.withdraw(cost)
            print("Super coaching session booked.")
        else:
            print("ERROR: Your balance is insufficient to complete this transaction.")

    def modify_balance(self, value):
        if value >= 0:
            self._HotelMember__balance = value
        else:
            print("ERROR: Balance cannot be negative")

    def deposit(self, amount):
        if amount <= 0:
            print('ERROR: The deposit amount <= 0')
        else:
            self.modify_balance(self.balance + amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print('ERROR: Insufficient balance')
        else:
            self.modify_balance(self.balance - amount)

    def upgrade_to_level(self, weight, height, coach=None):
        if self.balance < 30000:
            print("ERROR: Cannot upgrade to Ultimate, because minimum 30000 is required. Current status is not eligible.")
            return None
        return UltimateMember(self.name, self.tel, weight, height, self.balance, Platinum(self.name, self.tel, weight, height).balance, coach, is_member=True)



class UltimateMember(HotelPrivilegesMember, Platinum):
    init_cid = 0

    def __init__(self, name, tel, weight, height, hotel_balance, platinum_balance, coach=None, is_member=False):
        self.hotel_balance = hotel_balance
        self.platinum_balance = platinum_balance
        combined_balance = hotel_balance + platinum_balance

        HotelPrivilegesMember.__init__(self, name, tel, balance=hotel_balance, weight=weight, height=height, is_member=is_member)
        Platinum.__init__(self, name, tel, weight, height, balance=platinum_balance, coach=coach, is_member=is_member)

        self.__balance = combined_balance
        self.ultID = None
        self.is_member = is_member

        if not self.is_member and self.__balance < 30000:
            print("Insufficient balance to join the club. Minimum 30000 is required.")
            self.ultID = "error"
            return
        self.is_member = True  # 通过初始审核成为会员

        if self.ultID is not None:
            raise ValueError("ERROR: ultID should not be set during initialization.")
        print('I Love both Health Gym and Caesar Hotel !!')
    
    def tel_check(self):
        if self.ultID is None:
            if str(self.tel)[:2] == "09" and len(str(self.tel)) == 10:
                self.ultID = 'UM' + str(UltimateMember.init_cid).zfill(3) + '888'
                UltimateMember.init_cid += 1
                print(f"{self.name}'s ID is {self.ultID} with balance: {self.__balance}")
            else:
                self.ultID = "error"
                print("Wrong Mobile Phone Number!")
        else:
            return

    def __str__(self):
        if self.ultID == "error":
            return 'not available'
        else:
            return f'ID:{self.ultID} Name:{self.name} Balance={self.__balance}'

    def ultimate_experience(self):
        if self.ultID == "error":
            print("ERROR: Cannot book services due to initialization failure.")
            return
        cost = 20000
        if self.balance >= cost:
            self.withdraw(cost)
            print("Ultimate experience package booked.")
        else:
            print("ERROR: Insufficient balance to book the ultimate experience package.")

    def purchase_super_coach(self):
        if self.ultID == "error":
            print("ERROR: Cannot book services due to initialization failure.")
            return

        if self.__balance >= 3000:
            self.__balance -= 3000
            print("Super coaching session booked.")
        else:
            print("ERROR: Insufficient balance")

    def ultimate_coach(self):
        if self.ultID == "error":
            print("ERROR: Cannot book services due to initialization failure.")
            return
        cost = 6000
        if self.balance >= cost:
            self.withdraw(cost)
            print("Ultimate coaching session booked.")
        else:
            print("ERROR: Insufficient balance to book the ultimate coaching session.")

    def purchase_inbody(self):
        if self.ultID == "error":
            print("ERROR: Cannot book services due to initialization failure.")
            return
        cost = round(240 * 0.7)
        if self.balance >= cost:
            self.withdraw(cost)
        else:
            print("ERROR: Insufficient balance")

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        print('ERROR: The balance amount cannot be changed directly')

    def deposit(self, amount):
        if self.ultID == "error":
            print("ERROR: Cannot perform transactions due to initialization failure.")
            return
        if amount <= 0:
            print('ERROR: The deposit amount <= 0')
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if self.ultID == "error":
            print("ERROR: Cannot perform transactions due to initialization failure.")
            return
        if amount > self.__balance:
            print('ERROR: Insufficient balance')
        else:
            self.__balance -= amount




def test():
    # -----測試HotelMember會員-----
    # HotelMember1 = HotelMember("John", "987654321", 6000, 70, 170)
    # print(HotelMember1.memberID)
    # HotelMember1.tel_check()
    # print(HotelMember1)  # 錯誤電話測試
    # HotelMember1.tel_check()
    # HotelMember2 = HotelMember("Tom", "0987654321", 7000, 70, 172)
    # print(HotelMember2.memberID)
    # print(HotelMember2)
    # HotelMember2.tel_check()
    # HotelMember2.deposit(1000)
    # print(HotelMember2)
    # HotelMember2.withdraw(4000)
    # HotelMember2.tel_check()
    # print(HotelMember2)
    # HotelPrivilegesMember1 = HotelMember2.upgrade_to_level(70, 170)
    # print(HotelPrivilegesMember1.hpmID)
    # HotelPrivilegesMember1.tel_check()
    # print(HotelPrivilegesMember1)
    # HotelPrivilegesMember1.reserve_room()
    # -----測試HotelPrivilegesMember會員-----
    # HotelPrivilegesMember1 = HotelPrivilegesMember("Mary", "0912345678", 12000, 60, 168)
    # print(HotelPrivilegesMember1)
    # HotelPrivilegesMember1.tel_check()
    # print(HotelPrivilegesMember1)
    # HotelPrivilegesMember1.reserve_room()
    # print(HotelPrivilegesMember1)
    # HotelPrivilegesMember1.book_spa()
    # print(HotelPrivilegesMember1)
    # HotelPrivilegesMember1.super_coach()
    # print(HotelPrivilegesMember1)
    # HotelPrivilegesMember2 = HotelPrivilegesMember("Jack", "0987654321", 13000, 70, 180)
    # print(HotelPrivilegesMember2)
    # HotelPrivilegesMember2.tel_check()
    # print(HotelPrivilegesMember2)
    # HotelPrivilegesMember2.reserve_room()
    # print(HotelPrivilegesMember2)
    # HotelPrivilegesMember2.book_spa()
    # print(HotelPrivilegesMember2)
    # -----測試UltimateMember會員-----
    # HotelPrivilegesMember1 = HotelPrivilegesMember("Sam", "0912345678", 12000, 80, 180)
    # print(HotelPrivilegesMember1)
    # HotelPrivilegesMember1.tel_check()
    # print(HotelPrivilegesMember1)


    # HotelPrivilegesMember2 = HotelPrivilegesMember("Tom", "0987654321", 13000, 80, 180)
    # print(HotelPrivilegesMember2)
    # HotelPrivilegesMember2.tel_check()
    # print(HotelPrivilegesMember2)

    # platinumMember1 = Platinum('Sam', '0912345678', 80, 180, balance=15000)
    # print(platinumMember1)
    # platinumMember1.tel_check()
    # platinumMember1.deposit(15000)
    # print(platinumMember1)

    # platinumMember2 = Platinum('Tom', '0987654321', 80, 180, balance=16000)
    # print(platinumMember2)
    # platinumMember2.tel_check()
    # platinumMember2.deposit(16000)
    # print(platinumMember2)

    # UltimateMember1 = UltimateMember(HotelPrivilegesMember1.name, HotelPrivilegesMember1.tel, HotelPrivilegesMember1.weight, HotelPrivilegesMember1.height, HotelPrivilegesMember1.balance, platinumMember1.balance, coach='John')
    # print(UltimateMember1)
    # UltimateMember1.tel_check()
    # print(UltimateMember1)
    # UltimateMember1.purchase_super_coach()
    # print(UltimateMember1)
    # UltimateMember1.purchase_inbody()
    # print(UltimateMember1)
    # UltimateMember1.ultimate_experience()
    # print(UltimateMember1)
    # UltimateMember1.ultimate_coach()
    # print(UltimateMember1)

    # UltimateMember2 = UltimateMember(HotelPrivilegesMember2.name, HotelPrivilegesMember2.tel, HotelPrivilegesMember2.weight, HotelPrivilegesMember2.height, HotelPrivilegesMember2.balance, platinumMember2.balance, coach='Kom')
    # print(UltimateMember2)
    # UltimateMember2.tel_check()
    # print(UltimateMember2)
    # -----錯誤測試UltimateMember會員-----
    # UltimateMember1 = UltimateMember("Sam", "0912223648", 80, 180, 100000, 20000, coach='John')
    # print(UltimateMember1.ultID)
    # UltimateMember1.tel_check()
    # print(UltimateMember1)
    # UltimateMember1.purchase_super_coach()
    # print(UltimateMember1)
    # UltimateMember1.purchase_inbody()
    # print(UltimateMember1)
    # UltimateMember1.ultimate_experience()
    # print(UltimateMember1)

    # UltimateMember2 = UltimateMember("Ken", "0912235778", 80, 180, 1000, 20000, coach='John')
    # print(UltimateMember2.ultID)
    # UltimateMember2.tel_check()
    # print(UltimateMember2)
    # UltimateMember2.purchase_super_coach()
    # print(UltimateMember2)
    # UltimateMember2.purchase_inbody()
    # print(UltimateMember2)
    # UltimateMember2.ultimate_experience()
    # print(UltimateMember2)
    HotelMember1 = HotelMember("John", "987654321", 6000, 70, 170)
    print(HotelMember1.memberID)
    HotelMember1.tel_check()
    print(HotelMember1)
    HotelMember1.tel_check()
    HotelMember2 = HotelMember("Tom", "0987654321", 7000, 70, 172)
    print(HotelMember2.memberID)
    print(HotelMember2)
    HotelMember2.tel_check()
    HotelMember2.deposit(1000)
    print(HotelMember2)
    HotelMember2.withdraw(4000)
    HotelMember2.tel_check()
    print(HotelMember2)
    HotelPrivilegesMember1 = HotelMember2.upgrade_to_level(70, 170)
    print(HotelPrivilegesMember1.hpmID)
    HotelPrivilegesMember1.tel_check()
    print(HotelPrivilegesMember1)
    HotelPrivilegesMember1.reserve_room()

    
if __name__ == "__main__":
    test()