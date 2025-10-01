#!/bin/bash

trabajopractico2="TP2-IDS"

if python3 --version ; then
    echo "Python instalado"
else
    echo "Debe instalar python"
    sudo apt install -y python3
fi

if pip3 --version ; then
    echo "Pip instalado"
else
    echo "Debe instalar Pip"
    sudo apt install -y python3-pip
fi

sudo apt install python3-venv

mkdir -p "$trabajopractico2"
mkdir -p "$trabajopractico2"/.venv
mkdir -p "$trabajopractico2"/static/css
mkdir -p "$trabajopractico2"/static/images
mkdir -p "$trabajopractico2"/templates 

cd "$trabajopractico2"

touch app.py

python3 -m venv .venv

. .venv/bin/activate

pip3 install Flask
pip install python-dotenv
pip install Flask-Mail

echo " --- Ambiente virtual generado --- "
