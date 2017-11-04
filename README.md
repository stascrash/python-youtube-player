# Objective of this project
I forked the original code, and i am interested in implementing 
a media server for my video library.

i am interested in using Flask and Spyne (rpc), instead of sockets, and integrate with PyQt for some client-UI.
The goal is to have a simulated Digital Asset Management, as an entry point for TACTIC Asset Management



# Python Youtube Player
Python project to play YouTube videos through a multi-clint server and receive commands over the network 


## Description
This is a python project that uses both *pafy* and *vlc* libraries to stream videos from Youtube. It is the final project for the class *EE810 - Engineering Programming: Python* at Stevens Institute of Technology.

## Features
* Multiclient - let everyone in the network add their music to your play-list
* Play-list Management - add, pause and skip any music on your play-list
* Ad-Free

## Usage
#### Dependencies
In order to run this project, you need to install vlc (and plugins), youtube-dl and pafy. Run the following lines:
```bash
$ sudo apt-get install vlc
$ sudo apt-get install vlc-plugin-*
$ sudo pip install youtube_dl
$ sudo pip install pafy
```

See the following links for further information on the installation process:
* [Pafy Repository](https://github.com/mps-youtube/pafy)
* [VLC Bindings](https://wiki.videolan.org/Python_bindings/)

####Running the Server
Just run the server script, assigning a hostname and a port to it.
```bash
usage: 
$ python server.py [hostname] [port]

example: 
$ python server.py localhost 9999
```
####Running the Client
First, run the client script, assigning a hostname and a port to it.
```bash
usage: 
$ python client.py [hostname] [port]

example: 
$ python client.py localhost 9999
```
This will initialize the client and open a command prompt. The following commands are accepted:
* `/play`
* `/pause`
* `/next`
* `/add [YOUTUBE URL]`
* `/search [KEYWORDS]`
* `/nowplaying`
* `/playlist`
* `/queue`

See the example:
```bash
$ python client.py localhost 9999
>> /add https://www.youtube.com/watch?v=OPf0YbXqDm0
>> /add https://www.youtube.com/watch?v=YQHsXMglC9A
>> /add https://www.youtube.com/watch?v=oyEuk8j8imI
>> /play
```
