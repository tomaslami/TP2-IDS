#!/bin/bash

ENV_FILE=".env"

while true; do
    read -p "Ingrese el correo: " correo1
    read -p "Repita el correo: " correo2
    [ "$correo1" = "$correo2" ] && break
    echo "Los correos no coinciden. Intentea de nuevo."
done

MAIL_USERNAME="$correo1"


while true; do
    read -s -p "Ingrese la contrasena: " contrasena1
    echo
    read -s -p "Repita la contrasena: " contrasena2
    echo
    [ "$contrasena1" = "$contrasena2" ] && break
    echo "Las contraseñas no coinciden. Intenta de nuevo."
done
MAIL_PASSWORD="$contrasena1"

MAIL_DEFAULT_SENDER="$MAIL_USERNAME"

# Crear archivo .env (sobrescribe si ya existe)
cat > "$ENV_FILE" <<EOF
MAIL_SERVER="smtp.gmail.com"
MAIL_PORT="587"
MAIL_USE_TLS="True"
MAIL_USE_SSL="False"
MAIL_USERNAME="$MAIL_USERNAME"
MAIL_PASSWORD="$MAIL_PASSWORD"
MAIL_DEFAULT_SENDER="$MAIL_DEFAULT_SENDER"
EOF

echo "Archivo .env creado en: $(pwd)/$ENV_FILE"
