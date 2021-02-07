from page import page
from frame import frame
from dm import diskManager


class BufferPoolFullError(Exception):
    # exception used in the Clock class
    def __init__(self, message):
        self.message = message


class clock:
    def __init__(self):
        # do the required initializations
        self.current = 0

    def pickVictim(self, buffer):
        # find a victim page using the clock algorithm and return the frame number
        # if all pages in the buffer pool are pinned, raise the exception BufferPoolFullError
        current = 0
        for i in buffer:
            if i.pinCount >= 1:
                self.current += 1
                continue
            else:
                self.current += 1
                i.referenced = 0
        for ii in buffer:
            if ii.pinCount == 0 and ii.referenced == 0:
                return ii.currentPage.pageNo


# ==================================================================================================

class bufferManager:

    def __init__(self, size):
        self.buffer = []
        self.clk = clock()
        self.dm = diskManager()
        for i in range(size):
            self.buffer.append(frame())  # creating buffer frames (i.e., allocating memory)
            self.buffer[i].frameNumber = i

    # ------------------------------------------------------------

    def pin(self, pageNumber, new=False):

        for i in self.buffer:
            if i.currentPage.pageNo == pageNumber:
                i.pinCount += 1
                i.referenced = 1
                i.currentPage.content = pageNumber
                return i

        if new:
            victim_frame = self.clk.pickVictim(self.buffer)
            for i in self.buffer:
                if i.frameNumber == victim_frame:
                    if i.dirtyBit:
                        self.dm.writePageToDisk(i.currentPage)
                    i.pinCount = 1
                    i.dirtyBit = False
                    i.currentPage.pageNo = pageNumber
                    i.referenced = 1
                    i.currentPage.content = pageNumber
                    return i
        if not new:
            victim_frame = self.clk.pickVictim(self.buffer)
            for i in self.buffer:
                if i.frameNumber == victim_frame:
                    if i.dirtyBit:
                        self.dm.writePageToDisk(self.dm)
                    i.pinCount = 1
                    i.dirtyBit = False
                    i.currentPage = self.dm.readPageFromDisk(pageNumber)
                    i.referenced = 1
                    i.currentPage.content = pageNumber
                    return i
        # given a page number, pin the page in the buffer
        # if new = True, the page is new so no need to read it from disk
        # if new = False, the page already exists. So read it from disk if it is not already in the pool.
        pass

    # ------------------------------------------------------------
    def unpin(self, pageNumber, dirty):
        for i in self.buffer:
            if i.currentPage.pageNo == pageNumber:
                if dirty:
                    i.dirtyBit = True
                i.pinCount -= 1
            break

    def flushPage(self, pageNumber):
        # Ignore this function, it is not needed for this homework.
        # flushPage forces a page in the buffer pool to be written to disk
        for i in range(len(self.buffer)):
            if self.buffer[i].currentPage.pageNo == pageNumber:
                self.dm.writePageToDisk(self.buffer[i].currentPage)  # flush writes a page to disk
                self.buffer[i].dirtyBit = False

    def printBufferContent(self):  # helper function to display buffer content on the screen (helpful for debugging)
        print("---------------------------------------------------")
        for i in range(len(self.buffer)):
            print("frame#={} pinCount={} dirtyBit={} referenced={} pageNo={} pageContent={} ".format(
                self.buffer[i].frameNumber, self.buffer[i].pinCount, self.buffer[i].dirtyBit, self.buffer[i].referenced,
                self.buffer[i].currentPage.pageNo, self.buffer[i].currentPage.content))
        print("---------------------------------------------------")
