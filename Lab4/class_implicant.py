class Implicant(object):
    def __init__(self, name, isCore, toCover, isUsed):
        self.__name = name
        self.__isCore = isCore
        self.__toCover = toCover
        self.__isUsed = isUsed

    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self, value):
        self.__name = value
    
    @property
    def IsCore(self):
        return self.__isCore
    @IsCore.setter
    def IsCore(self, value):
        self.__isCore = value
    
    @property
    def ToCover(self):
        return self.__toCover
    @ToCover.setter
    def ToCover(self, value):
        self.__toCover.append(value)
    
    @property
    def IsUsed(self):
        return self.__isUsed
    @IsUsed.setter
    def IsUsed(self, value):
        self.__isUsed = value
    
    def printInfo(self):
        print("%s | %s | %s | %s" % (self.__name, self.__isCore, self.__toCover, self.IsUsed))