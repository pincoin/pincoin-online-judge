from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

sandbox_extension = Extension(
    name='sandbox',
    sources=['sandbox.pyx'],
    libraries=['sandbox', 'seccomp'],
    library_dirs=['clib'],
    include_dirs=['clib']
)

setup(
    name='pincoin sandbox',
    ext_modules=cythonize([
        sandbox_extension,
    ], compiler_directives={'language_level' : '3'})
)
