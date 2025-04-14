import platform
from importlib import metadata
from packaging.version import Version
from typing import List, TypedDict, Optional
from packaging.specifiers import SpecifierSet

__ALL__ = ['check_python_version', 'check_dependencies_version']


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


class DependencyNotFoundError(Exception):
    """依赖库不存在错误"""

    pass


class DependencyVersionError(Exception):
    """依赖库版本错误"""

    pass


class DependencyRule(TypedDict):
    # 必填，依赖库名称
    name: str
    # 选填，依赖库版本规则字符串，缺省时表示不限版本
    specifier: Optional[str]


def check_dependencies_version(
    rules: List[DependencyRule],
) -> None:
    """检查当前环境中的若干依赖库版本是否符合要求

    Args:
        rules (List[DependencyRule]): 依赖库版本检查规则
    """

    if rules:
        # 遍历规则，执行依赖版本检查
        for rule in rules:
            # 检查当前依赖库是否存在
            try:
                version = metadata.version(rule['name'])
            except metadata.PackageNotFoundError:
                raise DependencyNotFoundError(
                    f'Package {rule["name"]} not found'
                )

            # 若当前依赖库配置了明确的版本规则
            if rule.get('specifier'):
                # 检查当前依赖库版本是否符合明确的规则要求
                if version not in SpecifierSet(
                    rule['specifier'], prereleases=True
                ):
                    raise DependencyVersionError(
                        f'Package {rule["name"]} version must match {rule["specifier"]}'
                    )
