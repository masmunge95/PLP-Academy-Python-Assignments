# Football Players Polymorphism ⚽

## 📌 Overview
This project demonstrates **Object-Oriented Programming (OOP)** concepts in Python, focusing on:

- **Classes & Objects**
- **Constructors (`__init__`)**
- **Inheritance**
- **Polymorphism**

We model a simple football team with four player roles:  
- GoalKeeper  
- Defender  
- Midfielder  
- Striker  

Each role is a subclass of the base class `Players` and **overrides** the `perform_action()` method to show polymorphism.

---

## 🏗️ Classes & Structure

### 1. `Players` (Parent Class)
- Attributes: `name`, `team`  
- Method: `perform_action()` → generic placeholder (`"... is doing something..."`)

### 2. `GoalKeeper` (Child Class)
- Inherits from `Players`
- Overrides `perform_action()` → `"saves the penalty!"`

### 3. `Defender` (Child Class)
- Inherits from `Players`
- Overrides `perform_action()` → `"makes a super tackle!"`

### 4. `Midfielder` (Child Class)
- Inherits from `Players`
- Overrides `perform_action()` → `"is controlling the midfield!"`

### 5. `Striker` (Child Class)
- Inherits from `Players`
- Overrides `perform_action()` → `"scores a goal!"`

---

## 📊 UML Class Diagram

```
               ┌──────────────────────────┐
               │         Players           │
               ├──────────────────────────┤
               │ - name                    │
               │ - team                    │
               ├──────────────────────────┤
               │ + __init__(...)           │
               │ + perform_action()        │
               │   (generic placeholder)   │
               └────────────┬──────────────┘
                            │
   ┌─────────────┬──────────┼───────────┬──────────────┐
   │             │          │           │              │
┌───────────┐ ┌──────────┐ ┌───────────┐ ┌────────────┐
│ GoalKeeper│ │ Defender │ │ Midfielder│ │  Striker   │
├───────────┤ ├──────────┤ ├───────────┤ ├────────────┤
│           │ │          │ │           │ │            │
├───────────┤ ├──────────┤ ├───────────┤ ├────────────┤
│+perform_  │ │+perform_ │ │+perform_  │ │+perform_   │
│ action()  │ │ action() │ │ action()  │ │ action()   │
│ (saves)   │ │ (tackle) │ │ (midfield)│ │ (scores)   │
└───────────┘ └──────────┘ └───────────┘ └────────────┘
```

---

## 🎭 Polymorphism in Action
All four subclasses share the same method name (`perform_action`), but the **behavior changes depending on the object**:

**Example Output:**
```
Odhiambo from Tusker FC saves the penalty!
Kibwage from AFC Leopards makes a super tackle!
Onyango from Gor Mahia is controlling the midfield!
Omondi from Harambee Stars scores a goal!
```

---

## ▶️ How to Run
1. Make sure you have **Python 3** installed.  
2. Save the code into a file, e.g. `football_players.py`.  
3. Open a terminal/command prompt and run:
   ```bash
   python football_players.py
   ```

---

## 📖 What This Project Demonstrates
- **Inheritance:** Child classes (`GoalKeeper`, `Defender`, `Midfielder`, `Striker`) extend the base class `Players`.  
- **Constructors:** Each player is initialized with their name and team using `__init__`.  
- **Polymorphism:** Same method `perform_action()` behaves differently in each subclass.  

This satisfies both **Assignment 1 (Design Your Own Class)** and **Activity 2 (Polymorphism Challenge)**.

---
