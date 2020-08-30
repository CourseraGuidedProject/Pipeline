
import os
from tempfile import TemporaryDirectory
from unittest import TestCase

from csci_utils.io.io import atomic_write

class FakeFileFailure(IOError):
    pass

class AtomicWriteTests(TestCase):
    def test_atomic_write(self):
        """Ensure file exists after being written successfully"""

        with TemporaryDirectory() as tmp:
            fp = os.path.join(tmp, "abcd.txt")

            with atomic_write(fp, "w") as f:
                assert not os.path.exists(fp)
                tmpfile = f.name
                f.write("1234")

            assert not os.path.exists(tmpfile)
            assert os.path.exists(fp)

            with open(fp) as f:
                self.assertEqual(f.read(), "1234")

    def test_atomic_failure(self):
        """Ensure that file does not exist after failure during write"""

        with TemporaryDirectory() as tmp:
            fp = os.path.join(tmp, "abcd.txt")

            with self.assertRaises(FakeFileFailure):
                with atomic_write(fp, "w") as f:
                    tmpfile = f.name
                    assert os.path.exists(tmpfile)
                    raise FakeFileFailure()

            assert not os.path.exists(tmpfile)
            assert not os.path.exists(fp)

    def test_file_exists(self):
        """Ensure an error is raised when a file exists"""
        with TemporaryDirectory() as temp:
            fp=os.path.join(temp, "qwert.txt")

            with atomic_write(fp, "w") as f:
                f.write("qwert")
            
            assert os.path.exists(fp)

            try:
                with atomic_write(fp, "w") as f:
                    f.write("1234")
            except FileExistsError as e:
                self.assertIsInstance(e, FileExistsError)