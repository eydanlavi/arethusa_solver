from enum import Enum

class MachineType(Enum):
    PINT_PACKER = "pint_packer"
    FREEZER = "freezer"
    MIXER = "mixer"

class MaintenanceUnit(Enum):
    DAYS = "days"
    PINTS = "pints"
    HOURS = "hours"

class Machine:
    def __init__(self, machine_id: int, machine_type: MachineType, maintenance_duration: float, maintenance_unit: MaintenanceUnit):
        self.machine_id = machine_id
        self.machine_type = machine_type
        self.maintenance_duration = maintenance_duration
        self.maintenance_unit = maintenance_unit
    
    def get_maintenance_duration(self):
        return self.maintenance_duration + " " + self.maintenance_unit
    
    def __repr__(self):
        return (
            f"<Machine id={self.machine_id}, "
            f"type={self.machine_type.value}, "
            f"maintenance={self.maintenance_duration} {self.maintenance_unit.value}>"
        )