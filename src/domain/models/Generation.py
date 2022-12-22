

class Generation:

    def __init__(self, name, start_production_year, end_production_year=None):
        self.name = name
        self.start_production_year = start_production_year
        self.end_production_year = end_production_year

    def to_json(self):
        return {
            "name": self.name,
            "startProductionYear": self.start_production_year,
            "endProductionYear": self.end_production_year
        }
