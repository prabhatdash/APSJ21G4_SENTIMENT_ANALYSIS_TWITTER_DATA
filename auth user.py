import APSJ21G4_SENTIMENT_ANALYSIS_TWITTER_DATA.connector as con

def auth_user(email):
    query = "select * from reg_users;"
    con.cursor.execute(query)
    for i in con.cursor:
        if i[2]==email:
            count=1
            return count
        else:
            count=0
            return count
