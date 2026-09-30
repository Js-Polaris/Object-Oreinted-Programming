from abc import ABC, abstractmethod


# ============================================================
# CUSTOM EXCEPTIONS
# ============================================================

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


class RoomNotFoundError(Exception):
    pass


class AccommodationError(Exception):
    pass


# ============================================================
# STUDENT CLASS
# My contribution: Student class
# Responsibility: Stores student personal, academic and
# accommodation information.
# Demonstrates: constructor, instance attributes,
# encapsulation, properties, setters and validation.
# ============================================================

class Student:

    def __init__(self, student_id, student_name, gender, course,
                 year, hostel_name=None, room_number=None):
        self.student_id = student_id
        self.student_name = student_name
        self.gender = gender
        self.course = course
        self.year = year
        self.hostel_name = hostel_name
        self.room_number = room_number

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Student ID cannot be empty.")
        self._student_id = value.strip()

    @property
    def student_name(self):
        return self._student_name

    @student_name.setter
    def student_name(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Student name cannot be empty.")
        if not all(c.isalpha() or c.isspace() for c in value):
            raise ValueError("Student name must contain letters and spaces only.")
        self._student_name = value.strip()

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Gender cannot be empty.")
        self._gender = value.strip().title()

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Course cannot be empty.")
        self._course = value.strip()

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Academic year must be a positive number.")
        self._year = value

    def display_details(self):
        print("\n========== STUDENT DETAILS ==========")
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.student_name}")
        print(f"Gender: {self.gender}")
        print(f"Course: {self.course}")
        print(f"Year: {self.year}")

        if self.hostel_name and self.room_number:
            print(f"Hostel: {self.hostel_name}")
            print(f"Room: {self.room_number}")
        else:
            print("Accommodation: Not allocated")


# ============================================================
# ABSTRACT ROOM CLASS
# Demonstrates abstraction, encapsulation and abstract methods.
# ============================================================

class Room(ABC):

    def __init__(self, room_no, capacity):
        if not isinstance(room_no, str) or not room_no.strip():
            raise ValueError("Room number cannot be empty.")
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Room capacity must be positive.")

        self.room_no = room_no.strip()
        self._capacity = capacity
        self.__student_ids = []
        self.status = "Available"

    @property
    def capacity(self):
        return self._capacity

    @property
    def student_ids(self):
        return self.__student_ids.copy()

    def is_full(self):
        return len(self.__student_ids) >= self._capacity

    def available_spaces(self):
        return self._capacity - len(self.__student_ids)

    def add_student(self, student_id):
        if self.is_full():
            raise RoomTakenError(f"Room {self.room_no} is already full.")

        if student_id in self.__student_ids:
            raise RoomTakenError(
                f"Student {student_id} is already in room {self.room_no}."
            )

        self.__student_ids.append(student_id)
        self.update_status()

    def remove_student(self, student_id):
        if student_id not in self.__student_ids:
            raise StudentNotFoundError(
                f"Student {student_id} is not in room {self.room_no}."
            )

        self.__student_ids.remove(student_id)
        self.update_status()

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

    def display_room(self):
        print(f"Room Number: {self.room_no}")
        print(f"Room Type: {self.get_room_type()}")
        print(f"Capacity: {self.capacity}")
        print(f"Occupants: {len(self.student_ids)}")
        print(f"Available Spaces: {self.available_spaces()}")
        print(f"Status: {self.status}")
        print(f"Fee: UGX {self.calculate_fee():,}")


# ============================================================
# ROOM TYPES
# Demonstrates inheritance, method overriding and polymorphism.
# ============================================================

class SingleRoom(Room):

    def __init__(self, room_no):
        super().__init__(room_no, 1)

    def calculate_fee(self):
        return 1_500_000

    def get_room_type(self):
        return "Single Room"


class DoubleRoom(Room):

    def __init__(self, room_no):
        super().__init__(room_no, 2)

    def calculate_fee(self):
        return 850_000

    def get_room_type(self):
        return "Double Room"


class SharedRoom(Room):

    def __init__(self, room_no):
        super().__init__(room_no, 6)

    def calculate_fee(self):
        return 650_000

    def get_room_type(self):
        return "Shared Room"


# ============================================================
# HOSTEL CLASS
# Responsibility: Stores and manages Room objects.
# Relationship: A Hostel contains Room objects.
# ============================================================

class Hostel:

    def __init__(self, hostel_id, name):
        self.hostel_id = hostel_id
        self.name = name
        self._rooms = []

    @property
    def rooms(self):
        return self._rooms.copy()

    def add_room(self, room):
        if not isinstance(room, Room):
            raise TypeError("Only Room objects can be added.")

        for existing_room in self._rooms:
            if existing_room.room_no == room.room_no:
                raise ValueError(
                    f"Room {room.room_no} already exists in {self.name}."
                )

        self._rooms.append(room)

    def find_room(self, room_no):
        for room in self._rooms:
            if room.room_no.lower() == room_no.lower():
                return room

        raise RoomNotFoundError(
            f"Room {room_no} was not found in {self.name}."
        )

    def display_rooms(self):
        print(f"\n========== {self.name.upper()} ==========")

        for room in self._rooms:
            room.display_room()
            print("-" * 40)

    def total_rooms(self):
        return len(self._rooms)

    def occupied_rooms(self):
        return sum(1 for room in self._rooms if room.student_ids)

    def available_spaces(self):
        return sum(room.available_spaces() for room in self._rooms)


# ============================================================
# HOSTEL MANAGEMENT CLASS
# Responsibility: Coordinates students, hostels, rooms and
# hostel operations.
# ============================================================

class Hostel_Management:

    def __init__(self):
        self.hostels = []
        self.students = []
        self.status = "Active"
        self._create_default_hostels()

    def _create_default_hostels(self):

        hostel_data = [
            ("H001", "Nsibambi"),
            ("H002", "Sabiti"),
            ("H003", "PDR"),
            ("H004", "Honors College")
        ]

        for hostel_id, hostel_name in hostel_data:

            hostel = Hostel(hostel_id, hostel_name)

            # 20 Single Rooms
            for number in range(1, 21):
                hostel.add_room(
                    SingleRoom(f"{hostel_id}-S{number:02d}")
                )

            # 50 Double Rooms
            for number in range(1, 51):
                hostel.add_room(
                    DoubleRoom(f"{hostel_id}-D{number:02d}")
                )

            # 20 Shared Rooms
            for number in range(1, 21):
                hostel.add_room(
                    SharedRoom(f"{hostel_id}-SH{number:02d}")
                )

            self.hostels.append(hostel)

    def find_hostel(self, hostel_id):
        for hostel in self.hostels:
            if hostel.hostel_id.lower() == hostel_id.lower():
                return hostel

        raise HostelNotFoundError(
            f"Hostel with ID {hostel_id} was not found."
        )

    def add_hostel(self, name):

        if not isinstance(name, str) or not name.strip():
            raise HostelInputError("Hostel name cannot be empty.")

        hostel_id = f"H{len(self.hostels) + 1:03d}"
        hostel = Hostel(hostel_id, name.strip())
        self.hostels.append(hostel)

        return hostel

    def add_student(self, student):

        if not isinstance(student, Student):
            raise TypeError("Only Student objects can be registered.")

        for existing_student in self.students:
            if existing_student.student_id == student.student_id:
                raise DuplicateStudentError(
                    f"Student ID {student.student_id} already exists."
                )

        self.students.append(student)

    def find_student(self, student_id):

        for student in self.students:
            if student.student_id.lower() == student_id.lower():
                return student

        raise StudentNotFoundError(
            f"Student with ID {student_id} was not found."
        )

    def allocate_student(self, student_id, hostel_id, room_no):

        student = self.find_student(student_id)
        hostel = self.find_hostel(hostel_id)
        room = hostel.find_room(room_no)

        if student.hostel_name is not None:
            raise RoomTakenError(
                f"{student.student_name} already has accommodation "
                f"in {student.hostel_name}, room {student.room_number}."
            )

        room.add_student(student.student_id)

        student.hostel_name = hostel.name
        student.room_number = room.room_no

    def vacate_student(self, student_id):

        student = self.find_student(student_id)

        if not student.hostel_name or not student.room_number:
            raise AccommodationError(
                f"{student.student_name} does not have an allocated room."
            )

        hostel = None

        for current_hostel in self.hostels:
            if current_hostel.name == student.hostel_name:
                hostel = current_hostel
                break

        if hostel is None:
            raise HostelNotFoundError(
                f"Hostel {student.hostel_name} was not found."
            )

        room = hostel.find_room(student.room_number)
        room.remove_student(student.student_id)

        student.hostel_name = None
        student.room_number = None

    def display_all_rooms(self):

        for hostel in self.hostels:
            hostel.display_rooms()

    def occupancy_summary(self):

        print("\n========== HOSTEL OCCUPANCY SUMMARY ==========")

        total_rooms = 0
        total_occupied = 0
        total_spaces = 0

        for hostel in self.hostels:

            rooms = hostel.total_rooms()
            occupied = hostel.occupied_rooms()
            spaces = hostel.available_spaces()

            total_rooms += rooms
            total_occupied += occupied
            total_spaces += spaces

            print(f"\nHostel: {hostel.name}")
            print(f"Total rooms: {rooms}")
            print(f"Occupied rooms: {occupied}")
            print(f"Available spaces: {spaces}")

        print("\n--------------- TOTALS ----------------")
        print(f"Total rooms: {total_rooms}")
        print(f"Occupied rooms: {total_occupied}")
        print(f"Available spaces: {total_spaces}")

    def search_student(self, student_id):

        student = self.find_student(student_id)
        student.display_details()

        if student.hostel_name and student.room_number:

            hostel = None

            for current_hostel in self.hostels:
                if current_hostel.name == student.hostel_name:
                    hostel = current_hostel
                    break

            if hostel:
                room = hostel.find_room(student.room_number)

                print(f"Room Type: {room.get_room_type()}")
                print(
                    f"Accommodation Fee: "
                    f"UGX {room.calculate_fee():,}"
                )

        return student


# ============================================================
# MAIN MENU
# The menu handles user input while classes handle system logic.
# ============================================================

def main():

    system = Hostel_Management()

    while True:

        print("\n==========================================")
        print("      UNIVERSITY HOSTEL MANAGEMENT")
        print("==========================================")
        print("1. Register student")
        print("2. Allocate student to room")
        print("3. Vacate student")
        print("4. Search student")
        print("5. Display hostel rooms")
        print("6. Display occupancy summary")
        print("7. Exit")
        print("==========================================")

        choice = input("Enter your choice: ").strip()

        try:

            if choice == "1":

                student_id = input("Enter student ID: ").strip()
                name = input("Enter student name: ").strip()
                gender = input("Enter gender: ").strip()
                course = input("Enter course: ").strip()

                try:
                    year = int(input("Enter academic year: "))
                except ValueError:
                    print("Error: Academic year must be a number.")
                    continue

                student = Student(
                    student_id,
                    name,
                    gender,
                    course,
                    year
                )

                system.add_student(student)

                print(
                    f"\n{student.student_name} "
                    f"registered successfully."
                )

            elif choice == "2":

                student_id = input("Enter student ID: ").strip()
                hostel_id = input("Enter hostel ID (e.g. H001): ").strip()
                room_no = input(
                    "Enter room number (e.g. H001-S01): "
                ).strip()

                system.allocate_student(
                    student_id,
                    hostel_id,
                    room_no
                )

                print("\nStudent allocated successfully.")

            elif choice == "3":

                student_id = input("Enter student ID: ").strip()

                system.vacate_student(student_id)

                print("\nStudent has vacated the room successfully.")

            elif choice == "4":

                student_id = input("Enter student ID: ").strip()
                system.search_student(student_id)

            elif choice == "5":

                system.display_all_rooms()

            elif choice == "6":

                system.occupancy_summary()

            elif choice == "7":

                print(
                    "\nThank you for using the "
                    "Hostel Management System."
                )
                break

            else:

                print(
                    "\nInvalid choice. "
                    "Please select a number from 1-7."
                )

        except (
            HostelInputError,
            HostelNotFoundError,
            StudentNotFoundError,
            RoomNotFoundError,
            RoomTakenError,
            DuplicateStudentError,
            AccommodationError,
            ValueError,
            TypeError
        ) as error:

            print(f"\nError: {error}")


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()
