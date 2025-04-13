import platform
from packaging.version import Version

__ALL__ = ['check_python_version']


class PythonVersionError(Exception):
    """Python版本检查错误"""

    pass


def check_python_version(
    min_version: str = None, max_version: str = None
) -> None:
    """检查当前环境中的Python版本是否符合要求

    Args:
        min_version (str, optional): 要求的Python版本下限，如3.8. Defaults to None.
        max_version (str, optional): 要求的Python版本上限，如3.12. Defaults to None.
    """

    # 检查当前环境Python版本是否符合要求
    current_python_version_major, current_python_version_minor, _ = (
        platform.python_version_tuple()
    )
    # 构造当前Python版本
    current_python_version = Version(
        f'{current_python_version_major}.{current_python_version_minor}'
    )

    # 检查Python版本下限
    if min_version:
        if current_python_version < Version(min_version):
            raise PythonVersionError(
                f'Python version must be greater than or equal to {min_version}'
            )

    # 检查Python版本上限
    if max_version:
        if current_python_version > Version(max_version):
            raise PythonVersionError(
                f'Python version must be less than or equal to {max_version}'
            )
