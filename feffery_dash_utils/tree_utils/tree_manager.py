from typing import Union, Literal

__all__ = ['TreeManager']


class TreeManager:
    """
    针对`AntdTree`组件对应的树形数据结构进行快捷管理\n
    Manage the tree data structure of `AntdTree` easily.
    """

    @classmethod
    def update_tree_node(
        cls,
        input_object: Union[dict, list],
        node_key: str,
        new_node: dict,
        mode: Literal['replace', 'overlay'] = 'replace',
    ) -> Union[list, dict]:
        """
        对key值等于node_key的节点进行整体替换或增量更新

        Args:
            input_object (Union[dict, list]): 原始的treeData
            node_key (str): 更新目标节点key值
            new_node (dict): 更新目标节点新数据字典
            mode (Literal['replace', 'overlay'], default 'replace'): 更新模式，'replace'表示整体替换，'overlay'表示增量更新

        Returns:
            list: 完成更新后的treeData
        """

        # 检查input_object类型是否在list、dict中
        assert isinstance(
            input_object, (list, dict)
        ), 'input_object类型需为列表或字典\nthe type of input_object must be list or dict'

        if isinstance(input_object, list):
            return [
                cls.update_tree_node(
                    node, node_key, new_node, mode
                )
                for node in input_object
            ]

        elif isinstance(input_object, dict):
            if input_object.get('key') == node_key:
                if mode == 'replace':
                    return new_node
                else:
                    return {**input_object, **new_node}
            else:
                if input_object.get('children'):
                    input_object['children'] = [
                        cls.update_tree_node(
                            child, node_key, new_node, mode
                        )
                        for child in input_object[
                            'children'
                        ]
                    ]
                return input_object

    @classmethod
    def add_node_before(
        cls,
        input_object: Union[dict, list],
        node_key: str,
        new_node: dict,
    ) -> Union[list, dict]:
        """
        在key值等于node_key的节点之前插入平级新节点

        Args:
            input_object (Union[dict, list]): 原始的treeData
            node_key (str): 插入目标节点key值
            new_node (dict): 要插入的新节点数据字典

        Returns:
            dict: 完成插入后的treeData
        """

        # 检查input_object类型是否在list、dict中
        assert isinstance(
            input_object, (list, dict)
        ), 'input_object类型需为列表或字典\nthe type of input_object must be list or dict'

        if isinstance(input_object, list):
            current_layer_keys = [
                node.get('key') for node in input_object
            ]
            if node_key in current_layer_keys:
                return [
                    *input_object[
                        : current_layer_keys.index(node_key)
                    ],
                    new_node,
                    *input_object[
                        current_layer_keys.index(node_key) :
                    ],
                ]
            else:
                return [
                    cls.add_node_before(
                        node, node_key, new_node
                    )
                    for node in input_object
                ]

        elif isinstance(input_object, dict):
            if input_object.get('children'):
                input_object['children'] = (
                    cls.add_node_before(
                        input_object['children'],
                        node_key,
                        new_node,
                    )
                )

        return input_object

    @classmethod
    def add_node_after(
        cls,
        input_object: Union[dict, list],
        node_key: str,
        new_node: dict,
    ) -> Union[list, dict]:
        """
        在key值等于node_key的节点之后插入平级新节点

        Args:
            input_object (Union[dict, list]): 原始的treeData
            node_key (str): 插入目标节点key值
            new_node (dict): 要插入的新节点数据字典

        Returns:
            dict: 完成插入后的treeData
        """

        # 检查input_object类型是否在list、dict中
        assert isinstance(
            input_object, (list, dict)
        ), 'input_object类型需为列表或字典\nthe type of input_object must be list or dict'

        if isinstance(input_object, list):
            current_layer_keys = [
                node.get('key') for node in input_object
            ]
            if node_key in current_layer_keys:
                return [
                    *input_object[
                        : current_layer_keys.index(node_key)
                        + 1
                    ],
                    new_node,
                    *input_object[
                        current_layer_keys.index(node_key)
                        + 1 :
                    ],
                ]
            else:
                return [
                    cls.add_node_after(
                        node, node_key, new_node
                    )
                    for node in input_object
                ]

        elif isinstance(input_object, dict):
            if input_object.get('children'):
                input_object['children'] = (
                    cls.add_node_after(
                        input_object['children'],
                        node_key,
                        new_node,
                    )
                )

        return input_object

    @classmethod
    def delete_node(
        cls, input_object: Union[dict, list], node_key: str
    ) -> Union[list, dict]:
        """
        删除key值等于node_key的节点

        Args:
            input_object (Union[dict, list]): 原始的treeData
            node_key (str): 删除目标节点key值

        Returns:
            dict: 完成删除后的treeData
        """

        # 检查input_object类型是否在list、dict中
        assert isinstance(
            input_object, (list, dict)
        ), 'input_object类型需为列表或字典\nthe type of input_object must be list or dict'

        if isinstance(input_object, list):
            input_object = [
                (
                    {
                        **node,
                        'children': cls.delete_node(
                            node['children'], node_key
                        ),
                    }
                    if node.get('children')
                    else node
                )
                for node in input_object
                if node.get('key') != node_key
            ]

        return input_object

    @classmethod
    def get_node(
        cls, input_object: Union[dict, list], node_key: str
    ) -> Union[list, dict]:
        """
        查询key值等于node_key的节点

        Args:
            input_object (Union[dict, list]): 原始的treeData
            node_key (str): 查询目标节点key值

        Returns:
            dict: 目标节点数据字典
        """

        # 检查input_object类型是否在list、dict中
        assert isinstance(
            input_object, (list, dict)
        ), 'input_object类型需为列表或字典\nthe type of input_object must be list or dict'

        # 若当前节点为列表
        if isinstance(input_object, list):
            # 依次检查子节点
            for node in input_object:
                if node.get('key') == node_key:
                    return node
                # 否则递归检查子节点的children
                if 'children' in node:
                    found_node = cls.get_node(
                        node['children'], node_key
                    )
                    if found_node:
                        return found_node

        # 若当前节点为字典
        elif isinstance(input_object, dict):
            if input_object.get('key') == node_key:
                return input_object
            # 否则递归检查子节点的children
            if 'children' in input_object:
                return cls.get_node(
                    input_object['children'], node_key
                )
        # 若未找到则返回None
        return None
