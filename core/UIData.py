

from core.patterns.SingletonMeta import SingletonMeta

from PySide6.QtGui import QPalette,QColor
    

class UIData(metaclass=SingletonMeta):
    def __init__(self):
        self._pallete=None

        self._min_usuall_window_width=768
        self._min_usuall_window_height=640

    def set_pallete(self,palette:QPalette)->None:
        self._pallete=palette

    def get_usuall_window_sizes(self)->(int,int):
        return (self._min_usuall_window_width,self._min_usuall_window_height)

    def get_window_bg_color(self)->QColor:
        return self._pallete.color(QPalette.Window)
    
    def get_text_color(self)->QColor:
        return self._pallete.color(QPalette.WindowText)
    
    def get_base_color(self)->QColor:
        return self._pallete.color(QPalette.Base)
    
    def get_highlight_color(self)->QColor:
        return self._pallete.color(QPalette.Highlight)
    
    def get_highlist_text_color(self)->QColor:
        return self._pallete.color(QPalette.HighlightedText)