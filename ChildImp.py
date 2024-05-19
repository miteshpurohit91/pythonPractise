from OopsDemo import Cal


class childImp(Cal):

    num2 = 200

    def getCompleteData(self):
        return self.num + self.num2
