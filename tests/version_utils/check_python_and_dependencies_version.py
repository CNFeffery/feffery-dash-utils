import sys

sys.path.append('../..')

from feffery_dash_utils.version_utils import (
    check_python_version,
    check_dependencies_version,
)

if __name__ == '__main__':
    check_python_version(min_version='3.8', max_version='3.12')

    check_dependencies_version(
        rules=[{'name': 'dash', 'specifier': '>=2.18.2'}]
    )
