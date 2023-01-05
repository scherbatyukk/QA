import pytest
from array import array
from directory import Directory
from binaryFile import BinaryFile
from logTextFile import LogTextFile
from bufferFile import BufferFile

class TestDirectory:
    fatherDirectory = Directory('fatherDir')

    def test_directoryCreation(self):
        maxElements = 10
        name = 'name1'
        directory =Directory(name, maxElements)

        assert directory.name == name
        assert directory.DIR_MAX_ELEMS == maxElements
        assert directory.elementsCount == 0
        assert pytest.raises(OverflowError)

    def test_directoryMove(self):
        directory = Directory('dir')
        assert pytest.raises(OverflowError)

        directory.__move__(self.fatherDirectory)

        assert directory.father == self.fatherDirectory

    def test_directoryDeletion(self):
        directory = Directory('dir')

        del directory

        assert 'directory' not in locals()

class TestBinary:
    fatherDirectory = Directory('fatherDir')

    def test_binaryCreation(self):
        name = 'name1'
        content = 'content'
        binary = BinaryFile(name, content, self.fatherDirectory)

        assert binary.fileName == name
        assert binary.content == content
        assert binary.__read__() == content
        assert binary.father == self.fatherDirectory

    def test_binaryMove(self):
        name = 'name1'
        content = 'content'
        binary = BinaryFile(name, content)
        assert pytest.raises(OverflowError)

        binary.__move__(self.fatherDirectory)

        assert binary.father == self.fatherDirectory

    def test_binaryDeletion(self):
        binary = BinaryFile('bin')

        del binary

        assert 'binary' not in locals()

class TestBuffer:
    fatherDirectory = Directory('fatherDir')

    def test_bufferCreation(self):
        name = 'name1'
        size = 10
        buffer = BufferFile(name, size, self.fatherDirectory)

        assert buffer.fileName == name
        assert buffer.MAX_BUF_FILE_SIZE == size
        assert pytest.raises(OverflowError)
        assert buffer.father == self.fatherDirectory

    def test_bufferMove(self):
        name = 'name1'
        content = 'content'
        buffer = BufferFile(name, content)
        assert pytest.raises(OverflowError)
        
        buffer.__move__(self.fatherDirectory)

        assert buffer.father == self.fatherDirectory

    def test_bufferDeletion(self):
        buffer = BufferFile('buffer')

        del buffer

        assert 'buffer' not in locals()

    def test_bufferAddConsume(self):
        name = 'name1'
        size = 10
        line1 = 'line1'
        line2 = 'line2'
        buffer = BufferFile(name, size)

        buffer.__push__(line1)
        buffer.__push__(line2)

        assert buffer.__consume__() == line1
        assert buffer.__consume__() == line2
        assert pytest.raises(OverflowError)

class testLog:
    fatherDirectory = Directory('fatherDir')

    def test_logCreation(self):
        name = 'name1'
        log = LogTextFile(name, self.fatherDirectory)

        assert log.fileName == name
        assert pytest.raises(OverflowError)
        assert log.father == self.fatherDirectory

    def test_logMove(self):
        name = 'name1'
        log = LogTextFile(name)
        assert pytest.raises(OverflowError)

        log.__move__(self.fatherDirectory)

        assert log.father == self.fatherDirectory

    def test_logDeletion(self):
        log = LogTextFile('log')

        del log
        assert 'log' not in locals()

    def test_logAddRead(self):
        name = 'name1'
        line1 = 'line1'
        line2 = 'line2'
        log = LogTextFile(name)

        log.__log__(line1)
        log.__log__(line2)

        assert log.__read__() == '\r\n' + line1 + '\r\n' + line2