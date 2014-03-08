page1_elements = [
    ('dir', 'proj_dir', '', tr('(*)Project Path:'), None),
    ('string', 'proj_name', '', tr('(*)Project Name:'), None),
    ('string', 'username', '', tr('Username:'), None),
    ('string', 'email', '', tr('E-mail:'), None),
    ('single', 'database', 'sqlite3', tr('Backend DB:'), ['postgresql', 'mysql', 'sqlite3', 'ado_mssql']),
    ('openfile', 'db_file', '', tr('DB File(only sqlite3):'), None),
    ('string', 'db_user', '', tr('DB User(not used in sqlite3):'), None),
    ('string', 'db_password', '', tr('DB Password(not used in sqlite3):'), None),
    ('string', 'db_host', '', tr('DB Host(empty string for localhost, not used in sqlite3):'), None),
    ('int', 'db_port', 0, tr('DB Port(empty string for default, not used in sqlite3):'), None),
    ('string', 'time_zone', 'America/Chicago', tr('Time Zone:'), None),
    ('single', 'language', 'en', tr('Language:'),
        [(tr('English'), 'en'),
        (tr('Simplified Chinese'), 'zh-cn'),
        (tr('Bengali'), 'bn'),
        (tr('Czech'), 'cs'),
        (tr('Welsh'), 'cy'),
        (tr('Danish'), 'da'),
        (tr('German'), 'de'),
        (tr('Spanish'), 'es'),
        (tr('French'), 'fr'),
        (tr('Galician'), 'gl'),
        (tr('Icelandic'), 'is'),
        (tr('Italian'), 'it'),
        (tr('Norwegian'), 'no'),
        (tr('Brazilian'), 'pt-br'),
        (tr('Romanian'), 'ro'),
        (tr('Russian'), 'ru'),
        (tr('Slovak'), 'sk'),
        (tr('Serbian'), 'sr'),
        (tr('Swedish'), 'sv'),
         ]),
    ('static', '_memo', tr('* is must item'), tr('Description:'), None),
    ]

notebook = [
{'title':u'Django Project Wizard', 'description':u'Create basic Django Project', 'elements':page1_elements},
]
