# When backend are updated run this script, you should run the script in the backend_flask folder
# use sudo ./update_deploy.sh to run the script
echo "restarting backend_flask service"

sudo rm backend_flask.sock
sudo systemctl stop backend_flask
sudo systemctl start backend_flask
sudo systemctl enable backend_flask
echo "Started."

echo "give sock permission"
sudo chmod 660 backend_flask.sock

echo "restart backend_flask service"
sudo systemctl restart nginx

echo "Done"
