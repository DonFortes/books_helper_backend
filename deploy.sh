docker context use timeweb
# run at the server
docker stop alteasy_backend
docker stop ui_books
docker container rm alteasy_backend
docker container rm ui_books
docker rmi alteasy_backend
docker rmi ui_books
docker compose up -d
# return context
docker context use rootless
