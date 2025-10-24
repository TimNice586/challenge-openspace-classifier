from utils.table import Table, Seat
import random

class Openspace(Table):
    """creates Openspace objects representing a room with 6 tables and a list of 6 Table objects"""
    def __init__(self):
        """initializes the class with two attributes
            number_of_tables (int): the number of available tables at each openspace (it can be a variable too but for now we give at a fixed 6)
            tables (list of Table): a list of number_of_tables Table objects (here 6)"""
        super().__init__()
        #to be able to test i create the list of tables here and number of tables a fixed 6
        self.number_of_tables = 6
        self.tables = [Table() for _ in range(self.number_of_tables)]
        
    def organize(self, names: list) -> None:
        """randomly assigns people to Seat objects in the different Table objects
        first randomize the available students in from a list of names (random.shuffle)
        then "cycle" through each name and assign it to a table:
            by first cycling through the 4 available seat of each table (j)
            by then cycling through the 6 available tables
            which leaves us 24 names to fill in at 6 tables with 4 seats
        we also introduce a new variable for this task: name_index 
            name_index forces correct "jumps" to the index in order to always seat a new name from the list
        finally a message is printed stating the program was successfull"""
        random.shuffle(names)
        for j in range(self.capacity):
            for i in range(self.number_of_tables):
                name_index = i*(self.capacity)+j
                self.tables[i].assign_seat(names[name_index])
        print(f"\nall Tables are filled randomly:")
    
    def get_seating_dict(self):
        """creates and returns a dictionary"""
        seating_dict = {}
        for i, table in enumerate(self.tables):
            table_number = f"Table {i+1}"
            occupants_at_table = [seat.occupant for seat in table.seats]
            seating_dict[table_number] = occupants_at_table
        return seating_dict

    def display(self):
        """displays the seated names at each table by:
        getting a dictionary with randomly seated people (get_seating_dict)
        adding each assigned name one by one with (key:value) pair as (table with number: list of 4 names occupying the seats of said table)
        printing out the dictionary line by line so it produces a nice visual"""
        seating_dict = self.get_seating_dict()
        for table, occupants_at_table in seating_dict.items():
            print(f"{table} : {occupants_at_table}")
        print()

       

    def store(self, filename: str="output.csv"):
        """stores the result (seating_dict) in a CSV file output.csv by:
        first reusing the display method and writing it line by line into the file"""
        seating_dict = self.get_seating_dict()
        with open (filename, "w",encoding="utf-8") as result:
            for table, occupants in seating_dict.items():
                occupants = [occupant for occupant in occupants]
                row = f"{table}: " + ", ".join(occupants) + "\n"
                result.write(row)
        print(f"\nSeating can also be found in '{filename}'!")
        print()