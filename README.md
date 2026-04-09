# 🎓 Student Class in Python (OOP Example)

## 📌 Description

This Python program demonstrates the basic concept of **Object-Oriented Programming (OOP)** using a `Student` class. It shows how to create a class, define a constructor, and use objects to store and display student details.

---

## 🚀 Features

* Defines a `Student` class
* Uses a constructor (`__init__`) to initialize data
* Stores student name and roll number
* Displays student details using a method

---

## 🛠️ How It Works

1. A class named `Student` is created.
2. The constructor (`__init__`) is used to initialize:

   * `name`
   * `Roll_number`
3. A method `display()` is defined to print student details.
4. Two objects (`s1` and `s2`) are created with different values.
5. The `display()` method is called for each object.

---

## 💻 Code

```python
class Student:
    def __init__(self, name, Roll_number): 
        self.name = name
        self.Roll_number = Roll_number

    def display(self):
        print("Name :", self.name)
        print("Roll Number :", self.Roll_number)

s1 = Student("Pranay", 25) 
s2 = Student("Raj", 26) 

s1.display()
s2.display()
```

---

## ▶️ Example Output

```
Name : Pranay
Roll Number : 25
Name : Raj
Roll Number : 26
```

---

## 📚 Concepts Used

* Class and Object
* Constructor (`__init__`)
* Instance variables
* Methods in class

---

## 🎯 Use Case

This program helps beginners understand:

* How to structure data using classes
* How objects work in real-world scenarios (like storing student data)

---

## 🔧 Future Improvements

* Add more attributes (e.g., marks, branch)
* Add methods to calculate grades
* Take input from the user instead of hardcoding values

---

## 📄 License

This project is open-source and free to use.

<img width="551" height="776" alt="image" src="https://github.com/user-attachments/assets/649312fd-ea62-4963-a3f0-2d2fc13a4b67" />
