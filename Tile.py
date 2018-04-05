tileType = dict(empty = 0, ship=1, hit=2, miss=3, hidden=4)


class Tile(object):
    '''Each tile has a state'''
    def __init__(self,type):
        if type==tileType['empty']:
            self.__m_type = ('0', tileType['empty'])
        elif type==tileType['ship']:
            self.__m_type = ('1', tileType['ship'])
        elif type==tileType['hit']:
            self.__m_type = ('x', tileType['hit'])
        elif getType==tileType['miss']:
            self.__m_type = ('w', tileType['miss'])
        elif getType == tileType['hidden']:
            self.__m_type = ('0', tileType['hidden'])

    #report
    def __str__(self):
        rep = ""
        if self.getType == tileType['empty']:
            rep = "0"
        elif self.getType == tileType['ship']:
            rep = "1"
        elif self.getType == tileType['hit']:
            rep = "x"
        elif self.getType == tileType['miss']:
            rep = "w"
        elif self.getType == tileType['hidden']:
            rep = "0"
        return rep

    #set
    def setTile(self, type)
         if type == tileType['empty']:
            self.__m_type = ('0', TILE_TYPE['empty'])
        elif type == tileType['ship']:
            self.__m_type = ('1', TILE_TYPE['ship'])
        elif type == tileType['hit']:
            self.__m_type = ('X', TILE_TYPE['hit'])
        elif type == tileType['miss']:
            self.__m_type = ('W', TILE_TYPE['miss']) 
        elif type == tileType['hidden']:
            self.__m_type = ('0', TILE_TYPE['hidden'])

     #gets
    @property
    def getType(self):
        return self.__m_type;