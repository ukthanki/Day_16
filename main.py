# Class acts as a blueprint to make Objects
# Naming Convention for Class is Pascal Case
# Objects have attributes (what it has) and methods (what it does)
# Object.Attribute, Object.Method()

# import turtle
# from turtle import Turtle, Screen
# import another_module
# print(another_module.another_variable)
#
# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("DarkOrchid2")
# timmy.forward(100)
# print(my_screen.canvheight)
# my_screen.exitonclick()
#
# print(timmy)
# Added external library
from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])
table.add_column("Pokemon Name", ["Charizard","",""])
table.align = "r"


print(table)


