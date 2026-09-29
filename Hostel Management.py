print("Hello world")

class Hostel:
  def __init__(self, hostel_name, hostel_status):
    self.hostel_name = hostel_name
    self.hostel_status = hostel_status
## Room
from abc import ABC, abstractmethod
class room(ABC):
    def __init__(self,room_no,capacity)
        self.room_no = room_no
        self.capacity = capacity
        self.student_ids=[]
        self.status="available"
        
