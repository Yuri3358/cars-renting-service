import sqlite3 as sq

conn = sq.connect("./infra/renting_service.db",  detect_types=sq.PARSE_DECLTYPES | sq.PARSE_COLNAMES)

conn.execute('''
    CREATE TABLE IF NOT EXISTS vehicles (
        brand TEXT,
        model TEXT,
        license_plate TEXT,
        category TEXT,
        daily_rent REAL
    )
''')

conn.execute('''
    CREATE TABLE IF NOT EXISTS rentings (
        renting_id TEXT,
        license_plate TEXT,
        client_id TEXT,
        start DATE,
        end DATE
    )
''')