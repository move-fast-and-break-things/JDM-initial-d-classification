## JDM-initial-d classification

***!!!Программа изпользует несколько потоков и процессов, так что будьте осторожны!!!***

***!!!The program uses multiple threads and processes, so be careful!!!***

#### Installation
1. Download the bot.

2. Install virtualenv using the command
```
pip install virtualenv
```

3. Create a virtual environment by running the command in the bot folder
```
python -m v env env
```

4. In the same folder, we write the command

for Windows:
```
env\Scripts\activate
```

for Linux:
```
source env/bin/activate
```

5. Install all dependencies
```
pip install -r requirements.txt
```

6. Configure **TelegramConfig** and **BaseConfig** in the file `config.py`, just assign values directly in the script or use environment variables

7. Apply migrations for the database
```
alembic upgrade head
```

8. Run the file `main.py`
```
python main.py
```
