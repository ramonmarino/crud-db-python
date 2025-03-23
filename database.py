import sqlite3

try:
    conn = sqlite3.connect('escola.db')
    # estabelece uma conexão com o banco de dados chamado escola.db

    # criar cursor
    cursor = conn.cursor()
    # ferramenta para manipular os dados.

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        curso TEXT NOT NULL,
        UNIQUE(nome, curso)
    )
    ''')

    # Criar a tabela 'cursos' se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            descricao TEXT,
            UNIQUE(nome,descricao)
        )
    ''')

    # Criar a tabela 'professores' se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            especialidade TEXT NOT NULL,
            UNIQUE (nome,especialidade)
        )
    ''')
    # inserindo multiplos alunos de uma vez
    lista_alunos = [
        ("Ramon", 29, "Historia"),
        ("Gabriel", 26, "Matematica"),
        ("Gustavo", 39, "Engenharia"),
        ("Paula", 24, "Geografia")

    ]
    # dados da Entidade professores
    professores = [
        ('João Silva', 'Matemática'),
        ('Maria Oliveira', 'Física'),
        ('Carlos Souza', 'Química'),
        ('Pedro', 'programação')
    ]

    cursos = [
        ('Engenharia de Software', 'Curso sobre desenvolvimento de sistemas e programação.'),
        ('Matemática Aplicada', 'Curso de matemática com foco em aplicações em diversas áreas.'),
        ('Física Teórica', 'Curso focado nas teorias fundamentais da física.')
    ]

    cursor.execute("DELETE FROM alunos")
    cursor.execute("DELETE FROM cursos")
    cursor.execute("DELETE FROM professores")

    # Resetando os IDs (opcional, útil para garantir que IDs sempre reiniciem do 1)
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='alunos'")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='cursos'")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='professores'")

    # Usamos executemany() para inserir todos os alunos de uma vez, preenchendo os ? com os valores das tuplas.
    cursor.executemany('''
    INSERT OR IGNORE INTO  alunos (nome,idade,curso) VALUES (?, ?, ?)
    ''', lista_alunos)

    # modificando/atualizando das de um registro especifico.
    cursor.execute('''
    UPDATE alunos SET curso = 'Educação Física' WHERE id = 1;
        
    ''')

    cursor.executemany('''
    INSERT OR IGNORE INTO professores (nome,especialidade) VALUES (?,?)
    ''', professores)

    cursor.execute('''
    DELETE FROM professores WHERE id = 4;
    ''')

    cursor.executemany('''
    INSERT OR IGNORE INTO cursos (nome, descricao) VALUES(?,?)
    ''', cursos)

    # Selecionando todos os registros da tabela alunos

    cursor.execute("SELECT * FROM alunos")
    # Obtendo os resultados
    alunos = cursor.fetchall()

    # Exibindo os alunos
    print("Alunos")
    for aluno in alunos:
        print(aluno)

    print("\n---\n")  # Separador

    cursor.execute("SELECT * FROM cursos")
    cursos = cursor.fetchall()
    print("Cursos:")
    for curso in cursos:
        print(curso)

    print("\n---\n")  # Separador

    # Consultando e exibindo todos os professores
    cursor.execute("SELECT * FROM professores")
    professores = cursor.fetchall()
    print("Professores:")
    for professor in professores:
        print(professor)

    conn.commit()
    # print("Entidades criadas com sucesso!")
    # criado o print apenas para visualizar se conexão foi feita
except sqlite3.Error as e:
    print(f"Erro ao criar tabelas: {e}")

finally:
    # fechando a conexão com banco de dados
    if conn:
        conn.close()
        print("Conexão fechada!")
