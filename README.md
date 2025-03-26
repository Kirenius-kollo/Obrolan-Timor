# Obrolan-Timor

Timor-Chat adalah aplikasi chat yang dikembangkan menggunakan Python, JavaScript, HTML, dan CSS.

## Fitur
- Chat real-time
- Notifikasi pesan
- User authentication
- Antarmuka pengguna yang responsif

## Instalasi

### Prasyarat
- Python 3.x
- Node.js dan npm
- Virtualenv (opsional)

### Langkah-langkah Instalasi
1. Clone repositori ini:
    ```sh
    git clone https://github.com/Kirenius-kollo/Timor-Chat.git
    cd Timor-Chat
    ```

2. Buat dan aktifkan virtual environment (opsional tapi disarankan):
    ```sh
    python -m venv env
    source env/bin/activate  # Di Windows gunakan `env\Scripts\activate`
    ```

3. Instal dependensi Python:
    ```sh
    pip install -r requirements.txt
    ```

4. Instal dependensi JavaScript:
    ```sh
    npm install
    ```

5. Jalankan aplikasi:
    ```sh
    python manage.py runserver
    ```

## Deployment

### Heroku

1. Login ke Heroku:
    ```sh
    heroku login
    ```

2. Buat aplikasi di Heroku:
    ```sh
    heroku create timor-chat
    ```

3. Deploy ke Heroku:
    ```sh
    git push heroku main
    ```

4. Migrate database di Heroku:
    ```sh
    heroku run python manage.py migrate
    ```

### AWS (Elastic Beanstalk)

1. Instal AWS CLI dan EB CLI:
    ```sh
    pip install awsebcli
    ```

2. Login ke AWS:
    ```sh
    aws configure
    ```

3. Inisialisasi aplikasi di Elastic Beanstalk:
    ```sh
    eb init -p python-3.x timor-chat
    ```

4. Buat dan deploy aplikasi:
    ```sh
    eb create timor-chat-env
    eb deploy
    ```

## CI/CD Pipeline

### GitHub Actions

 `.github/workflows/deploy.yml`

```yaml
name: Deploy to Heroku

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.x

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Deploy to Heroku
        env:
          HEROKU_API_KEY: ${{ secrets. }}6379ff29-1bb9-7d54-009f-486bf8d8a209
        run: |
          git remote add heroku https://git.heroku.com/timor-chat.git
          git push heroku main
