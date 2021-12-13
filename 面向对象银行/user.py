
class User:
    __card_id=0
    __password=''
    __name=''
    __country=''
    __province=''
    __street=''
    __door=''
    __money=0
    def set_mes(self,id,pwd,nm,con,pro,str,dor):
        self.__card_id=id
        self.__password=pwd
        self.__name=nm
        self.__country=con
        self.__province=pro
        self.__street=str
        self.__door=dor
    def get_card(self):
        return self.__card_id

    def get_password(self):
        return self.__password

    def get_name(self):
        return self.__name

    def get_country(self):
        return self.__country

    def get_province(self):
        return self.__province

    def get_street(self):
        return self.__street

    def get_door(self):
        return self.__door


