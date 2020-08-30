from contextlib import contextmanager
import os
import io
import tempfile
from atomicwrites import atomic_write as _backend_writer, AtomicWriter


class SuffixWriter(AtomicWriter):
    """ Subclass AtomicWriter to override the get_fileobject method. 
    """

    def get_fileobject(self, dir=None, **kwargs):
        """ Override the function from AtomicWriter in order to 
        keep the original file extension for the temp file
        :param dir: the directory for the target file 
        :param kwargs: optional arguments 
        :return:  the temporary file to use.
        """
        if dir is None:                 #pragma: no cover
            dir = os.path.normpath(os.path.dirname(self._path))

        filename, ext = os.path.splitext(self._path)

        descriptor, name = tempfile.mkstemp(suffix=ext, prefix=filename, dir=dir)

        os.close(descriptor)  # no longer needs the descriptor, close for reuse.
        kwargs["mode"] = self._mode
        kwargs["file"] = name
        return io.open(**kwargs)


@contextmanager
def atomic_write(file, mode="w", as_file=True, new_default="asdf", **kwargs):
    """ Wrapper function for atomicwrites.atomic_write. 
    The SuffixWriter class keeps the file extension of the original file.
    
    :param file: str or :class:'os.PathLike' target to write
    
    :param bool as_file:  if True, the yielded object is a :class:File.
        (eg, what you get with `open(...)`).  Otherwise, it will be the
        temporary file path string

    :param kwargs: anything else needed to open the file

    :raises: FileExistsError if target exists

    Example::

        with atomic_write("hello.txt") as f:
            f.write("world!")

    
    """
    # User _backend_writer to implement the writing.
    with _backend_writer(file, writer_cls=SuffixWriter, **kwargs) as f:

        if not as_file:             #pragma: no cover
            f = os.fspath(file)  # return the temporary file path string
        yield f
