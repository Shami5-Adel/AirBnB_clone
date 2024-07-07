#!/usr/bin/python3
"""
An interactive shell for the AirBnB clone project
"""

import cmd
import re
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class_home = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "Amenity": Amenity,
    "City": City,
    "Review": Review,
    "State": State
}


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """Exits console"""
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        """Quit command to exit the program"""
        print("Quit command to exit the program")

    def emptyline(self):
        """Overrides the emptyline method to do nothing"""
        pass

    def do_create(self, line):
        """Creates a new instance of a class"""
        if not line:
            print("** class name missing **")
            return
        if line not in class_home:
            print("** class doesn't exist **")
            return
        new_instance = class_home[line]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in class_home:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        try:
            print(models.storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in class_home:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        try:
            del models.storage.all()[key]
            models.storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances"""
        if not line:
            print([str(obj) for obj in models.storage.all().values()])
        elif line not in class_home:
            print("** class doesn't exist **")
        else:
            print([str(obj) for key, obj in models.storage.all().items()
                   if key.startswith(line)])

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in class_home:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        instance = models.storage.all()[key]
        setattr(instance, args[2], args[3])
        instance.save()

    def do_count(self, line):
        """Counts the number of instances of a class"""
        if line not in class_home:
            print("** class doesn't exist **")
            return
        count = sum(1 for obj in models.storage.all().values()
                    if obj.__class__.__name__ == line)
        print(count)

    def default(self, line):
        """Handles unrecognized commands and specific syntax for commands"""
        if line is None:
            return
        cmd_pattern = "^([A-Za-z]+)\.([a-z]+)\(([^(]*)\)"
        params_pattern = "^\"([^\"]+)\"(?:, (?:\"([^\"]+)\")?)?"
        m = re.match(cmd_pattern, line)
        if not m:
            super().default(line)
            return
        class_name, method, params = m.groups()
        params = params.split(", ") if params else []
        if method == "all":
            return self.do_all(class_name)
        if method == "count":
            return self.do_count(class_name)
        if method == "show":
            if len(params) == 1:
                return self.do_show(f"{class_name} {params[0]}")
        if method == "destroy":
            if len(params) == 1:
                return self.do_destroy(f"{class_name} {params[0]}")
        if method == "update":
            if len(params) == 2:
                return self.do_update(f"{class_name} {params[0]} {params[1]}")
            if len(params) == 3:
                return self.do_update(f"{class_name} {params[0]} {params[1]} {params[2]}")
        print(f"*** Unknown syntax: {line}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()

