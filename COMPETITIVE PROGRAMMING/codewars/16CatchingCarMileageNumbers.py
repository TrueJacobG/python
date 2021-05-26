import math


class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.coll = collection
        self.itemspp = items_per_page

    def item_count(self):
        return len(self.coll)

    def page_count(self):
        return math.ceil(len(self.coll)/self.itemspp)

    def page_item_count(self, page_index):
        pages = math.ceil(len(self.coll)/self.itemspp)
        if page_index + 1 > pages:
            return -1
        elif page_index + 1 == pages:
            return len(self.coll) % self.itemspp
        else:
            return self.itemspp

    def page_index(self, item_index):
        if item_index > len(self.coll)-1 or item_index < 0:
            return -1
        return math.floor(item_index/self.itemspp)
