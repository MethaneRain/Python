Crash course into classes, methods, and attributes 
---

## Classes

Since the majority of my Python experience has been to gain working knowledge, mostly for plotting and data analysis, I have often overlooked the use of classes. I aim to change that and take a step towards becoming a true Python developer, and understanding classes has to be a major point along that journey.

Classes in Python are fairly basic and similar to classes in other languages. I have to admit when I first started learning classes it got a bit overwhelming. Since I really used Python as a data and science language for working with atmospheric science and mostly in Jupyter notebooks, I brute forced everything. I'm hoping to reconsider some projects in the eyes of classes.

One description of classes that helped me move beyond the abstract terminology was to consider classes like a questionnaire. The questionnaire (class) defines needed info and is just an idea until someone fills out the form. After filling out the form, an idea has become a thing. In Python terms, the class has been instantiated and the user's filled form is an instance of the class with actual information relevant to the user.

Classes are used to create user defined data structures that contain information.

Let's create a new ```class``` called ```Meteorologist```

~~~Python
class Meteorologist:
    education = "Atmospheric Science"

    def __init__(self,name,age,employer):
        self.name = name
        self.age = age
        self.employer = employer

    def description(self):
        return f"Hi, my name is {self.name} and I'm {self.age} years old and work for {self.employer}!"
~~~



---

## Objects (Instances)

* https://docs.python.org/dev/reference/datamodel.html
> Objects are Python’s abstraction for data. All data in a Python program is represented by objects or by relations between objects. (In a sense, and in conformance to Von Neumann’s model of a “stored program computer,” code is also represented by objects.)

> Every object has an identity, a type and a value.

So really, everything in Python is an object!

Objects are copies of the blueprint class, just with actual values. This means an idea (class) turns into a thing (object).

---

## Methods



---

## Attributes

All <em>classes</em> create <em>objects</em> and all objects therefore contain characteristics known as <em>attributes</em>.

There are two types of attributes in Python:

  - Class Attributes
  - Instance Attributes

### Class Attributes

Class attributes are characteristics which are owned by the class on a universal level. These attributes will be shared by all instances of the class, therefore, they will have the same value for every instance. These attributes are defined outside of all methods in the class.

Let's take another quick look at the ```Meteorologist``` class:

~~~Python
class Meteorologist:
    education = "Atmospheric Science"

    def __init__(self,name,age,employer):
        self.name = name
        self.age = age
        self.employer = employer

    def description(self):
        return f"Hi, my name is {self.name} and I'm {self.age} years old and work for {self.employer}!"
~~~

Here, the class attribute ```education``` will always have the value of "Atmospheric Science" for every instance of ```Meteorologist```

### Instance Attributes

Instance attributes are characteristics that are owned by the unique instances of a class. Therefore, for different instances of a class will have different attributes. The instance attributes also come from any instance methods.

In the ```Meteorologist``` class, each instance will have a distinct ```name```, ```age```, and ```employer``` attribute. Also, each attribute that comes from the method ```description``` will be unique to an instance.

### Modifying Attributes

Attributes are mutable in Python and therefore, we can change them with the right syntax.

Let's add to our ```Meteorologist``` class a bit:

~~~Python
class Meteorologist:
    education = "Atmospheric Science"

    def __init__(self,name,age,employer):
        self.name = name
        self.age = age
        self.employer = employer

    def description(self):
        return f"Hi, my name is {self.name} and I'm {self.age} years old and work for {self.employer}!"

    def change_employer(self, new_employer):
        self.employer = new_employer
~~~

Now we've added an instance method ```change_employer``` to update the object's employer.

First, let's instantiate the new object ```fred```:

~~~python
fred = Meteorologist("Fred",42,"UCAR")
print(fred)

>>>
<__main__.Meteorologist at 0x1129116a0>
~~~

Sweet, it successfully instantiated our meteorologist Fred. Now we can grab a description of Fred by calling the instance method ```description```:

~~~Python
fred.description()

>>>
"Hi, my name is Fred and I'm 42 years old and work for UCAR!"
~~~

Great, the instance methods are working correctly too! Let's take it a step further and switch Fred's employer from UCAR to NWS using the other instance method ```change_employer```:

~~~Python
fred.change_employer("NWS")
~~~

And once again check his description:

~~~python
fred.description()

>>>
"Hi, my name is Fred and I'm 42 years old and work for NWS!"
~~~

Wonderful, the ```change_employer``` method allowed us to change the initial ```employer``` attribute!

---
