# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
class Vehicle:

    pass  # parent class


class GroundVehicle(Vehicle):

    pass  # child of Vehicle


class Car(GroundVehicle):

    pass  # child of GroundVehicle, Grandchild of Vehicle


class Motorcycle(GroundVehicle):

    pass  # child of GroundVehicle, Grandchild of Vehicle


class FlightVehicle(Vehicle):

    pass  # child of Vehicle


class Airplane(FlightVehicle):

    pass  # child of FLightVehicle, Grandchild of Vhicle


class Starship(FlightVehicle):

    pass  # child of FLightVehicle, Grandchild of Vhicle

