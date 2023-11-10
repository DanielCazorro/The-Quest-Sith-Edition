import sqlite3


def inicializar_base_datos():
    with sqlite3.connect("data/records.db") as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                record INTEGER NOT NULL
            )
        """)

    conn.commit()
    conn.close()


inicializar_base_datos()


def agregar_record(nombre, record):
    conn = sqlite3.connect("data/records.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO records (nombre, record) VALUES (?, ?)", (nombre, record))

    cursor.execute("SELECT * FROM records ORDER BY record DESC")
    records_ordenados = cursor.fetchall()

    if len(records_ordenados) > 5:
        id_peor_record = records_ordenados[-1][0]
        cursor.execute("DELETE FROM records WHERE id=?", (id_peor_record,))

    conn.commit()
    conn.close()


def rec_puntuaciones():
    conn = sqlite3.connect("data/records.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM records ORDER BY record DESC")
    records = [{"id": r[0], "nombre": r[1], "record": r[2]}
               for r in cursor.fetchall()]

    conn.close()

    return records
