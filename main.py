from machine import *

m1 = Machine(1,MachineType.PINT_PACKER, 5, MaintenanceUnit.PINTS)

machines_by_id = {}

def add_machine(machine):
    machines_by_id[machine.machine_id] = machine

print(m1.get_maintenance_duration)