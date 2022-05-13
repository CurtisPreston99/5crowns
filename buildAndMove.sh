# build angular project
cd Crown5Frontend
ng build --prod --build-optimizer --baseHref="/static/"
cd ..
# clean out old build
rm templates/index.html
rm ./static/*
# copy angular build to served dir
cp -a ./Crown5Frontend/dist/crown5-frontend/. ./static
# copy index to to template folder
cp ./static/index.html ./templates/index.html
# remove index from static folders
rm static/index.html
