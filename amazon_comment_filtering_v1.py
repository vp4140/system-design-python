"""
comment
do you want filtering on different types?Like multiflitering strategy?
Amazon Product : reviews are different types..
How da you filter comments?


Spam commets? Abusifve somments??

Comment?
id,
comment
state = []

class CommentStregy(ABC):
        @staticmetehod
        def filter(cooment): str
            pass
class SpamStegrtey(CommenrStrategy):
    def __init__(self):
        self.arr = ["Promotion","Buy","Sale","Spam","Fake"]
    def filter(comment:Comment):
            for ele in comment.comment.split():
                if ele in self.arr:
                    comment.state.append("Spam")
            return comment
class commentContext:
    def __init__(stretygy: [CommenStrarye])
        self.strategy = strategy
    def changeStratey(self,strategy:CommentStrategy):
        self.strategy = strategy
    def filter(comment:Comment):
        arr = []
        for strategy in self.strategy:


if __name__ == "main":
    s = Spamstarty()
    c = Comment(1,"hello I am Promotion"]

    c = commentContext(s)
    c.filter(c)
    c.state






---










Profanity, Spam,
Comment:
CommentStrategy:
SpamFilter
Profanity filter
"""
from typing import List
from abc import ABC, abstractmethod


class Comment:
    def __init__(self,id:str,comment:str):
        self.id = id
        self.comment = comment
        self.type = "Approved"
    def flag_comment(self):
        self.type = "Flagged"

class CommentStrategy(ABC):
    @abstractmethod
    def filter(self,comment:Comment):
        pass
class SpamFilter(CommentStrategy):
    def __init__(self):
        self.words_in_str = ["Promotion","Buy","Sale","Spam","Fake"]

    def filter(self,comment:Comment):

        for ele in comment.comment.split():
            if ele in self.words_in_str:
                return True
        return False

class AbusiveFilter(CommentStrategy):
    def __init__(self):
        self.words_in_str = ["abuse","shit"]
    def filter(self, comment: Comment):
        for ele in comment.comment.split():
            if ele in self.words_in_str:
                return True
        return False
class FilteringSystemContext:
    def __init__(self,filter:List[CommentStrategy]):
        self.filterarr = filter
    def apply_filter(self,comment):
        for filter in self.filterarr:
            if filter.filter(comment):
                comment.flag_comment()
                return "Flagged"
        return "Approved"


if __name__=="__main__":
    print("Start")
    c = Comment(1, "Hello I am here")
    c2 = Comment(1, "Hello I here")
    f = FilteringSystemContext([SpamFilter(), AbusiveFilter()])
    f.apply_filter(c)
    print(c.type)
    f.apply_filter(c2)
    print(c2.type)
    print("Done")

class Comment:
    def __init__(self,id:str,comment:str):
        self.id = id
        self.comment = comment
        self.type = "Approved"

class CommentStrategy(ABC):
    @abstractmethod
    def filter(self,comment:Comment):
        pass

class SpamFilter(CommentStrategy):
    def __init__(self):
        self.words_in_str = ["Promotion","Buy","Sale","Spam","Fake"]
    def filter(self,comment:Comment):
        for ele in comment.comment.split():
            if ele in self.words_in_str:
                return True
        return False



"""
Comments 

"""





