# TODO: complete this class
import math


class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.coll = collection
        self.itemspp = items_per_page

    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.coll)

    # returns the number of pages

    def page_count(self):
        return math.ceil(len(self.coll)/self.itemspp)

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        pages = math.ceil(len(self.coll)/self.itemspp)
        if page_index + 1 > pages:
            return -1
        elif page_index + 1 == pages:
            return len(self.coll) % self.itemspp
        else:
            return self.itemspp

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index > len(self.coll)-1 or item_index < 0:
            return -1
        return math.floor(item_index/self.itemspp)
