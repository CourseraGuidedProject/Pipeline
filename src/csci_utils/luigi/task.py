# csci_utils: Using composition to implement requires() and output()
import os

from functools import partial
from luigi.local_target import LocalTarget
from dask.bytes.core import get_fs_token_paths

class Requirement:
    def __init__(self, task_class, **params):
        self.task_class = task_class
        self.params = params

    def __get__(self, task, cls):
        if task is None:        #do we need this? extra...?
            return self
        return task.clone(
            self.task_class,
            **self.params)


class Requires:
    """Composition to replace :meth:`luigi.task.Task.requires`

    Example::

        class MyTask(Task):
            # Replace task.requires()
            requires = Requires()  
            other = Requirement(OtherTask)

            def run(self):
                # Convenient access here...
                with self.other.output().open('r') as f:
                    ...

        MyTask().requires()
        {'other': OtherTask()}

    """

    def __get__(self, task, cls):
        if task is None:        #need this?
            return self
        # Bind self/task in a closure
        return  lambda: self(task)#partial(self.__call__, task)

    def __call__(self, task):
        """Returns the requirements of a task

        Assumes the task class has :class:`.Requirement` descriptors, which
        can clone the appropriate dependences from the task instance.

        :returns: requirements compatible with `task.requires()`
        :rtype: dict
        """
        #TODO: when do I need to check if task exist?
        # Search task.__class__ for Requirement instances
        # return       
        return {k:getattr(task,k) for k in dir(task.__class__) if isinstance(getattr(task.__class__,k), Requirement)}       # return dict of instances.
                

class TargetOutput:
    def __init__(self, file_pattern='{task.__class__.__name__}',
        ext='.txt', target_class=LocalTarget, **target_kwargs):

        self.file_pattern =file_pattern
        self.ext =ext
        self.target_class =target_class
        self.target_kwargs =target_kwargs


    def __get__(self, task, cls):
        if  task is None:
            return self
        return partial(self.__call__, task)

    def __call__(self, task):
        # Determine the path etc here

        updated_kwargs = {i:self.target_kwargs[i] for i in self.target_kwargs if i != 'glob' }

        if 'glob' in self.target_kwargs:
            target_path = self.file_pattern.format(task=task)
            updated_glob = self.target_kwargs['glob'].format(task=task) + self.ext.format(task=task)
            updated_kwargs['glob'] = new_glob
        else:
            target_path = (self.file_pattern.format(task=task) +
                           self.ext.format(task=task))

        path_sep = get_fs_token_paths(target_path)[0].sep
        if target_path[-1] != path_sep:
            if target_path[-1] == "/":
                target_path = target_path[:-1]
            target_path = target_path + path_sep
        fs, _, _ = get_fs_token_paths(target_path)

        return self.target_class(target_path, **updated_kwargs)
        

        