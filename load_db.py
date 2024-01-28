import sqlite3, os


def return_to_original_db():
    db = "GameDB.db3"
    db = os.path.join('data/db', db)
    con = sqlite3.connect(db)
    cur = con.cursor()

    original_user_army = cur.execute("""SELECT * FROM army WHERE id = 1""").fetchall()
    original_castle_army = cur.execute("""SELECT * FROM army WHERE id = 2""").fetchall()
    original_castle = cur.execute("""SELECT * FROM castles WHERE id = 1""").fetchall()
    original_hero = cur.execute("""SELECT * FROM heroes WHERE id = 1""").fetchall()
    original_resource = cur.execute("""SELECT * FROM user_resources WHERE id = 1""").fetchall()

    unit_name = []
    resource_name = []
    for i in range(10):
        unit = cur.execute("""SELECT unit_name FROM units WHERE id = ?""", (i + 1,)).fetchone()
        unit_name.append(unit)
    for i in range(4):
        resource = cur.execute("""SELECT name FROM resources WHERE id = ?""", (i + 1,)).fetchone()
        resource_name.append(resource)
    list_l = ['lvl', 'horse_stable', 'marketplace', 'militia', 'pennies', 'swordmans', 'knights', 'archer',
              'crossbowman', 'cleric', 'abbot', 'master_of_light_and_might', 'horseman']

    for i in range(len(unit_name)):
        a = original_user_army[0][i + 2]
        b = unit_name[i][0]
        cur.execute(f"""UPDATE army SET {unit_name[i][0]} = ? WHERE id = 3""",
                    (original_user_army[0][i + 2],))
        cur.execute(f"""UPDATE army SET {unit_name[i][0]} = ? WHERE id = 5""",
                    (original_user_army[0][i + 2],))
        cur.execute(f"""UPDATE army SET {unit_name[i][0]} = ? WHERE id = 4""",
                    (original_castle_army[0][i + 2],))
        cur.execute(f"""UPDATE army SET {unit_name[i][0]} = ? WHERE id = 6""",
                    (original_castle_army[0][i + 2],))
        cur.execute(f"""UPDATE army SET {unit_name[i][0]} = ? WHERE id = 7""",
                    (original_castle_army[0][i + 2],))
        cur.execute(f"""UPDATE army SET {unit_name[i][0]} = ? WHERE id = 8""",
                    (original_castle_army[0][i + 2],))

    for i in range(len(resource_name)):
        cur.execute(f"""UPDATE user_resources SET {resource_name[i][0]} = ? WHERE id = 2""",
                    (original_resource[0][i + 2],))
        cur.execute(f"""UPDATE user_resources SET {resource_name[i][0]} = ? WHERE id = 3""",
                    (original_resource[0][i + 2],))

    for i in range(len(list_l)):
        cur.execute(f"""UPDATE castles SET {list_l[i]} = ? WHERE id = 2""",
                    (original_castle[0][i + 2],))
        cur.execute(f"""UPDATE castles SET {list_l[i]} = ? WHERE id = 3""",
                    (original_castle[0][i + 2],))

    cur.execute("""UPDATE heroes SET motion = ?, damage = ?, protection = ?, inspiration = ?, luck = ?, 
    slot_a = ?, slot_b = ?, slot_c = ?, slot_d = ? WHERE id = 2""",
                (original_hero[0][2], original_hero[0][3], original_hero[0][4], original_hero[0][5],
                 original_hero[0][6], original_hero[0][7], original_hero[0][8], original_hero[0][9],
                 original_hero[0][10],))
    cur.execute("""UPDATE heroes SET motion = ?, damage = ?, protection = ?, inspiration = ?, luck = ?, 
        slot_a = ?, slot_b = ?, slot_c = ?, slot_d = ? WHERE id = 3""",
                (original_hero[0][2], original_hero[0][3], original_hero[0][4], original_hero[0][5],
                 original_hero[0][6], original_hero[0][7], original_hero[0][8], original_hero[0][9],
                 original_hero[0][10],))
    con.commit()
    cur.close()


