from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Хранилище для отзывов (в памяти)
feedbacks = []

# Главная страница с формой
@app.route('/')
def index():
    return render_template('index.html')  # Отображаем главную страницу с формой

# Обработка формы и добавление отзыва
@app.route('/submit', methods=['POST'])
def submit_feedback():
    # Получаем данные из формы
    name = request.form.get('name')
    message = request.form.get('message')

    # Проверяем, что поля заполнены
    if name and message:
        feedbacks.append({'name': name, 'message': message})  # Сохраняем отзыв в списке
        return redirect(url_for('show_feedbacks'))  # Перенаправляем на страницу с отзывами
    else:
        return "Please fill in all fields", 400  # Возвращаем ошибку, если поля не заполнены

# Страница для отображения всех отзывов
@app.route('/feedbacks')
def show_feedbacks():
    return render_template('feedbacks.html', feedbacks=feedbacks)  # Передаем отзывы в шаблон

if __name__ == '__main__':
    app.run(debug=True)  # Запускаем приложение в режиме отладки