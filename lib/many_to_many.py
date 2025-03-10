class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        Author.all_authors.append(self)
    
    def contracts(self):
        """Return a list of contracts associated with this author."""
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        """Return a list of books associated with this author using the Contract class."""
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        """Sign a contract between this author and the specified book."""
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class.")
        contract = Contract(self, book, date, royalties)
        return contract
    
    def total_royalties(self):
        """Return the total amount of royalties the author has earned from all their contracts."""
        return sum(contract.royalties for contract in self.contracts())
    
    def __repr__(self):
        return f"Author({self.name!r})"

    pass


class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        Book.all_books.append(self)
    
    def __repr__(self):
        return f"Book({self.title!r})"

    pass



class Contract:
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of the Author class.")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class.")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all_contracts.append(self)
    
    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts signed on the specified date."""
        return [contract for contract in cls.all_contracts if contract.date == date]
    
    def __repr__(self):
        return f"Contract({self.author.name!r}, {self.book.title!r}, {self.date!r}, {self.royalties!r})"

    pass