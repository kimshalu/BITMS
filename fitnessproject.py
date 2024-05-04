class FitnessClass:
    def __init__(self, class_id, class_name, max_capacity):
        self.class_id = class_id
        self.class_name = class_name
        self.max_capacity = max_capacity
        self.bookings = {}  

    def add_booking(self, user_id):
        if len(self.bookings) < self.max_capacity:
            if user_id not in self.bookings:
                self.bookings[user_id] = True
                return True  
            else:
                raise ValueError("User already booked this class.")
        else:
            raise ValueError("Class is already full.")

    def cancel_booking(self, user_id):
        if user_id in self.bookings:
            del self.bookings[user_id]
            return True  
        else:
            raise ValueError("User did not book this class.")

    def get_bookings(self):
        return self.bookings


class FitnessClassManager:
    def __init__(self):
        self.classes = []

    def add_class(self, fitness_class):
        self.classes.append(fitness_class)
        return True  

    def delete_class(self, class_id):
        for fitness_class in self.classes:
            if fitness_class.class_id == class_id:
                self.classes.remove(fitness_class)
                return True  
        raise ValueError("Class not found.")

    def update_class(self, class_id, new_class_name, new_max_capacity):
        for fitness_class in self.classes:
            if fitness_class.class_id == class_id:
                fitness_class.class_name = new_class_name
                fitness_class.max_capacity = new_max_capacity
                return True 
        raise ValueError("Class not found.")

    def manage_fitness_class_bookings(self, class_id, user_id, action):
        for fitness_class in self.classes:
            if fitness_class.class_id == class_id:
                if action == "book":
                    return fitness_class.add_booking(user_id)
                elif action == "cancel":
                    return fitness_class.cancel_booking(user_id)
                else:
                    raise ValueError("Invalid action.")
        raise ValueError("Class not found.")

    def track_class_attendance(self):
        attendance_data = {}
        for fitness_class in self.classes:
            attendance_data[fitness_class.class_id] = len(fitness_class.get_bookings())
        return attendance_data

    def display_classes(self):
        return [fitness_class.class_name for fitness_class in self.classes]

    def get_class_details(self, class_id):
        for fitness_class in self.classes:
            if fitness_class.class_id == class_id:
                return fitness_class.get_bookings()
        raise ValueError("Class not found.")

import unittest

class TestFitnessClassBookingSystem(unittest.TestCase):
    def setUp(self):
        self.class_manager = FitnessClassManager()
        self.yoga_class = FitnessClass(1, "Yoga", 10)
        self.zumba_class = FitnessClass(2, "Zumba", 15)
        self.class_manager.add_class(self.yoga_class)
        self.class_manager.add_class(self.zumba_class)
        
    def test_add_class(self):
        self.assertTrue(self.class_manager.add_class(FitnessClass(3, "gym", 20)))
        self.assertEqual(len(self.class_manager.classes), 3)
        
    def test_delete_class(self):
        self.assertTrue(self.class_manager.delete_class(1))
        self.assertEqual(len(self.class_manager.classes), 1)
        with self.assertRaises(ValueError):
            self.class_manager.delete_class(1)

    def test_update_class(self):
        self.assertTrue(self.class_manager.update_class(1, "Yoga Plus", 15))
        self.assertEqual(self.class_manager.classes[0].class_name, "Yoga Plus")
    
        with self.assertRaises(ValueError):
            self.class_manager.update_class(3, "gym Gold", 20)

    def test_manage_fitness_class_bookings(self):
        self.assertTrue(self.class_manager.manage_fitness_class_bookings(1, "rachi", "book"))
        self.assertTrue(self.class_manager.manage_fitness_class_bookings(1, "rachi", "cancel"))
        with self.assertRaises(ValueError):
            self.class_manager.manage_fitness_class_bookings(300, "rachi", "book")
        with self.assertRaises(ValueError):
            self.class_manager.manage_fitness_class_bookings(100, "prapul", "invalid_action")

    def test_track_class_attendance(self):
        self.class_manager.manage_fitness_class_bookings(1, "rachi", "book")
        self.class_manager.manage_fitness_class_bookings(1, "prapul", "book")
        attendance_data = self.class_manager.track_class_attendance()
        self.assertEqual(attendance_data[1], 2)

    def test_display_classes(self):
        self.assertEqual(self.class_manager.display_classes(), ["Yoga", "Zumba"])

    def test_display_class_details(self):
        self.class_manager.manage_fitness_class_bookings(1, "rachi", "book")
        self.assertEqual(self.class_manager.get_class_details(1), {"rachi": True})
        with self.assertRaises(ValueError):
            self.class_manager.get_class_details(3)

if __name__=='__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)

