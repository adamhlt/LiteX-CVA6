import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cva6"

# Module version
version_str = "0.0.post122"
version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post122")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post10"
data_version_tuple = (0, 0, 10)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post10")
except ImportError:
    pass
data_git_hash = "39e4bb554b6955291114f005195fdd9bf7df81f0"
data_git_describe = "v0.0-10-g087cb61"
data_git_msg = """\
commit 39e4bb554b6955291114f005195fdd9bf7df81f0
Author: Andreas Kuster <20418060+andreaskuster@users.noreply.github.com>
Date:   Fri Oct 22 10:09:07 2021 +0200

    Bender cleanup and proper cv64a/cv32a switch (#762)
    
    * Remove src file artifacts
    
    * Separate 32/64bit config into separate targets

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_cva6."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_cva6".format(f))
    return fn
