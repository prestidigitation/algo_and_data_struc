class Computer:

    def __init__(self, manufacturer, processor, ram_size, disk_size):
        self.manufacturer = manufacturer
        self.processor = processor
        self.ram_size = ram_size
        self.disk_size = disk_size

    def get_manufacturer(self):
        return self.manufacturer

    def get_processor(self):
        return self.processor

    def get_ram_size(self):
        return self.ram_size

    def get_disk_size(self):
        return self.disk_size


class Laptop(Computer):

    def __init__(self, manufacturer, processor, ram_size, disk_size, screen_size, weight):
        super().__init__(manufacturer, processor, ram_size, disk_size)
        self.screen_size = screen_size
        self.weight = weight

    def get_screen_size(self):
        return self.screen_size

    def get_weight(self):
        return self.weight


class Server(Computer):

    def __init__(self, manufacturer, processor, ram_size, disk_size):
        super().__init__(manufacturer, processor, ram_size, disk_size)
