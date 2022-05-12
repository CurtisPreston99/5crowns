cd Crown5Frontend
ng build --prod --build-optimizer --baseHref="/static/"
cd ..
rm templates/index.html
rm ./static/*
cp -a ./Crown5Frontend/dist/crown5-frontend/. ./static
cp ./static/index.html ./templates/index.html
rm static/index.html
