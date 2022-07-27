from ast import Sub
from pathlib import Path


import numpy
from errors import MissingFilenameException


from flags import ACCESS_MAPPING, F_ANON, F_RDWR, INTERCHANGING_FLAGS, F_RDONLY
import mmap
import py_mmap
from py_mmap_unix import mmap_unix

from py_mmap_window import mmap_window

# need to add error handling right here
def MapRegion(filename , length = 0, prot = None, flags = F_ANON, offset=0):
    # check to see if any of the parameters are missing
    if filename is None :
        raise MissingFilenameException
    
    if py_mmap.system_info() == 'Unix':
        import resource
        if offset % numpy.int64(resource.getpagesize()) == 0:
            return bytearray([])
    
    f = Path(filename)
        
    if length == 0:
        return bytearray([])
    elif length < 0:
        length = Path(filename).stat().st_size
    
    opp = py_mmap.MMapOp(
        filename=filename,
        length=length,
        prot=prot,
        flags=flags,
        offset=offset
    )
    
    if py_mmap.system_info() == "Windows":
       return mmap_window(mmapOp=opp)
   
    elif py_mmap.system_info() == "Unix":
        return mmap_unix(mmapOp=opp)


def Map(f = None, prot = None, flags = F_ANON) -> py_mmap.MMap:
    return MapRegion(f,prot,flags)
            

    
# # test region
# test_content = MapRegion('test.txt', length=-1, flags=F_RDWR)
# print(test_content.Find(MMapOp=test_content.operation, Sub='relative'))
# print(test_content.operation.filename)
# test_content.Write(MMapOp=test_content.operation, Text='\nNew content fuck yeah!\n')
# test_content.Update(MMapOp=test_content.operation)
# print(test_content.content)
# # end test region