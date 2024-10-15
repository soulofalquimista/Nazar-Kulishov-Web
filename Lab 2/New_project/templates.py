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
