#!/usr/bin/env python3
# *-* coding:utf-8 *-*

from skribi.type_model import *

# ============================= #
# Variables and types in Skribi #
# ============================= #

class Variable:
    """
    A variable is a value with a type. It hasn't any name
    """

    def __init__(self, value, base_type):
        self.value = value
        self.type = base_type

    # String Representation
    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self.value) + " " + str(self.type)


# ============================= #
# Types in Skribi               #
# ============================= #

# Primitive types

class NumberType(PrimitiveType):
    """
    A number type is a type that can be used to store a number.
    """

    def __init__(self, scope, name="aritmi"):
        super().__init__(name, scope)
        
    # String Representation
    def __str__(self):
        return str(self.__dict__)
    
    def __repr__(self):
        return str(self.__dict__)


class StringType(PrimitiveType):
    """
    A string type is a type that can be used to store a string.
    """

    def __init__(self, scope):
        super().__init__("cartais", scope)
        
    # String Representation
    def __str__(self):
        return str(self.__dict__)
    
    def __repr__(self):
        return str(self.__dict__)


class IntType(NumberType):
    """
    A int type is a type that can be used to store an integer.
    """

    def __init__(self, scope):
        super().__init__(scope, "integi")
        
    # String Representation
    def __str__(self):
        return str(self.__dict__)
    
    def __repr__(self):
        return str(self.__dict__)





