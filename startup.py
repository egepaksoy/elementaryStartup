import os

select = input('işlem seçin \n1-Update upgrade\n2-Download')
if int(select) == 1:

    os.system('sudo apt-get update && sudo apt-get upgrade -y')
    os.system('shutdown -r now')

if int(select) == 2:
    print('success')

    os.system('sudo apt-get install software-properties-common -y')
    os.system('sudo apt-get install apt-get-transport-https -y')
    os.system('sudo apt-get install gedit -y')


    os.system('sudo snap install code --classic')


    os.system('sudo apt-get install git -y')
    os.system('git clone https://github.com/btd1337/La-Sierra-Icon-Theme ~/.icons/La-Sierra')
    os.system('git clone https://github.com/btd1337/eOS-Sierra-Gtk ~/.themes/eOS-Sierra-Gtk')
    os.system('gsettings set org.gnome.desktop.interface icon-theme "La-Sierra"')
    os.system('gsettings set org.gnome.desktop.interface gtk-theme "eOS-Sierra-Gtk"')


    os.system('sudo apt-get install vim -y')
    os.system('git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime')
    os.system('sh ~/.vim_runtime/install_awesome_vimrc.sh')


    os.system('wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-get-key add -')
    os.system('echo "deb https://download.sublimetext.com/ apt-get/stable/" | sudo tee /etc/apt-get/sources.list.d/sublime-text.list')
    os.system('sudo apt-get install sublime-merge -y')


    os.system('curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.34.0/install.sh | bash')
    os.system('export NVM_DIR="$HOME/.nvm"\n[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"\n[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"')
    os.system('nvm install --lts')


    os.system('sudo apt-get install python3-pip -y')
    os.system('sudo pip3 install virtualenv')


    os.system('sudo apt install software-properties-common')
    os.system('sudo add-apt-repository ppa:philip.scott/elementary-tweaks && sudo apt install elementary-tweaks')


    os.system('wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -')
    os.system('sudo apt-get install apt-transport-https -y')
    os.system('echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list')
    os.system('sudo apt-get update && apt-get install sublime-merge -y')

    os.system('sudo apt-get update')
    os.system('sudo apt-get upgrade -y')
    os.system('echo "indirmen gereken birkac uygulama kaldı bunlar Discord Zoom Telegram ScreenRec Firefox fira code"')


