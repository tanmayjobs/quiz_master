class SQLQueries:
    CREATE_TOKEN_TABLE = """
    CREATE TABLE IF NOT EXISTS tokens (
        token_pair_id TEXT PRIMARY KEY,
        user_id TEXT NOT NULL,
        exp TEXT NOT NULL
    );
    """
    CREATE_AUTH_TABLE = """
        CREATE TABLE IF NOT EXISTS auth (
            id TEXT PRIMARY KEY,
            username TEXT NOT NULL,
            hash_password TEXT NOT NULL,
            user_role INTEGER NOT NULL CHECK (user_role IN (0, 1, 2)),
            UNIQUE (username)
        );
    """
    CREATE_QUIZ_TABLE = """
        CREATE TABLE IF NOT EXISTS quizzes (
            id TEXT PRIMARY KEY,
            quiz_name TEXT NOT NULL,
            creator_id TEXT,
            FOREIGN KEY (creator_id) REFERENCES auth (id) ON DELETE SET NULL
        );
    """
    CREATE_QUESTION_TABLE = """
        CREATE TABLE IF NOT EXISTS questions (
            id TEXT PRIMARY KEY,
            question_text TEXT NOT NULL,
            quiz_id TEXT NOT NULL,
            FOREIGN KEY (quiz_id) REFERENCES quizzes (id) ON DELETE CASCADE
        );
    """
    CREATE_OPTION_TABLE = """
        CREATE TABLE IF NOT EXISTS options (
            id TEXT PRIMARY KEY,
            option_text TEXT NOT NULL,
            is_correct INTEGER NOT NULL CHECK (is_correct IN (0, 1)),
            question_id TEXT NOT NULL,
            FOREIGN KEY (question_id) REFERENCES questions (id) ON DELETE CASCADE
        );
    """
    CREATE_QUIZ_SCORE_TABLE = """
        CREATE TABLE IF NOT EXISTS score_table (
            id TEXT PRIMARY KEY,
            user_id TEXT,
            quiz_id TEXT,
            score REAL NOT NULL,
            played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES auth (id) ON DELETE SET NULL,
            FOREIGN KEY (quiz_id) REFERENCES quizzes (id) ON DELETE SET NULL
        );
    """
    CREATE_TYPE_TABLE = """
        CREATE TABLE IF NOT EXISTS tags (
            id TEXT PRIMARY KEY,
            tag_name TEXT NOT NULL UNIQUE
        );
    """
    CREATE_QUIZ_TYPE_MAPPING_TABLE = """
        CREATE TABLE IF NOT EXISTS quiz_tags (
            id TEXT PRIMARY KEY,
            quiz_id TEXT NOT NULL,
            tag_id TEXT NOT NULL,
            FOREIGN KEY (quiz_id) REFERENCES quizzes (id) ON DELETE CASCADE,
            FOREIGN KEY (tag_id) REFERENCES tags (id) ON DELETE CASCADE
        );
    """

    GET_USER_BY_ID = "SELECT * FROM auth WHERE id = ?;"
    GET_QUIZ_BY_ID = "SELECT * FROM quizzes WHERE id = ?;"
    GET_QUESTION_BY_ID = """
        SELECT
        questions.id AS question_id,
        questions.question_text AS question_text,
        quizzes.id AS quiz_id,
        quizzes.creator_id AS creator_id
        FROM questions
        INNER JOIN quizzes ON quizzes.id = questions.quiz_id
        WHERE questions.id = ?;
    """

    LOAD_TOKEN = "SELECT * FROM tokens WHERE token_pair_id = ?;"
    SAVE_TOKEN = "INSERT INTO tokens VALUES (?, ?, ?);"

    GET_ALL_TAGS = "SELECT * FROM tags;"
    CREATE_TAG = "INSERT INTO tags (id, tag_name) VALUES (?, ?);"
    GET_TAG = "SELECT * FROM tags WHERE id = ?;"
    REMOVE_TAG = "DELETE FROM tags WHERE id = ?;"
    UPDATE_TAG = "UPDATE tags SET tag_name = ? WHERE id = ?;"
    ADD_QUIZ_TAG = "INSERT INTO quiz_tags (id, quiz_id, tag_id) VALUES (?, ?, ?);"
    REMOVE_QUIZ_TAG = "DELETE FROM quiz_tags WHERE quiz_id = ? AND tag_id = ?;"

    GET_RECORDS = "SELECT * FROM score_table WHERE {};"

    GET_ALL_USERS = "SELECT * FROM auth WHERE user_role != 0;"
    GET_USER = "SELECT * FROM auth WHERE username = ?;"
    ADD_USER = "INSERT INTO auth (id, username, hash_password, user_role) VALUES (?, ?, ?, ?);"
    REMOVE_USER = "DELETE FROM auth WHERE id = ?;"

    ADD_QUIZ = "INSERT INTO quizzes (id, quiz_name, creator_id) VALUES (?, ?, ?);"
    ADD_QUESTION = "INSERT INTO questions VALUES (?, ?, ?);"
    UPDATE_QUESTION = "UPDATE questions SET question_text = ? WHERE id = ?;"
    ADD_OPTION = "INSERT INTO options VALUES (?, ?, ?, ?);"
    UPDATE_OPTION = "UPDATE options SET option_text = ?, is_correct = ? WHERE id = ?;"
    REMOVE_QUIZ = "DELETE FROM quizzes WHERE id = ? AND creator_id = ?;"

    GET_QUIZ = """
        SELECT
        quiz.id,
        quiz.quiz_name,
        quiz.creator_id,
        auth.username AS creator_name,
        GROUP_CONCAT(
            json_object(
                'tag_id', tag.id,
                'tag_name', tag.tag_name
            )
        ) AS tags
        FROM quizzes AS quiz
        INNER JOIN auth AS auth ON quiz.creator_id = auth.id
        LEFT JOIN quiz_tags AS quiz_tag ON quiz_tag.quiz_id = quiz.id
        LEFT JOIN tags AS tag ON tag.id = quiz_tag.tag_id
        WHERE quiz.id = ?
        GROUP BY quiz.id;
    """
    GET_QUESTIONS_AS_CREATOR = """
        SELECT
        question.id AS question_id,
        question.question_text AS question_text,
        GROUP_CONCAT(
            json_object(
                'id', options.id,
                'option', options.option_text,
                'is_correct', options.is_correct
            )
        ) AS options
        FROM questions AS question
        INNER JOIN options ON question.id = options.question_id
        WHERE question.quiz_id = ?
        GROUP BY question.id;
    """
    GET_QUESTIONS_AS_PLAYER = """
        SELECT
        question.id AS question_id,
        question.question_text AS question_text,
        GROUP_CONCAT(
            json_object(
                'id', options.id,
                'option', options.option_text
            )
        ) AS options
        FROM questions AS question
        INNER JOIN options ON question.id = options.question_id
        WHERE question.quiz_id = ?
        GROUP BY question.id;
    """
    GET_QUIZ_QUESTION = """
        SELECT
        question.id AS question_id,
        question.question_text AS question_text,
        GROUP_CONCAT(
            json_object(
                'id', options.id,
                'option', options.option_text,
                'is_correct', options.is_correct
            )
        ) AS options
        FROM questions AS question
        INNER JOIN options ON question.id = options.question_id
        WHERE question.id = ?
        GROUP BY question.id;
    """

    REMOVE_QUESTION = "DELETE FROM questions WHERE id = ?;"
    REMOVE_OPTION_BY_QUESTION = "DELETE FROM options WHERE question_id = ?;"
    REMOVE_OPTION = "DELETE FROM options WHERE id = ?;"
    CAN_MODIFY_OPTION = """
        SELECT creator_id
        FROM options
        INNER JOIN questions ON questions.id = options.question_id
        INNER JOIN quizzes ON quizzes.id = questions.quiz_id
        WHERE options.id = ?;
    """

    GET_ALL_QUIZZES = """
        SELECT
        quiz.id AS quiz_id,
        quiz.quiz_name AS quiz_name,
        quiz.creator_id AS creator_id,
        auth.username AS creator_name,
        GROUP_CONCAT(
          json_object(
              'tag_id', tag.id,
              'tag_name', tag.tag_name
          )
        ) AS tags
        FROM quizzes AS quiz
        INNER JOIN auth AS auth ON quiz.creator_id = auth.id
        LEFT JOIN quiz_tags AS quiz_tag ON quiz_tag.quiz_id = quiz.id
        LEFT JOIN tags AS tag ON tag.id = quiz_tag.tag_id
        GROUP BY quiz.id;
    """
    FILTER_ALL_QUIZZES = """
        SELECT
        quiz.id AS quiz_id,
        quiz.quiz_name AS quiz_name,
        quiz.creator_id AS creator_id,
        auth.username AS creator_name,
        GROUP_CONCAT(
          json_object(
              'tag_id', tag.id,
              'tag_name', tag.tag_name
          )
        ) AS tags
        FROM quizzes AS quiz
        INNER JOIN auth AS auth ON quiz.creator_id = auth.id
        LEFT JOIN quiz_tags AS quiz_tag ON quiz_tag.quiz_id = quiz.id
        LEFT JOIN tags AS tag ON tag.id = quiz_tag.tag_id
        WHERE quiz.quiz_name LIKE ? OR tag.tag_name LIKE ?
        GROUP BY quiz.id;
    """

    GET_QUESTION_IDS = "SELECT id AS question_id FROM questions WHERE quiz_id = ?;"
    GET_ALL_OPTIONS_IDS = """
        SELECT * FROM options
        INNER JOIN questions ON questions.id = options.question_id
        WHERE questions.quiz_id = ?;
    """

    ADD_SCORE = "INSERT INTO score_table (id, user_id, quiz_id, score) VALUES (?, ?, ?, ?);"
