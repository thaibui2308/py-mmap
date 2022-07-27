import mmap
from flags import ACCESS_MAPPING, F_ANON, INTERCHANGING_FLAGS
from py_mmap import MMap


def mmap_window(mmapOp = None):
    with open(mmapOp.filename, mode = INTERCHANGING_FLAGS[mmapOp.flags], encoding="utf-8") as f:
        with mmap.mmap(f.fileno(),length=mmapOp.length, access=ACCESS_MAPPING[mmapOp.flags], offset=mmapOp.offset) as mmap_object:
            content = mmap_object.read()
            mmap_object.close()
            return MMap(content=content, operation=mmapOp)
    