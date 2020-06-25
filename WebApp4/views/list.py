from flask import Blueprint, render_template
import pymysql as db

list_blueprint = Blueprint('list', __name__)


@list_blueprint.route('/list')
def list():
   # db접속
    conn = db.connect(
                        host='192.168.44.46',
                        user='krg',
                        password='1234',
                        db='krg',
                        charset='utf8',
    )
    # 쿼리문 실행 객체 생성
    cur = conn.cursor()
    # 쿼리문 실행
    cur.execute("SELECT * FROM `USER1`")
    conn.commit()

    users = []
    for row in cur.fetchall():
        user = {
                'uid':row[0],
                'name':row[1],
                'hp':row[2],
                'age':row[3]
        }

        users.append(user)

    # db종료
    conn.close()
    return render_template('/list.html', users=users)