from .style import style

class DarkTheme(style):
    style = style.rootStyle + """
    * {
        background-color: #181B1E;
        color: #B5B5B5;
     }
    """