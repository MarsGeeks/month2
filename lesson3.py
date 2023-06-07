class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        a = self.cpu * self.memory
        return f'cpu -{self.cpu} memory - {self.memory} = {a}'

    def __str__(self):
        return f"Cpu: {self.__cpu} Mermory: {self.__memory}"

    def __gt__(self, other):
        return self.__memory < other.memory

    def __lt__(self, other):
        return self.__memory > other.memory

    def __ne__(self, other):
        return self.__memory != other.memory

    def __ge__(self, other):
        return self.__memory >= other.memory

    def __le__(self, other):
        return self.__memory <= other.memory

    def __eq__(self, other):
        return self.__memory == other.memory

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        print(
            f'Идет звонок на номер +{call_to_number} с сим-карты-{sim_card_number}-{self.__sim_cards_list[sim_card_number]}')
    def __str__(self):
        return f"sim_card_list{self.__sim_cards_list}"
class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self,  location):
        print(f'Маршрут построин до {location} осталось 7,5km')

    def __str__(self):
        return Computer.__str__(self) + Phone.__str__(self)





ASUS = Computer(3200, 516)

print(ASUS)
phone = Phone({
    1: 'Beeline',
    2: 'MegaCom',
    3: 'O'})
phone.call(2, '996 550 50 52 41')
print(phone)
smart_phone = SmartPhone(2400, 128, {1: 'Beeline',
                                     2: 'MegaCom'})
smart_phone.use_gps('Цум')
print(smart_phone)

