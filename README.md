# 🎮 MMORPG Board

Простая платформа объявлений для игроков MMORPG, сделанная на Django.

## 🔧 Возможности

* Регистрация и вход через email (allauth)
* Создание и редактирование объявлений
* Категории: Танки, Хилы, ДД, и др.
* Отклики на объявления
* Уведомления по email при отклике и принятии
* CKEditor для форматирования текста и загрузки изображений
* Приватная страница со своими откликами
* Пагинация и фильтрация

## 🚀 Как запустить

```bash
git clone https://github.com/TanyaDyakonova/mmorpg-board.git
cd mmorpg-board

python -m venv .venv
source .venv/bin/activate 

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Перейди в браузер: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## 🗂 Основные приложения

* `board` — основное приложение (модели, формы, шаблоны)
* `ckeditor` — редактор для форматирования и загрузки изображений


## 📌 Примечание

* Чтобы работали картинки в редакторе, нужен `enctype="multipart/form-data"` в форме и правильная настройка `MEDIA_URL` и `MEDIA_ROOT`.

---

🛠 Проект создавался в учебных целях, но легко расширяется под реальные задачи.
