import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLineEdit, QAction, QLabel
from PyQt5.QtGui import QIcon

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QGridLayout()
        self.central_widget.setLayout(self.layout)

        self.status_label = QLabel()
        self.layout.addWidget(self.status_label, 0, 0, 1, 4)
        self.status_label.setStyleSheet("font-size: 20px; padding: 5px;")

        self.input_line = QLineEdit()
        self.input_line.setFixedHeight(60)
        self.layout.addWidget(self.input_line, 1, 0, 1, 4)

        buttons = [
            ("7", self.number_button_clicked),
            ("8", self.number_button_clicked),
            ("9", self.number_button_clicked),
            ("/", self.operation_button_clicked),
            ("4", self.number_button_clicked),
            ("5", self.number_button_clicked),
            ("6", self.number_button_clicked),
            ("*", self.operation_button_clicked),
            ("1", self.number_button_clicked),
            ("2", self.number_button_clicked),
            ("3", self.number_button_clicked),
            ("-", self.operation_button_clicked),
            ("0", self.number_button_clicked),
            (".", self.number_button_clicked),
            ("=", self.calculate),
            ("+", self.operation_button_clicked),
            ("C", self.clear_input)
        ]

        row = 2
        col = 0
        for btn_text, btn_action in buttons:
            btn = QPushButton(btn_text)
            btn.clicked.connect(btn_action)
            self.layout.addWidget(btn, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('File')
        exit_action = QAction(QIcon('exit.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        with open('styles.css', 'r') as f:
            self.setStyleSheet(f.read())

        self.current_operation = ''

    def number_button_clicked(self):
        button = self.sender()
        self.input_line.setText(self.input_line.text() + button.text())
        self.current_operation += button.text()

    def operation_button_clicked(self):
        button = self.sender()
        self.input_line.setText(self.input_line.text() + " " + button.text() + " ")
        self.current_operation += " " + button.text() + " "

    def calculate(self):
        expression = self.input_line.text()
        try:
            result = eval(expression)
            self.input_line.setText(str(result))
            self.current_operation += " = " + str(result)
            self.status_label.setText(self.current_operation)
        except Exception as e:
            self.input_line.setText("Error")

    def clear_input(self):
        self.input_line.clear()
        self.current_operation = ''
        self.status_label.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
