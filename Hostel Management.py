class HostelInputError(Exception):
  pass
class HostelNotFoundError(Exception):
  pass
class StudentNotFoundError(Exception):
  pass
class RoomTakenError(Exception):
  pass
class DuplicateStudentError(Exception):
  pass

class Hostel_Management:
  def __init__(self):
    self.hostels =[{"id": H001}", "name": Nsibambi, "rooms_available": []},
     {"id": H002}", "name": Sabiti, "rooms_available": []},
     {"id": H003}", "name": PDR, "rooms_available": []},
     {"id": H004}", "name": TechPark, "rooms_available": []}
     ]
    self.student = []
    self.status = "active"
    self.next_id = 5
    
  def add_hostel(self, name,rooms):
    try:
      name = input("Please Enter the hostel neame here: ")
      if not name:
        raise HostelInputError("name cannot be empty")
      rooms = int(input("How many rooms are availabe in your hostel: ")) 
      if rooms <=0:
        raise HostelInputError("rooms cannot be less than zero")
      hostel = {"id": f"H{self.next_id:}", "name": name, "rooms_available": rooms }
      self.hostels.append(hostel)
      self.next_id +=1
    except ValueError:
      print("enter valid number of rooms")    
    print("\n {name} hostel has been added!")
    
  def find_hostel(self):
    hostel_id = (input("Enter the hostel_id Youre looking for here: "))
    for h in self.hostels:
      if h["id"] == hostel_id:
        return h
      raise HostelNotFoundError(f"hostel with the id {hostel_id} is not here")  
      
  def hostel_is_full(self, hostel):
    for room in hostel["rooms"]:
        if room.available_spaces() > 0:
            return False
    return True

  def add_student(self, student):
    for existing_student in self.students:
      if existing_student.student_id == student.student_id:
        return DuplicateStudentError
      self.students.append(student)
      print(f"{student.name} has been added successfully!")
      return True

  def find_student(self,student_id):
    try:
      student_id = int(input("Enter teh student's ID here: "))
      print(student.name)
    except StudentNotFoundError as s:
      print(f"Error: {s}")
    for student  in self.students:
      if student.student_id == student_id:
        return student
      raise StudentNotFoundError(f"Student with {student_id} is not found")
    

## Room
from abc import ABC, abstractmethod
class room(ABC):
    def __init__(self,room_no,capacity)
        self.room_no = room_no
        self.capacity = 0
        self.student_id=[]
        self.status="available"

@property 
def capacity(self): 
  return self._capacity  
@property
def student_id(self):
  return self._student_id
  ##room operations
def is_full(self):
  return len(self.__student_ids) >= self._capacity 
  
def available_spaces(self):
    return self._capacity - len(self.__student_ids)

def add_student(self, student_id):
  if self.is_full(): 
      return False  
if student_id in self.__student_ids:
    return False
  self.__student_ids.append(student_id) 
  self.update_status()
  return True 
def remove_student(self, student_id):
    if student_id not in self.__student_ids: 
       return False
    self.__student_ids.remove(student_id)
    self.update_status()
    return True    

def update_status(self): 
    if len(self.__student_ids) == 0:
    self.status = "Available"
    elif len(self.__student_ids) < self._capacity:  
        self.status = "Partially Occupied" 
else: 
    self.status = "Full" 
@abstractmethod 
def calculate_fee(self):
    pass 
@abstractmethod 
def get_room_type(self): 
    pass

   ##Display Information 
def display_room(self):
        print(f"Room Number: {self.room_no}")
        print(f"Room Type: {self.get_room_type()}")
        print(f"Capacity: {self.capacity}")
        print(f"Occupants: {len(self.student_ids)}")
        print(f"Available Spaces: {self.available_spaces()}")
        print(f"Status: {self.status}")
        print(f"Fee: UGX {self.calculate_fee():,}")
    
## Room Types

class doubleroom(room):

    def __init__(self, room_no):
        super().__init__(room_no)
        self._capacity = 2

    def calculate_fee(self):
        return 850_000

    def get_room_type(self):
        return "Double Room"


class sharedroom(room):

    def __init__(self, room_no):
        super().__init__(room_no)
        self._capacity = 6

    def calculate_fee(self):
        return 650_000

    def get_room_type(self):
        return "Shared Room"


class singleroom(room):

    def __init__(self, room_no):
        super().__init__(room_no)
        self._capacity = 1

    def calculate_fee(self):
        return 1_500_000

    def get_room_type(self):
        return "Single Room"



  
      
        
