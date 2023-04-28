from fbs_runtime.application_context.PySide6 import ApplicationContext
from PySide6.QtWidgets import QMainWindow

import sys

from package.main_window import MainWindow

class AppContext(ApplicationContext):
    def run(self):
        main_window = MainWindow(ctx=appctxt)
        main_window.show()
        return self.app.exec()


if __name__ == '__main__':
    appctxt = AppContext()
    sys.exit(appctxt.run())