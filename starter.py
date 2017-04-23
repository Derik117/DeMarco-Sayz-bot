import logging
def start():
    try:
        logging.info("Bot start")
        import main
    except Exception as e:
        logging.info("Bot down :( \n" + str(e), exc_info=True)
        start()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s : %(levelname)s : %(message)s", filename="log.txt")
    start()