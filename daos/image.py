#import psycopg2


class ImageDAO:
    def __init__(self):
    #An message_id = -1 means there's no image in the message
        I1 = [1, 0]
        I2 = [2, 3]
        I3 = [3, 2]
        I4 = [4, 1]
        I5 = [5, 0]

        self.data = []
        self.data.append(I1)
        self.data.append(I2)
        self.data.append(I3)
        self.data.append(I4)
        self.data.append(I5)


    def getAllImages(self):
        return self.data

    def getImagesById(self, image_id):
        for i in self.data:
            if int(image_id) == i[0]:
                return i
        return None

    def searchByMessageId(self, message_id):
        result = []
        for i in self.data:
            if int(message_id) == i[1]:
                result.append(i)
        return result

    def searchImagesSameMessages(self, message_id):
        result = []
        for i in self.data:
            if int(message_id) == i[1]:
                result.append(i)
        return result

