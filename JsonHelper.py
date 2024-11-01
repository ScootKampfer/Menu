import json

class JsonManager():
    def __init__(self) -> None:
        self.dict = {}
        self.file_name = ""

    def open(self,file_name:str):
        self.file_name = file_name
        try:self.dict = json.loads(open(file_name,"r").read())
        except: open(file_name,"w").close()

    def getValue(self,key:str):
        try:
            if self.file_name != "":return self.dict[key]
        except KeyError:return KeyError

    def Value(self,key:str,value:any):
        if self.file_name == "":print("JsonSaving Error: no file oppened, cannot modify/add value (Val Function)");return
        file = open(self.file_name,"w")
        try:
            if isinstance(self.dict[key],list):print("please use the ListValue to modify/add a value to an List ");return
            if isinstance(self.dict[key],dict):print("Please use function dictValue to modify/add a value to a Dictionary");return
        except:pass
        self.dict[key] = value
        file.write(json.dumps(self.dict, indent=4))
        file.close()

    def ListValue(self,listname:str,index:int,value:any):
        if self.file_name == "":print("JsonSaving Error: no file oppened, cannot modify/add value (Val Function)");return
        file = open(self.file_name,"w")
        try:
            if isinstance(self.dict[listname],dict):print("Please use function DictValue to modify/add a value to a Dictionary");return
        except:pass
        try:
            self.dict[listname][index] = value
            file.write(json.dumps(self.dict, indent=4))
            file.close()
        except:
            self.dict[listname] = []
            try:self.dict[listname][index] = value
            except:self.dict[listname].append(value)
            file.write(json.dumps(self.dict, indent=4))
            file.close()
        
    def List(self,listname:str,list:list):
        if self.file_name == "":print("JsonSaving Error: no file oppened, cannot modify/add value (Val Function)");return
        file = open(self.file_name,"w")
        self.dict[listname] = list
        file.write(json.dumps(self.dict, indent=4))
        file.close()

    def Dict(self,dictname:str,dict:dict):
        if self.file_name == "":print("JsonSaving Error: no file oppened, cannot modify/add value (Val Function)");return
        file = open(self.file_name,"w")
        self.dict[dictname] = dict
        file.write(json.dumps(self.dict, indent=4))
        file.close()
        
    def DictValue(self,dictname:str,key:any,value:any):
        if self.file_name == "":print("JsonSaving Error: no file oppened, cannot modify/add value (Val Function)");return
        file = open(self.file_name,"w")
        try:
            if isinstance(self.dict[dictname],list):print("Please use function ListValue to modify/add a value to a List");return
        except:pass
        try:
            self.dict[dictname][key] = value
            file.write(json.dumps(self.dict, indent=4))
            file.close()
        except:
            self.dict[dictname] = {}
            self.dict[dictname][key] = value
            file.write(json.dumps(self.dict))
            file.close()

    def reset(self):
        self.dict = {}
        self.file_name = ""

    def is_opened(self):
        if self.file_name != "":return True
        else:return False
