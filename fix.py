import sqlite3
import re

def fix_spaces(text):
    if text is None:
        return text
    text = re.sub(r'([а-яёА-ЯЁ])(\d)', r'\1 \2', text)
    # буква после цифры (2года)
    text = re.sub(r'(\d)([а-яёА-ЯЁ])', r'\1 \2', text)
    return text

conn = sqlite3.connect("result.db")
conn.row_factory = sqlite3.Row

rows = conn.execute("SELECT [index], descr, ocoben, food, end FROM dogs").fetchall()

for row in rows:
    conn.execute("""
        UPDATE dogs SET 
            descr = ?,
            ocoben = ?,
            food = ?,
            [end] = ?
        WHERE [index] = ?
    """, (
        fix_spaces(row["descr"]),
        fix_spaces(row["ocoben"]),
        fix_spaces(row["food"]),
        fix_spaces(row["end"]),
        row["index"]
    ))

conn.commit()
conn.close()
print("Готово!")