class Book:
 
    def __init__(self, name, author, comment, state = 0):
        self.name = name
        self.author = author
        self.comment = comment
        self.state = state
 
    def __str__(self):
        status = 'Not loaned'
        if self.state == 1:
            status = 'Out on loan'
        return 'Name：《%s》 Author：%s Comment：%s\nState：%s ' % (self.name, self.author, self.comment, status)
 
class BookManager:

    books = []
    def __init__(self):
        book1 = Book('The Book of Disquiet','Fernando Pessoa','The self-revelation of a disoriented soul on the verge of collapse, a hymn of obscurity, failure, wisdom, difficulty, and silence.')
        book2 = Book('Life in the Woods','Henry David Thoreau','part personal declaration of independence, social experiment, voyage of spiritual discovery, satire, and manual for self-reliance.')
        book3 = Book('The Heart Is a Lonely Hunter','Carson McCullers','We are eager to talk, but we never listen. Girls, blacks, dumbs, drunks, and widowers have different forms of loneliness, but they never leave.',1)
        self.books.append(book1)
        self.books.append(book2)
        self.books.append(book3)
 
    def menu(self):
        print('Welcom to use Vagrant Book Management System.\n')
        while True:
            print('1.Show all books\n2.Add books\n3.Lend books\n4.Return books\n5.Exit system\n')
            choice = int(input('Please enter the number to select the corresponding function：'))
            if choice == 1:
                self.show_all_book()
            elif choice == 2:
                self.add_book()
            elif choice == 3:
                self.lend_book()
            elif choice == 4:
                self.return_book()
            else:
                print('Thank you for using Vagrant Book Management System.')
                break
 
    def show_all_book(self):
        print('Books information：')
        for book in self.books:
            print(book)
            print('')

    def add_book(self):
        new_name = input('Please input the name of the book：')
        new_author =  input('Please input the author of the book：')
        new_comment = input('Please input the comment of the book：')
        new_book = Book(new_name, new_author, new_comment)
        self.books.append(new_book)
        print('Added in successfully\n')

    def check_book(self,name):
        for book in self.books:
            if book.name == name:
                 return book 
        else:
            return None

    def lend_book(self):
        name = input('Please input the name of the book：')
        res = self.check_book(name)

        if res != None:
            if res.state == 1:
                print('Out on loan')
            else:
                print('Successfully borrowed')
                res.state = 1
        else:
            print('Not found in system')
    
    def return_book(self):
        name = input('Please input the name of the book：')
        res = self.check_book(name)
        if res == None:
            print('No match, error')
        else:
            if res.state == 0:
                print('Not loaned')
            else:
                print('Successfully returned')
                res.state = 0
 
manager = BookManager()
manager.menu()
