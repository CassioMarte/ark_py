
CREATE TABLE IF NOT EXISTS 'pets' (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    uuid VARCHAR(36) UNIQUE NOT NULL, 
    name TEXT NOT NULL,
    type TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS 'people' (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    uuid VARCHAR(36) UNIQUE NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    pet_uuid VARCHAR(36) NOT NULL,
    FOREIGN KEY (pet_uuid) REFERENCES pets(uuid)
);

INSERT INTO pets (uuid, name, type)
VALUES
    ('550e8400-e29b-41d4-a716-446655440001', 'cobra', 'snake'),
    ('550e8400-e29b-41d4-a716-446655440002', 'cao', 'dog'),
    ('550e8400-e29b-41d4-a716-446655440003', 'gato', 'cat'),
    ('550e8400-e29b-41d4-a716-446655440004', 'jorgin', 'hamster'),
    ('550e8400-e29b-41d4-a716-446655440005', 'burro', 'donkey'),
    ('550e8400-e29b-41d4-a716-446655440006', 'shrek', 'ogro'),
    ('550e8400-e29b-41d4-a716-446655440007', 'belinha', 'dog');
