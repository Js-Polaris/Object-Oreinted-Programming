class HostelInputError(Exception):
  pass
class HostelNotFoundError():
  pass
class StudentNotFoundError():
  pass
class RoomTakenError():
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
      rooms = int(input("How many rooms are availabe in your hostel: ")) 
    except ValueError:
      print("Enter a proper name")
    hostel = {"id": f"H{self.next_id:}", "name": name, "rooms_available": rooms }
    self.hostels.append(hostel)
    self.next_id +=1
    print("\n {name} hostel has been added!")
  def find_hostel(self):
    hostel_id = int(input("Enter the hostel_id Youre looking for here: "))
    for h in self.hostels:
      if h[hostel_id] == hostel_id:
        print(f"{h["id"]} | "
              f"{h["name"]} |"
              f"{h["location"]} |"
              f"Rooms: {len(h["rooms"])}")
  def hostel_is_full(self, hostel):
    for room in hostel["rooms"]:
        if room.available_spaces() > 0:
            return False
    return "hostel is fully occupied"

  def add_student(self, student):
    for existing_student in self.students:
      if existing_student.student_id == student.student_id:
        print("Student Already Exists")
        return True
      self.students.append(student)
      print(f"{student.name} has been added successfully!")
      return True
  
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




  
      
        
