import openpyxl
import os

class ExcelReader:

    # 读取excel文件中的内容。返回list。如果excel有标题，则把标题与其他行封装成字典
    def __init__(self, excel, sheet= 'sheet1', title_line=True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError('文件不存在！')
        self.sheet = sheet
        self.title_line = title_line
        self._data = list()

    @property
    def data(self):
        if not self._data:

            workbook = openpyxl.load_workbook(self.excel)
            # s = workbook.get_sheet_by_name(sheet_name)这种方式已经弃用，不建议使用

            sheet = workbook[self.sheet]
            for row in sheet.rows:
                row_list = []
                for cell in row:  # 直接从行中取每个cell
                    row_list.append(cell.value)
                self._data.append(row_list)

            if self.title_line:
                data2 = []
                title = (self._data)[0]
                for i in range(1, len(self._data)):

                    # 非标题行与首行组成dict，拼到data2中
                    data2.append(dict(zip(title, (self._data)[i])))
                self._data = data2

        return self._data


if __name__ == '__main__':

    e = '/Users/haroldrain/project/test_fly/data/baidu.xlsx'

    reader = ExcelReader(e,sheet = 'sheet1', title_line= True)
    print(reader.data)
