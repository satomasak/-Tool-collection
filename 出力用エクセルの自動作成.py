#エクセルの作成
from openpyxl import Workbook
wb = Workbook()
datash = wb.create_sheet('シート名')