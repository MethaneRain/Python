Documenting Python classes
---

Since the majority of my Python experience has been to gain working knowledge, mostly for plotting and data analysis, I have often overlooked the use of classes. I aim to change that and take a step towards becoming a true Python developer, and understanding classes has to be a major point along that journey.

---

Classes in Python are fairly basic and similar to classes in other languages. I have to admit when I first started learning classes it got a bit overwhelming. Since I really used Python as a data and science language for working with atmospheric science and mostly in Jupyter notebooks, I brute forced everything. I'm hoping to reconsider some projects in the eyes of classes.

One description of classes that helped me move beyond the abstract terminology was to consider classes like a questionnaire. The questionnaire (class) defines needed info and is just an idea until someone fills out the form. After filling out the form, an idea has become a thing. In Python terms, the class has been instantiated and the user's filled form is an instance of the class with actual information relevant to the user.

Classes are used to create user defined data structures that contain information.

---

## Objects

* https://docs.python.org/dev/reference/datamodel.html
> Objects are Python’s abstraction for data. All data in a Python program is represented by objects or by relations between objects. (In a sense, and in conformance to Von Neumann’s model of a “stored program computer,” code is also represented by objects.)

> Every object has an identity, a type and a value.

So really, everything in Python is an object!

Objects are copies of the blueprint class, just with actual values. This means an idea (class) turns into a thing (object).

---

## Attributes

All <em>classes</em> create <em>objects</em> and all objects therefore contain characteristics known as <em>attributes</em>.

---

Let's create a new ```class``` called ```Meteorologist```

~~~Python
class Meteorologist:
  def __init__(self, name, age):
    self.name = names
    self.age = age
~~~
