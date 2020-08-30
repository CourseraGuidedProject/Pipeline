
import os
import random
import tempfile
import string

from luigi.local_target import LocalTarget, atomic_file
from contextlib import contextmanager
from pathlib import Path

class suffix_preserving_atomic_file(atomic_file):
    # Overwrite generate_tmp_path method from AtomicLocalFile 
    # in order to perserve the suffix of the input file.
    def generate_tmp_path(self, path):
        name = Path(path).stem
        suffix = Path(path).suffix
        return name + '-luigi-tmp-%09d' % random.randrange(0, 1e10) + suffix


class BaseAtomicProviderLocalTarget(LocalTarget):
    # Allow some composability of atomic handling
    atomic_provider = atomic_file

    def open(self, mode='r'): ## TODO: need to handle more modes
        # leverage super() as well as modifying any code in LocalTarget
        # to use self.atomic_provider rather than atomic_file
        if mode == 'w':
            self.makedirs()
            return self.format.pipe_writer(self.atomic_provider(self.path))
        
        return super().open(mode)

    @contextmanager
    def temporary_path(self):
        # NB: unclear why LocalTarget doesn't use atomic_file in its implementation
        self.makedirs()
        with self.atomic_provider(self.path) as af:
            yield af.tmp_path


class SuffixPreservingLocalTarget(BaseAtomicProviderLocalTarget):
    atomic_provider = suffix_preserving_atomic_file