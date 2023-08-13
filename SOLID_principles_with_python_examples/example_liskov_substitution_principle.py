from abc import ABC

class Bird: # type: ignore
    def fly(self):
        print('I can fly')

class Penguin(Bird): # type: ignore
    def fly(self):
        print('I cant fly')
    
"""
Penguin overrides fly() => violates the LSP => Object of a superclass should be able to be replaced with objects of a sublass without affecting the correctness
of the program.
-  Penguin can't fly but out superclass can.
    ** We might get unexpected behavior due to the overriden fly() method

"""


class Bird(ABC):
    def fly(self):
        pass
class FlyingBird(Bird):
    def fly(self):
        print('I can fly')
class NonFlyingBird(Bird):
    def fly(self):
        print("I can't fly")

class Penguin(NonFlyingBird):
    pass

"""
FlyingBird and NonFlyingBird => Bird

Adheres to he LSP because sublcass of Bird can now be substituted without altering the correctness of the program.

"""
