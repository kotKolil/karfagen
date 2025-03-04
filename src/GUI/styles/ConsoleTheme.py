from .style import style

class ConsoleTheme(style):
    style = style.rootStyle + """
        * {
            background-color: #181B1E;
            color: #1F822E;
        }
    """


