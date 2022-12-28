#instance methods
#class methods
#static methods

#instance method

class Car:
    somerealvar="real"
    def sample_car_instance_method(self,a):
        print(a)
        print(self.somerealvar)

carObj=Car()
carObj.sample_car_instance_method("hello again")

carObj2=Car()
carObj2.sample_car_instance_method(2)

class CarSample:
    dummyvar1="dummyvar1"
    dummyvar2="dummyvar2"
    def __init__(self,name,model):
        self.name=name
        self.model=model
    def displayCarDetails(self):
        print(self.name)
        print(self.model)

carObj=CarSample("Audi","A5")
carObj.displayCarDetails()

#static method

class StaticClass:
    @staticmethod
    def sample_static_method_addition(a,b):
        print(a+b)
    @staticmethod
    def sample_static_method_multiplication(a,b):
        print(a*b)
staticObj=StaticClass()
out_add=staticObj.sample_static_method_addition(4,3)
out_mul=staticObj.sample_static_method_multiplication(4,3)
print(out_add,out_mul)
StaticClass.sample_static_method_addition(4,3)

#Class Method
class ClassMethodExample:
    classVar1="False"
    classVar2="ON"
    @classmethod
    def sample_class_method(cls):
        cls.classvar1="True"
        cls.classvar2="OFF"
ClassMethodExample.sample_class_method()
print(ClassMethodExample.classvar1)
print(ClassMethodExample.classvar2)

######################################################################################

#__init()__=constructor
class animal:
    def __init__(self,species,gender):
        self.species=species
        self.gender=gender
animalObj=animal('Dog','Male')
print(animalObj.gender)
print(animalObj.species)

#example2
class my_class:
    realvar="class"
    def instance_method_example(self,a):
        print(a)
        print(self.realvar)
myclassObj=my_class()
myclassObj.instance_method_example("Hola!")

#instanceclass example
class my_instance_class:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sample_instance_class(self):
        print(self.a,self.b)
obj=my_instance_class ("vasu","abhi")
obj.sample_instance_class()

#classMethods
class ClassMethod:
    @classmethod
    def class_method(cls):
        print("this is called class method")
obj=ClassMethod()
obj.class_method()

#instance methods---handle instance objects
#static methods---utility classes

#problem:=

class start_engine:
    def __init__(self,color,max_speed,acceleration,tyre_friction,start_engine,current_speed):
        self.color=color
        self.max_speed=max_speed
        self.acceleration=acceleration
        self.tyre_friction=tyre_friction
        self.start_engine=start_engine
        self.current_speed=current_speed
    def is_engine_started(self):
        self.start_engine=True
        print("Engine started")
    def is_engine_stopped(self):
        self.is_stop_engine=False
        print("engine stopped")
    def apply_breaks(self,tyre_friction):
        self.tyre_friction=tyre_friction
        self.current_speed-=self.tyre_friction
        if not start_engine:
            print("car is not started")
        elif self.current_speed > self.max_speed:
            self.current_speed = self.max_speed:
            print("apply break and stop")
    def sound_horn(self):
        if self.start_engine:
            print("beep beep")
        else:
            print("engine stopped")
        


















































































