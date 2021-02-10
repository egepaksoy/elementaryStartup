import os

file = open('setupLog.txt', 'w+')
file = open('setupLog.txt', 'r')

if file.readline() == '\n':

    os.system('sudo apt update && sudo apt upgrade -y')
    file = open('setupLog.txt', 'w')
    file.write('update\nupgrade')
    file.close()
    os.system('shutdown -r now')

else:
    print('success')
    os.system('sudo apt install git && git clone https://github.com/btd1337/La-Sierra-Icon-Theme ~/.icons/La-Sierra')
    os.system('git clone https://github.com/btd1337/eOS-Sierra-Gtk ~/.themes/eOS-Sierra-Gtk')
    os.system('gsettings set org.gnome.desktop.interface icon-theme "La-Sierra"')
    os.system('gsettings set org.gnome.desktop.interface gtk-theme "eOS-Sierra-Gtk"')
    os.system('sudo apt install software-properties-common')
    os.system('sudo snap install code --classic')
    os.system('git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime')
    os.system('sh ~/.vim_runtime/install_awesome_vimrc.sh')
    os.system('wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -')
    os.system('sudo apt-get install apt-transport-https')
    os.system('echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list')
    os.system('sudo apt-get update')
    os.system('sudo apt-get install sublime-merge') 
    os.system('sudo apt-get install gedit -y')
    os.system('curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash')
    os.system('nvm install --lts')
    os.system('rm setupLog.txt')