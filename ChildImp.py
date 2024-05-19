import OopsDemo
from OopsDemo import Cal


class childImp(Cal):

    def __init__(self):
        Cal.__init__(self, 5, 10)

    num2 = 200

    def getCompleteData(self):
        return self.num + self.num2 + self.summation()


obj = childImp()
print(obj.getCompleteData())
