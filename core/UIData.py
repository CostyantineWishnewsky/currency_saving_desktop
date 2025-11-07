
from pathlib import Path
from core.patterns.SingletonMeta import SingletonMeta

from PySide6.QtGui import QPalette,QColor
from PySide6.QtGui import QPixmap, QIcon
from PySide6 import QtSvg, QtGui

class UIData(metaclass=SingletonMeta):
    def __init__(self):
        self._pallete=None

        self._min_usuall_window_width=768
        self._min_usuall_window_height=640


        self._icon_pathes={
            "logo":"./assets/icons/logo.svg"
        }

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
    
    def load_svg_icon(self,name:str)->QIcon:
        if name not in self._icon_pathes.keys():
            raise Exception(f"Icon with name {name} does not exists in icons")
        
        path=self._icon_pathes[name]
        svg_renderer = QtSvg.QSvgRenderer(path)
        image = QtGui.QImage(64, 64, QtGui.QImage.Format_ARGB32)
        image.fill(0x00000000)
        svg_renderer.render(QtGui.QPainter(image))
        pixmap = QPixmap.fromImage(image)
        return QIcon(pixmap)
