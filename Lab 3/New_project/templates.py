<h1>Статті</h1>
<a href="{% url 'add_article' %}">Додати статтю</a>
<ul>
    {% for article in articles %}
    <li>
        <h2>{{ article.title }}</h2>
        <p>{{ article.content }}</p>
        <a href="{% url 'delete_article' article.id %}">Видалити</a>
    </li>
    {% endfor %}
</ul>

<h1>Додати статтю</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Зберегти</button>
</form>

<h1>Реєстрація</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Зареєструватися</button>
</form>

<h1>Редагувати статтю</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Зберегти зміни</button>
</form>

<h1>{{ article.title }}</h1>
<p>{{ article.content }}</p>

<h2>Коментарі:</h2>
<ul>
    {% for comment in comments %}
    <li>{{ comment.author }}: {{ comment.content }} ({{ comment.created_at }})</li>
    {% endfor %}
</ul>

<h3>Залишити коментар:</h3>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Надіслати</button>
</form>

<head>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
</head>
