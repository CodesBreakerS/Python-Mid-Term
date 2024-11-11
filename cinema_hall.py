
class star_cinema:
    hall_list: list = []    #class attribute
    
    def entry_hall(self):
        star_cinema.hall_list.append(self)
        
    
    

class Hall(star_cinema):

    def __init__(self,rows,cols,hall_no): #instance attribute
        self.seats = {}
        self.__rows = rows   
        self.cols = cols        ##  public attribute
        self.__hall = hall_no   ##  private attribute
        self._show_list = []    ##  Protected attribute
        self.entry_hall()
    
    def entry_show(self,show_id,movie_name,time):
        self._show_id = show_id
        self._movie_name = movie_name
        self.time = time
        self.info = (show_id,movie_name,time)
        self._show_list.append(self.info)
        seat_l = [[0 for i in range(self.cols)] for i in range(self.__rows)]
        self.seats[show_id] = seat_l
        
    def book_seats(self,show_id,row,col,ticket):
        # for _ in range(ticket):
        if show_id in self.seats:
            if row<=self.__rows and col <=self.cols:
                    # for i in self.seats[show_id][row-1][col-1]:
                if self.seats[show_id][row-1][col-1] == 1:
                    print('This seat is already booked.')
                    ticket+=1
                else:
                    self.seats[show_id][row-1][col-1] = 1
                    print(f'The ({row},{col}) seat is booked successfully !')
            else:
                print('The seat number is invalid')
        else:
            print(f'There is no show in this id')

    def view_show_list(self):
        
        # if len(self._show_list) == 0:
        #     print('\tEmpty')
        # else:
        for i in range(len(self._show_list)):
            print(f'Show ID:{self._show_list[i][0]} Movie Name:{self._show_list[i][1]} Time:{self._show_list[i][2]}')
        
    def view_available_seats(self,id):
        for col in self.seats[id]:
            print(col)

            
cinema = star_cinema()
hall1 = Hall(4,5,'1')
hall2 = Hall(4,5,'2')

while True:

    print("""
1.View All Show Today.
2.View Available Seats.
3.Book Ticket.
4.Entry Show.
5.Exit.""")
    op = int(input('Enter Option: '))
    # currentHall = hall1
    
    if op == 1:
        if all(len(hall._show_list) == 0 for hall in cinema.hall_list):
            print('!!!!!!!!!!!!!!!!!!!!')
            print('\tEmpty')
            print('!!!!!!!!!!!!!!!!!!!!')
        
        else:
            print('--------------------')
            for hall in cinema.hall_list:
                hall.view_show_list()
            print('--------------------')
    elif op == 2:
        id = input('Enter Show id: ')
        for hall in cinema.hall_list:
            # if hall._show_list == id:
            if id in hall.seats:
                hall.view_available_seats(id)
                break
            else:
                print('---------##-----------')
                print('There is no show in this name!')
                print('---------##-----------')
                break
    elif op == 3:
        id = input("Show ID: ")
        for hall in cinema.hall_list:
            # if hall._show_list == id:
            if id in hall.seats:
                ticket = int(input('Number of ticket? '))
                for _ in range(ticket):
                    row = int(input('Enter seat Row: '))
                    col = int(input('Enter seat column: '))
                    # for hall in cinema.hall_list:
                    #     # if hall._show_list == id:
                    #     if id in hall.seats:
                    hall.book_seats(id,row,col,ticket)
                else:
                    print('********************')
                    print('    Updated seats')
                    print('********************')
                    for hall in cinema.hall_list:
                        # if hall._show_list == id:
                        if id in hall.seats:
                            hall.view_available_seats(id)
                    break
            else:
                print('*******!!!!*********')
                print('Invalid Show ID!')
                print('*******!!!!*********')
                break
            
    elif op == 4:
        hall_id = input('Entry hall no: (1/2)')
        if hall_id == '1':
            show_id = input('Entry show id: ')
            movie_name = input('Entry Movie name: ').strip().lower()
            time = input('Entry time schedule: ')
            # if show_id and movie_name not in hall1._show_list:
            hall1.entry_show(show_id,movie_name,time)
            # else:
            #     print('The show is already inserted.')
        elif hall_id == '2':
            show_id = input('Entry show id: ')
            movie_name = input('Entry Movie name: ').strip().lower()
            time = input('Entry time schedule: ')
            # if show_id and movie_name in hall2._show_list:
            print('The show is already inserted.')
            # else:
            #     hall2.entry_show(show_id,movie_name,time)
        
    elif op == 5:
        print('Exit')
        break
        
        
