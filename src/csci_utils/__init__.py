from pkg_resources import get_distribution,DistributionNotFound


try:
    __version__ = get_distribution(__name__).version            #pragma: no cover
except DistributionNotFound:                                    #pragma: no cover
    from setuptools_scm import get_version
    import os
    __version__ = get_version(                                  
        os.path.dirname(os.path.dirname(__file__))              
    )
