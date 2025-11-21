from repos import VehicleRepo

import sqlite3 as sq

conn = sq.connect("./infra/renting_service.db")

conn.execute('''
    CREATE TABLE IF NOT EXISTS vehicles (
        brand TEXT,
        model TEXT,
        license_plate TEXT,
        category TEXT
    )
''')