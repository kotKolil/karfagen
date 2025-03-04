from .style import style

class WhiteTheme(style):
    style = style.rootStyle +"""
        * {
            background-color: #F3F3F3;
            color: #333F3F;
        }
    """