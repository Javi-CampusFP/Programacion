#!/bin/bash
repositories=("LM.git" "BBDD.git" "Programacion.git")
github="https://github.com/JaviBC-CampusFP/"
for repo in "${repositories[@]}"; do
    repoFinal="${github}${repo}"
    finalDirectory="${repo%.git}"

    cd $finalDirectory
    git pull
    if git status --porcelain | grep -q '.'; then
        echo "Se detectaron cambios en $finalDirectory"
        git add .

        echo "Introduce el mensaje de commit:"
        read -r mensaje

        git commit -m "$mensaje"
        git push
        echo "Cambios subidos correctamente."
    else
        echo "$finalDirectory está limpio, nada que hacer."
    fi
    cd ..
done
echo "Operación realizada con éxito"
