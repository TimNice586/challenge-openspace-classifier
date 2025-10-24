class Seat:
    """creates Seat objects that are initally free with no occupant
    we can:
        seat a person (set_occupant)
        remove the person from his assigned seat (remove_occupant) """
    def __init__(self):
        """ initializes the class with two atributes:
                free (bool): initally the seat is free, seat is free (True) or, if assigned to a person, taken (False)
                occupant (str): initially the occupant is no one, if assigned to a seat it will contain the name of the person on the seat"""
        self.free = True
        self.occupant = None

    def set_occupant(self, name: str) -> None:
        """assigns someone a seat if it's free by linking the name of a person to a seat (occupant)
        if we should try to assign a seat to an already taken one a warning message will be displayed"""
        if self.free == True:
            self.occupant = name
            self.free = False
        else:
            print("Seat at the table is already taken!")
    
    def remove_occupant(self) -> str:
        """removes someone from a seat (we do not use this function it is only extra at the moment)
        if the seat was already free: a message is displayed indicating it was already free
        if someone is removed the seat: the seat is free again by re-initizalizing the seat and the name of the old occupant is returned"""
        if self.free == True:
            return "Seat was already free"
        else:   
            print(f"Seat at the table was taken by {self.occupant} but is now free!")
            self.old_occupant = self.occupant
            self.free = True
            self.occupant = None
            return self.old_occupant

        
class Table(Seat):
    """creates Table objects that are initally free with no occupants
    we can:
        check if the table has a free spot (has_free_spot)
        seat persons at a table (assign_seat)
        remove the person from his assigned seat (remove_occupant) """
    def __init__(self):
        """initializes the class with two attributes
            capacity (int): the number of available seats at each table (it can be a variable too but for now we give at a fixed 4)
            seats (list of Seat): a list of capacity Seat objects (here 4) """
        super().__init__()
        self.capacity = 4
        self.seats = [Seat() for _ in range(self.capacity)] 

    def has_free_spot(self):
        """checks if a table has a free spot and returns True in case, otherwise returns False"""
        if self.left_capacity() == 0:
            return False
        else:
            return True
        
    def assign_seat(self, name: str):
        """assigns a person to a seat at the table"""
        if self.has_free_spot():
            for seat in self.seats:
                if seat.free:
                    seat.set_occupant(name)
                    return
        else:
            return "Table is already full, Find another please!"
                
    def left_capacity(self) -> int:
        """checks how many free seats are left a table"""
        counter = 4
        for seat in self.seats:
            if seat.free == False:
                counter -= 1
        return counter