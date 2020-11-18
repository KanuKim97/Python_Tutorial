book = 100


def library(student):
    global book
    book = book - student
    print("남은 책 : {0}".format(book))


def library_return(book_1, student):
    book_1 = book - student
    return book_1


print("전체 책 : {0}".format(book))
# library(3)
book = library_return(book, 3)
print("남은 책 : {0}".format(book))
