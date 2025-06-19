@echo off
echo Iniciando o aplicativo Flask...

REM Navegue até o diretório do projeto (se necessário)
cd /D "C:\Users\Jorge Maques\Documents\Diabetes"

REM Ative o ambiente virtual (se estiver usando)
if exist venv\Scripts\activate (
    call venv\Scripts\activate
)

REM Execute o aplicativo Flask
python app.py

echo Aplicativo Flask encerrado.
pause
