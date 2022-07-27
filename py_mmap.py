import mmap
import platform
from flags import ACCESS_MAPPING, F_ANON, INTERCHANGING_FLAGS

def system_info():
    return platform.system()

def preq_file_operation(func):
    def wrapper(*args,**kwargs):
        # extract arguments
        op = kwargs.get('MMapOp')
        with open(op.filename, mode = INTERCHANGING_FLAGS[op.flags], encoding='utf-8') as f:
            with mmap.mmap(f.fileno(),length=op.length, access=ACCESS_MAPPING[op.flags], offset=op.offset) as mmap_obj:
                if kwargs.__contains__("Sub"):
                    loc = mmap_obj.find(str.encode(kwargs.get('Sub')))
                    print(mmap_obj.size())
                    mmap_obj.close()
                    return loc
                elif kwargs.__contains__("Text"):
                    # resize the file to write new content
                    old_size = mmap_obj.size()
                    new_size = old_size + len(bytes(kwargs.get('Text'), encoding='utf-8'))
                    mmap_obj.resize(new_size)
                    #update content using slice notation
                    mmap_obj[old_size:] = bytes(kwargs.get('Text'), encoding='utf-8')
                    # set the current file pointer to the start of the file
                    mmap_obj.seek(0)
                    print(mmap_obj.read())
                    mmap_obj.close()
                # if only keyword argument (and in this case its MMemOp object) provided means read method lmao
                else:
                    content = mmap_obj.read()
                    return content
                
    return wrapper

class MMapOp():
    def __init__(self, filename, length = 0, prot = None, flags = F_ANON, offset = 0):
        self.filename = filename
        self.length = length
        self.prot = prot
        self.flags = flags
        self.offset = offset
        
    

class MMap(): 
    def __init__(self, content = None, operation = None):
        self.content = content
        self.operation = operation
        self.sys = system_info()
    
    # return the content of the underlying file
    @property
    def Header(self):
        return self.content
    
    @Header.setter
    def Header(self, value):
        self.content = value
    
    # find a specific word in the underlying file 
    # Find(MMapOp: MMapOp, Sub: str) -> int:
    @preq_file_operation    
    def Find(self, **kwargs):
        pass
    
    # write new content to the underlying file
    # Write(MMapOp: MMapOp, Sub: str) 
    @preq_file_operation
    def Write(self, **kwargs):
        pass
    
    # read new content from the underlying file
    # Read(MMapOp: MMapOp)
    @preq_file_operation
    def Read(self, **kwargs):
        pass
    
    # update MMapOp's content value
    # should be called right after a Write command 
    # Update(MMapOp: MMapOp)
    def Update(self, **kwargs):
        new_content = self.Read(**kwargs)
        self.Header(new_content)