from cx_Freeze import setup, Executable

includefiles=[
        "assets",
        "jdata",
        "samples",
        "build.py",
        "license.txt",
        "readme.md"
    ]

setup(
    name="karfagen",
    version="0.1",
    author = "treska",
    description="Karfagen - open src fb2 reader",
    executables=[
        Executable(
            "app.pyw",
            icon="./assets/karfagen.ico",
            base="Win32GUI"
        )
    ],
    options={
        'build_exe': {
            'include_files': includefiles
        }
    }
)
