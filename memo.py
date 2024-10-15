#create a memory card application
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QButtonGroup, QRadioButton, QGroupBox
from random import shuffle, randint

class Question():
    def __init__(self,question, right_answer, wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = list()
question_list.append(Question("Quel sport se joue avec une balle et un filet, et où deux équipes de six joueurs s'affrontent sur un terrain rectangulaire?", 'Volleyball', 'Football', 'Tennis', 'Basketball'))
question_list.append(Question('Quel est le sport le plus populaire au monde, suivi par des millions de personnes dans tous les pays?', 'Le football', 'Le cricket', 'Le baseball', 'Le hockey sur glace'))
question_list.append(Question('Dans quel sport un athlète utilise une raquette pour frapper une balle dans un but adverse?', 'Le tennis', ' Le badminton', 'Le tennis de table', 'Le squash'))
question_list.append(Question('Quelle est la plus longue rivière du monde ?', 'Le Nil', " L'Amazone", 'Le Mississippi', 'Le Yangzi Jiang'))
question_list.append(Question('Qui a peint la Joconde ?', 'Léonard de Vinci', 'Vincent van Gogh', 'Pablo Picasso', 'Michelangelo'))
question_list.append(Question('Dans quel pays se trouve la Grande Muraille de Chine ?', 'Chine', 'Japon', 'Inde', 'Corée du Sud'))
question_list.append(Question("Quelle est la capitale de l'Australie ?", 'Canberra', 'Sydney', 'Melbourne', 'Perth'))
question_list.append(Question("Qui a découvert l'Amérique ?", 'Christophe Colomb', 'Marco Polo', 'Vasco de Gama', 'Ferdinand Magellan'))
question_list.append(Question('Quelle est la plus grande planète du système solaire ?', 'Jupiter', 'Mars', 'Saturne', 'Neptune'))
question_list.append(Question('En quelle année a eu lieu la chute du mur de Berlin ?', '1989', '1969', '1949', '1979'))


app = QApplication([])
pushbutton = QPushButton('Answer')
window = QWidget()
window.setWindowTitle('Memo Card')
question = QLabel('The most difficult question in the world!')

group_box = QGroupBox('Answer options')
option1 = QRadioButton('option1')
option2 = QRadioButton('option2')
option3 = QRadioButton('option3')
option4 = QRadioButton('option4')

radio_group = QButtonGroup()
radio_group.addButton(option1)
radio_group.addButton(option2)
radio_group.addButton(option3)
radio_group.addButton(option4)

layout1 = QHBoxLayout()
layout2 = QVBoxLayout()
layout3 = QVBoxLayout()

layout2.addWidget(option1)
layout2.addWidget(option2)
layout3.addWidget(option3)
layout3.addWidget(option4)

layout1.addLayout(layout2)
layout1.addLayout(layout3)

group_box.setLayout(layout1)



group_box2 = QGroupBox('Test result')
result = QLabel('Right or not?')
correct = QLabel('answer will be printed')
layout4 = QVBoxLayout()
layout4.addWidget(result,alignment = (Qt.AlignLeft|Qt.AlignTop))
layout4.addWidget(correct, alignment = Qt.AlignHCenter, stretch = 2)
group_box2.setLayout(layout4)

layout5 = QHBoxLayout()
layout6 = QHBoxLayout()
layout7 = QHBoxLayout()

layout5.addWidget(question, alignment = (Qt.AlignHCenter|Qt.AlignVCenter))
layout6.addWidget(group_box)
layout6.addWidget(group_box2)
group_box.hide()

layout7.addStretch(1)
layout7.addWidget(pushbutton, stretch = 2)
layout7.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout5, stretch = 2)
layout_card.addLayout(layout6, stretch = 8)
layout_card.addStretch(1)
layout_card.addLayout(layout7, stretch = 1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    group_box.hide()
    group_box2.show()
    pushbutton.setText('Next question')

def show_question():
    group_box.show()
    group_box2.hide()
    pushbutton.setText('Answer')
    radio_group.setExclusive(False)
    option1.setChecked(False)
    option2.setChecked(False)
    option3.setChecked(False)
    option4.setChecked(False)
    radio_group.setExclusive(True)

def start_test():
    if pushbutton.text() == 'Answer':
        show_result()
    else:
        show_question()

answers = [option1, option2, option3, option4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Correct')
        window.score += 1
        print('Statistiques\nTotal questions:', window.total, '\nBonne reponses:', window.score)
        print('Performance:',(window.score/window.total)*100,'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('wrong answer')
            print('Performance:',(window.score/window.total)*100,'%')

def next_queston():
    window.total += 1
    print('Statistiques\nTotal questions:', window.total, '\nBonne reponses:', window.score)
    cur_question = randint(0,len(question_list)-1)
    q = question_list[cur_question]
    ask(q)

def click_ok():
    if pushbutton.text() == 'Answer':
        check_answer()
    else:
        next_queston()
window.setLayout(layout_card)
pushbutton.clicked.connect(click_ok)
window.total = 0
window.score = 0
next_queston()
window.resize(400,300)
window.show()
app.exec_()