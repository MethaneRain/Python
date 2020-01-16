Documenting Python
---

## Classes

Since the majority of my Python experience has been to gain working knowledge, mostly for plotting and data analysis, I have often overlooked the use of classes. I aim to change that and take a step towards becoming a true Python developer, and understanding classes has to be a major point along that journey.

Classes in Python are fairly basic and similar to classes in other languages. I have to admit when I first started learning classes it got a bit overwhelming. Since I really used Python as a data and science language for working with atmospheric science and mostly in Jupyter notebooks, I brute forced everything. I'm hoping to reconsider some projects in the eyes of classes.

One description of classes that helped me move beyond the abstract terminology was to consider classes like a questionnaire. The questionnaire (class) defines needed info and is just an idea until someone fills out the form. After filling out the form, an idea has become a thing. In Python terms, the class has been instantiated and the user's filled form is an instance of the class with actual information relevant to the user.

Classes are used to create user defined data structures that contain information.

---

## Objects (Instances)

* https://docs.python.org/dev/reference/datamodel.html
> Objects are Python’s abstraction for data. All data in a Python program is represented by objects or by relations between objects. (In a sense, and in conformance to Von Neumann’s model of a “stored program computer,” code is also represented by objects.)

> Every object has an identity, a type and a value.

So really, everything in Python is an object!

Objects are copies of the blueprint class, just with actual values. This means an idea (class) turns into a thing (object).

---

## Attributes

All <em>classes</em> create <em>objects</em> and all objects therefore contain characteristics known as <em>attributes</em>.

There are two types of attributes in Python:

  - Class Attributes
  - Instance Attributes

### Class Attributes

Class attributes are characteristics which are owned by the class on a universal level. These attributes will be shared by all instances of the class, therefore, they will have the same value for every instance. These attributes are defined outside of all methods in the class.

Let's take a quick look at the ```Meteorologist``` class:

~~~Python
class Meteorologist:
    education = "Atmospheric Science"

    def __init__(self,name,age,employer):
        self.name = name
        self.age = age
        self.employer = employer
~~~

Here, the class attribute ```education``` will always have the value of "Atmospheric Science" for every instance of ```Meteorologist```

### Instance Attributes

Instance attributes are characteristics that are owned by the unique instances of a class. Therefore, for different instances of a class will have different attributes.

In the ```Meteorologist``` class, each instance will have a distinct ```name```, ```age```, and ```employer``` attribute.

---

Let's create a new ```class``` called ```Meteorologist```

~~~Python
class Meteorologist:
  def __init__(self, name, age):
    self.name = names
    self.age = age
~~~
