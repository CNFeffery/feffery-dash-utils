from pprint import pprint
from feffery_dash_utils.tree_utils import TreeManager


if __name__ == '__main__':
    # 示例树形数据
    demo_tree = [
        {
            'title': '节点1',
            'key': '节点1',
            'children': [
                {
                    'title': '节点1-1',
                    'key': '节点1-1',
                    'children': [
                        {
                            'title': '节点1-1-1',
                            'key': '节点1-1-1',
                        },
                        {
                            'title': '节点1-1-2',
                            'key': '节点1-1-2',
                        },
                    ],
                }
            ],
        },
        {'title': '节点2', 'key': '节点2'},
    ]

    print('原始数据结构：')
    pprint(demo_tree)

    print('节点更新测试：')
    pprint(
        TreeManager.update_tree_node(
            demo_tree,
            '节点1-1',
            {'title': '节点1-1', 'key': '节点1-1'},
        )
    )

    print('节点增量更新测试：')
    pprint(
        TreeManager.update_tree_node(
            demo_tree,
            '节点1-1',
            {'title': '节点1-1new'},
            'overlay',
        )
    )

    print('节点前置新增测试：')
    pprint(
        TreeManager.add_node_before(
            demo_tree,
            '节点1-1',
            {'title': '节点1-0', 'key': '节点1-0'},
        )
    )

    print('节点后置新增测试：')
    pprint(
        TreeManager.add_node_after(
            demo_tree,
            '节点1-1',
            {'title': '节点1-2', 'key': '节点1-2'},
        )
    )

    print('节点删除测试：')
    pprint(TreeManager.delete_node(demo_tree, '节点2'))

    print('节点查询测试：')
    pprint(TreeManager.get_node(demo_tree, '节点1-1'))

    print('不存在节点查询测试：')
    pprint(TreeManager.get_node(demo_tree, '节点1-666'))

    print('节点查询+节点增量更新测试：')
    pprint(
        TreeManager.update_tree_node(
            demo_tree,
            '节点1-1',
            {
                'children': [
                    *TreeManager.get_node(
                        demo_tree, '节点1-1'
                    )['children'],
                    {
                        'title': '节点1-1-3',
                        'key': '节点1-1-3',
                    },
                ]
            },
            'overlay',
        )
    )
