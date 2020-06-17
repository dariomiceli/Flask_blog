from index import create_app

app = create_app()

if __name__ == "__main__":          #
    app.run(debug=True)             # dubug=True: server restarts automatically
