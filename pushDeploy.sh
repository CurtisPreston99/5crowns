
echo "$1"
./buildAndMove.sh
git add .
git commit -m "$1"
git push
git push heroku