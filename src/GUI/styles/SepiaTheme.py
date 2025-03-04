from .style import style


class SepiaTheme(style):
    style = style.rootStyle +"""
    * {
        background-color: #f0dec6;
        color: #000000;
     }
    """