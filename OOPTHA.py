#!/usr/bin/env python
# coding: utf-8

# In[1]:


class book:
    def __init__(self,author,name,price,rackno,status,edition):
        self.author = author
        self.name = name
        self.price = price
        self.rackno = rackno
        self.status = status
        self.edition = edition
    def display_book_detail(self):
        pass
    def update_status(self):
        pass
class librarian:
    def __init__(self):
        self.name = name
        self.password = password
    def search_book(self):
        pass
    def verify_member(self):
        pass
    def issue_book(self):
        pass
    def calculate_fine(self):
        pass
    def create_bill(self):
        pass
    def return_book(self):
        pass
class transaction:
    def __init__(self):
        self.trans_id = trans_id 
        self.member_id = member_id
        self.book_id = book_id
        self.date_of_issue = date_of_issue
        self.due_date = due_date
    def create_transaction(self):
        pass

    def delete_transaction(self):
        pass

    def retrieve_transaction(self):
        pass
class member_record:
    def __init__(self):
        self.member_id = member_id
        self.type = type
        self.date_of_membership = date_of_membership
        self.no_of_books_issue = no_of_books_issue
        self.max_book_limit = max_book_limit

    def retrieve_member(self):
        pass

    def increase_book_issued(self):
        pass

    def decrease_book_issued(self):
        pass

    def pay_bill(self):
        pass
class bill:
    def __init__(self):
        self.bill_no = bill_no 
        self.date = date
        self.member = member
        self.amount = amount

    def bill_create(self):
        pass

    def bill_update(self):
        pass
print("!!!!!!!!!!!!!!!!!")

