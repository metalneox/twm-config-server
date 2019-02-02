#!/bin/python

from flask import Flask, jsonify,abort

app = Flask(__name__)

themes = [
    {
    "id": 1, 
    "title": "metalneox-i3",
    "git": "https://github.com/metalneox/dotfiles.git", 
    "description": "Configuration i3wm ", 
    "distro" : "Arch",
    "package": ["i3-wm","i3-gaps","i3blocks","i3status","zsh","fish","zsh-theme-powerlevel9k","ttf-dejavu","curl","ranger","termite","rofi","otf-font-awesome","ttf-font-awesome","ttf-ubuntu-font-family","ttf-hack","gifsicle","dunst","feh","compton","scrot","zsh-autosuggestions","papirus-icon-theme","udiskie","mpv","neofetch","newsboat"],
    "community": ["cava","polybar","shantz-xwinwrap-bzr","yay","mkinitcpio-openswap","ckbcomp"] 
    },
    #Theme not tested
    {
    "id": 2, 
    "title": "desi-notebook",
    "git": "https://github.com/FrancescoDeSimone/dotsNotebook.git", 
    "description": "Configuration Desi", 
    "distro" : "Arch",
    "package": ["i3-wm","i3-gaps","i3status","zsh"],
    "community": ["cava","polybar",""] 
    }
]

@app.route('/api/v1.0/list/', methods=['GET'])
def list():
    return jsonify(themes)

@app.route('/api/v1.0/themes/<int:theme_id>', methods=['GET'])
def get_theme(theme_id):
    theme = [theme for theme in themes if theme['id'] == theme_id]
    if len(theme) == 0:
        abort(404)
    return jsonify({'theme': theme[0]})


if __name__ == '__main__':
    app.run(debug=True)

