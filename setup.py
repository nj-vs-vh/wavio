from setuptools import setup


def get_wavio_version():
    """
    Find the value assigned to __version__ in wavio.py.

    This function assumes that there is a line of the form

        __version__ = "version-string"

    in wavio.py.  It returns the string version-string, or None if such a
    line is not found.
    """
    with open("wavio.py", "r") as f:
        for line in f:
            s = [w.strip() for w in line.split("=", 1)]
            if len(s) == 2 and s[0] == "__version__":
                return s[1][1:-1]


setup(
    name='wavio',
    version=get_wavio_version(),
    author='Warren Weckesser',
    description=("Read and write 24 bit WAV files with numpy arrays."),
    license="BSD",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    py_modules=["wavio"],
    install_requires=[
        'numpy >= 1.6.0',
    ],
)