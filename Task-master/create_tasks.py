#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import datetime
import sqlite3
from contextlib import closing

from tqdm import tqdm

COLORS = [
    'blue',
    'red',
    'orange',
    'green',
]

INICIOS = [
    "Estudiar sobre",
    "Leer un artículo sobre",
    "Buscar si existe alguna revista centrada en",
    "Leer un libro sobre",
    "Ver un vídeo acerca de",
    "Oir un podcast que hable de",
    "Entender el concepto de",
    "Escribir una nota sobre lo que sé de",
    "Escribir una nota sobre lo que quiero aprender de",
    "Preguntar a alguien que sepa de",
    "Dibujar un diagrama explicando",
    "Reflexionar sobre",
    "Dar un paseo y pensar en",
    "Pensar en la ducha sobre",
]

FINALES = [
    "desarrollo web",
    "protocolo HTTP",
    "lenguaje HTML 5",
    "hojas de estilo en cacada CSS",
    "Django",
    "Flask",
    "Python",
    "SQL",
    "sqlite3",
    "las Dataclasses de Python",
    "las excepciones en Python",
    "exportación e importación de datos",
    "procesadores",
    "sistemas en la nube",
    "programación asíncrona",
    "modelos Django",
    "microservicios",
    "Javascript",
    "bases de datos",
    "modelo vista/modelo/controlador",
    "modelos Entidad/Relación",
    "copias de seguridad",
    "el concepto de vista",
    "las vistas basadas en clases (CBV)",
    "el sistema de herencias de las plantillas",
    "modelos de IA",
    "bases de datos jerárquicas",
    "el framework CSS Bulma",
    "el framework CSS/JS Bootstrap",
    "Vue.js",
    "jQuery.js",
]


def random_name():
    inicio = random.choice(INICIOS)
    final = random.choice(FINALES)
    return f"{inicio} {final}"


def random_project(db):
    if random.random() >= 0.5:
        return None
    with closing(db.cursor()) as cursor:
        cursor.execute('Select id from tasks_project')
        return random.choice([
            row[0] for row in cursor.fetchall()
            ])


def random_priority():
    return random.choices('LNH', weights=[1, 4, 2])[0]


def random_color():
    return random.choice(COLORS)


def random_order():
    return random.choice(range(100))


def random_finished():
    return random.random() < 0.10


def random_due_date():
    hoy = datetime.date.today()
    days = random.randrange(-10, 92)
    return hoy + datetime.timedelta(days=days)


def nueva_tarea(db):
    sql = '''
INSERT INTO tasks_task (
    name, priority, orden, due_date, color, finished, project_id
) VALUES (?, ?, ?, ?, ?, ?, ?)
'''
    id_project = random_project(db)
    with closing(db.cursor()) as cursor:
        cursor.execute(sql, [
            random_name(),
            random_priority(),
            random_order(),
            random_due_date(),
            random_color(),
            random_finished(),
            id_project,
        ])


def main():
    with closing(sqlite3.connect('db.sqlite3')) as db:
        for _ in tqdm(range(32)):
            nueva_tarea(db)
        db.commit()


if __name__ == "__main__":
    main()
