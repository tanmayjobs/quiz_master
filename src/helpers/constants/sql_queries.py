class SQLQueries:
    CREATE_AUTH_TABLE = """
        CREATE TABLE IF NOT EXISTS `auth` (
            `id` varchar(255) NOT NULL,
            `username` varchar(255) NOT NULL,
            `hash_password` varchar(255) NOT NULL,
            `user_role` enum('0','1','2') NOT NULL,
            PRIMARY KEY (`id`),
            UNIQUE KEY `username` (`username`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    """
    CREATE_QUIZ_TABLE = """
        CREATE TABLE IF NOT EXISTS `quizzes` (
            `id` varchar(255) NOT NULL,
            `quiz_name` varchar(30) NOT NULL,
            `creator_id` varchar(255),
            PRIMARY KEY (`id`),
            UNIQUE KEY `quiz_name` (`quiz_name`),
            KEY `creator_id` (`creator_id`),
            CONSTRAINT `quizzes_ibfk_1` FOREIGN KEY (`creator_id`) REFERENCES `auth` (`id`) ON DELETE SET NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    """
    CREATE_QUESTION_TABLE = """
        CREATE TABLE IF NOT EXISTS `questions` (
            `id` varchar(255) NOT NULL,
            `question_text` varchar(255) NOT NULL,
            `quiz_id` varchar(255) NOT NULL,
            PRIMARY KEY (`id`),
            KEY `quiz_id` (`quiz_id`),
            CONSTRAINT `questions_ibfk_1` FOREIGN KEY (`quiz_id`) REFERENCES `quizzes` (`id`) ON DELETE CASCADE
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    """
    CREATE_OPTION_TABLE = """
        CREATE TABLE IF NOT EXISTS `options` (
            `id` varchar(255) NOT NULL,
            `option_text` varchar(255) NOT NULL,
            `is_correct` tinyint(1) NOT NULL,
            `question_id` varchar(255) NOT NULL,
            PRIMARY KEY (`id`),
            KEY `question_id` (`question_id`),
            CONSTRAINT `options_ibfk_1` FOREIGN KEY (`question_id`) REFERENCES `questions` (`id`) ON DELETE CASCADE
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    """
    CREATE_QUIZ_SCORE_TABLE = """
        CREATE TABLE IF NOT EXISTS `score_table` (
            `id` varchar(255) NOT NULL,
            `user_id` varchar(255),
            `quiz_id` varchar(255),
            `score` decimal(3,2) NOT NULL,
            `played_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (`id`),
            KEY `user_id` (`user_id`),
            KEY `quiz_id` (`quiz_id`),
            CONSTRAINT `score_table_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `auth` (`id`) ON DELETE SET NULL,
            CONSTRAINT `score_table_ibfk_2` FOREIGN KEY (`quiz_id`) REFERENCES `quizzes` (`id`) ON DELETE SET NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    """
    CREATE_TYPE_TABLE = """
        CREATE TABLE IF NOT EXISTS `tags` (
            `id` varchar(255) NOT NULL,
            `tag_name` varchar(20) NOT NULL,
            PRIMARY KEY (`id`),
            UNIQUE KEY `tag_name` (`tag_name`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    """
    CREATE_QUIZ_TYPE_MAPPING_TABLE = """
        CREATE TABLE IF NOT EXISTS `quiz_tags` (
            `id` varchar(255) NOT NULL,
            `quiz_id` varchar(255) NOT NULL,
            `tag_id` varchar(255) NOT NULL,
            PRIMARY KEY (`id`),
            KEY `quiz_id` (`quiz_id`),
            KEY `tag_id` (`tag_id`),
            CONSTRAINT `quiz_tags_ibfk_1` FOREIGN KEY (`quiz_id`) REFERENCES `quizzes` (`id`) ON DELETE CASCADE,
            CONSTRAINT `quiz_tags_ibfk_2` FOREIGN KEY (`tag_id`) REFERENCES `tags` (`id`) ON DELETE CASCADE
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    """

    GET_USER_BY_ID = """
        SELECT * FROM auth
        WHERE id = %s;
    """
    GET_QUIZ_BY_ID = """
        SELECT * FROM quizzes
        WHERE id = %s;
    """
    GET_QUESTION_BY_ID = """
        SELECT
        questions.id as question_id,
        questions.question_text as question_text,
        quizzes.id as quiz_id,
        quizzes.creator_id as creator_id
        FROM questions
        INNER JOIN quizzes ON quizzes.id = questions.quiz_id
        WHERE questions.id = %s;
    """

    GET_ALL_TAGS = "SELECT * FROM tags;"
    CREATE_TAG = """
        INSERT INTO tags (id, tag_name)
        VALUES (%s, %s);
    """
    GET_TAG = """
        SELECT * FROM tags
        WHERE id = %s;
    """
    REMOVE_TAG = """
        DELETE FROM tags
        WHERE id = %s;
    """
    UPDATE_TAG = """
        UPDATE tags
        SET tag_name = %s
        WHERE id = %s;
    """
    ADD_QUIZ_TAG = """
        INSERT INTO quiz_tags(id, quiz_id, tag_id)
        VALUES(%s, %s, %s);
    """
    REMOVE_QUIZ_TAG = """
        DELETE FROM quiz_tags
        WHERE quiz_id = %s AND tag_id = %s;
    """

    GET_RECORDS = """
        SELECT * FROM score_table
        WHERE {};
    """

    GET_ALL_USERS = """
        SELECT * FROM auth
        WHERE user_role != 0;
    """
    GET_USER = """
        SELECT * FROM auth
        WHERE username = %s;
    """
    ADD_USER = """
        INSERT INTO auth(id, username, hash_password, user_role)
        VALUES(%s, %s, %s, %s);
    """
    REMOVE_USER = """
        DELETE FROM authentication
        WHERE id = %s;
    """

    ADD_QUIZ = """
        INSERT INTO quizzes(id, quiz_name, creator_id)
        VALUES(%s, %s, %s);
    """
    ADD_QUESTION = """
        INSERT INTO questions
        VALUES(%s, %s, %s);
    """
    UPDATE_QUESTION = """
        UPDATE questions
        SET question_text = %s
        WHERE id = %s;
    """
    ADD_OPTION = """
        INSERT INTO options
        VALUES(%s, %s, %s, %s);
    """
    UPDATE_OPTION = """
        UPDATE options
        SET option_text = %s, is_correct = %s
        WHERE id = %s;
    """
    REMOVE_QUIZ = """
        DELETE FROM quizzes
        WHERE id = %s and creator_id = %s;
    """

    GET_QUIZ = """
        SELECT
        quiz.id,
        quiz.quiz_name,
        quiz.creator_id,
        auth.username as creator_name,
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
        WHERE quiz.id = %s
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
        WHERE question.quiz_id = %s
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
        WHERE question.quiz_id = %s
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
        WHERE question.id = %s
        GROUP BY question.id;
    """

    REMOVE_QUESTION = """
        DELETE FROM questions
        WHERE id = %s;
    """
    REMOVE_OPTION_BY_QUESTION = """
        DELETE FROM options
        WHERE question_id = %s;
    """
    REMOVE_OPTION = """
        DELETE FROM options
        WHERE id = %s;
    """
    CAN_MODIFY_OPTION = """
        SELECT creator_id
        FROM options
        INNER JOIN questions ON questions.id = options.question_id
        INNER JOIN quizzes ON quizzes.id = questions.quiz_id
        WHERE options.id = %s;
    """

    GET_ALL_QUIZZES = """
        SELECT
        quiz.id as quiz_id,
        quiz.quiz_name as quiz_name,
        quiz.creator_id as creator_id,
        auth.username as creator_name,
        GROUP_CONCAT(
          json_object(
              'tag_id', tag.id,
              'tag_name', tag.tag_name
          )
        ) as tags
        FROM quizzes AS quiz
        INNER JOIN auth AS auth ON quiz.creator_id = auth.id
        LEFT JOIN quiz_tags AS quiz_tag ON quiz_tag.quiz_id = quiz.id
        LEFT JOIN tags AS tag ON tag.id = quiz_tag.tag_id
        GROUP BY quiz.id;
    """
    FILTER_ALL_QUIZZES = """
        SELECT
        quiz.id as quiz_id,
        quiz.quiz_name as quiz_name,
        quiz.creator_id as creator_id,
        auth.username as creator_name,
        GROUP_CONCAT(
          json_object(
              'tag_id', tag.id,
              'tag_name', tag.tag_name
          )
        ) as tags
        FROM quizzes AS quiz
        INNER JOIN auth AS auth ON quiz.creator_id = auth.id
        LEFT JOIN quiz_tags AS quiz_tag ON quiz_tag.quiz_id = quiz.id
        LEFT JOIN tags AS tag ON tag.id = quiz_tag.tag_id
        WHERE quiz.is_deleted = False
        AND (quiz.quiz_name LIKE %s OR tag.tag_name LIKE %s)
        GROUP BY quiz.id;
    """
