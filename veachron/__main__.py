from veachron.persistence.postgresql.initialization import initialize_database
from veachron.application.logging import configure_logging
from veachron.presentation import main

configure_logging()
initialize_database()

if __name__ == '__main__':
    main()
