import json
from flask import request


class Translator:
    """实现文案内容的快捷国际化相关操作"""

    def __init__(
        self,
        translations: str,
        translations_encoding: str = 'utf-8',
        root_locale: str = None,
        cookie_name: str = 'dash-i18n',
    ) -> None:
        """
        初始化 Translator 实例。

        Args:
            translations (str)：本地化配置文件路径
            translations_encoding (str)：本地化配置文件编码 Defaults to 'utf-8'.
            root_locale (str)：手动设置的根语言环境类型 Defaults to None.
            cookie_name (str)：存储当前语言环境类型的 cookie 名称 Defaults to 'dash-i18n'.

        Returns:
            None
        """

        root_locale_from_json = self.rebuild_transilations(
            translations=translations,
            translations_encoding=translations_encoding,
        )

        self.root_locale = (
            root_locale or root_locale_from_json
        )

        self.cookie_name = cookie_name

    def t(
        self, input_content: str, source_locale: str = None
    ) -> str:
        """
        文案内容国际化转换

        Args:
            input_content (str): 转换前文案内容
            source_locale (str, optional): 手动控制源语种 Defaults to None.

        Returns:
            str: 转换结果
        """

        # 确定本次翻译提取的源语种
        source_locale = source_locale or self.root_locale

        # 尝试从cookie中获取当前语种
        current_locale = request.cookies.get(
            self.cookie_name
        )

        current_locale = current_locale or self.root_locale

        assert (
            current_locale is not None
        ), '未从cookie中检测到当前语种'
        assert (
            current_locale in self.translations
        ), '检测到的当前语种不在配置信息中'

        # 尝试从已加载的配置信息中提取目标文案语种
        if source_locale != current_locale:
            match_transitions = self.translations[
                source_locale
            ].get(input_content)
            assert (
                match_transitions is not None
            ), '未从配置信息中检测到目标文案语种'
            assert (
                match_transitions.get(current_locale)
                is not None
            ), '未从配置信息中检测到目标文案语种的翻译内容'

            return match_transitions[current_locale]

        return input_content

    def rebuild_transilations(
        self,
        translations: str,
        translations_encoding: str = 'utf-8',
    ) -> str:
        """
        基于传入的本地国际化配置文件重置国际化配置参数

        Args:
            translations (str): 本地国际化配置文件路径
            translations_encoding (str, optional): 本地国际化配置文件编码. Defaults to 'utf-8'.

        Returns:
            str: 解析结果中的根语种
        """

        # 读取目标本地国际化配置文件
        with open(
            translations,
            'r',
            encoding=translations_encoding,
        ) as f:
            raw_translations = json.load(f)

        # 基于raw_translations生成多语种文案映射字典
        # 生成根语种文案映射字典
        self.translations = {
            raw_translations[
                'root_locale'
            ]: raw_translations['contents']
        }

        # 补充生成其他语种文案映射字典
        for (
            root_content,
            root_content_translations,
        ) in raw_translations['contents'].items():
            for (
                locale,
                content,
            ) in root_content_translations.items():
                if locale not in self.translations:
                    self.translations[locale] = {}
                if content not in self.translations[locale]:
                    self.translations[locale][content] = {}
                self.translations[locale][content].update(
                    {
                        raw_translations[
                            'root_locale'
                        ]: root_content,
                        **{
                            key: value
                            for key, value in root_content_translations.items()
                            if key != locale
                        },
                    }
                )

        # 更新当前可用语种列表
        self.available_locales = list(
            self.translations.keys()
        )

        # 返回当前根语种
        return raw_translations['root_locale']
