
echo "$1"
git add .
git commit -m "$1"
git push
git push heroku