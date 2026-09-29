class HostelInputError(Exception):
  pass
class HostelNotFoundError():
  pass
class StudentNotFoundError():
  pass
class RoomTakenError():
  pass

class Hostel:
  def __init__(self, hostel_name, hostel_status):
    self.hostel_name = hostel_name
    self.hostel_status = hostel_status
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




  
      
        
