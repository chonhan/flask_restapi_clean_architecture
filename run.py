from application import create_app
# from dotenv import load_dotenv

# load_dotenv(dotenv_path='.flaskenv')
app = create_app()

def main():
    app.run()

if __name__ == '__main__':
    main()
