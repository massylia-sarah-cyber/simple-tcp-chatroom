MULTI-USER CHAT APPLICATION

A simple real-time chat application built with Python sockets that allows multiple users to communicate simultaneously in a single chat room.

FEATURES

Real-time messaging - Instant message delivery to all connected users

Multi-user support - Multiple clients can connect simultaneously

Nickname system - Each user chooses their own display name

Broadcast messaging - Every message is visible to all connected users

Connection notifications - See when users join or leave the chat

Simple terminal interface - Easy to use command-line interface

GETTING STARTED

Prerequisites

Python 3.x installed on your system

No additional libraries required (uses only built-in modules)

Installation

Clone the repository:
git clone https://github.com/yourusername/chat-application.git
cd chat-application

No installation needed - the application uses only Python's standard library!

Running the Application

Start the Server
python server.py

You should see:
server is listening...

Start Client(s)
Open a new terminal window and run:
python client.py

Enter your nickname when prompted.

You can open multiple terminals to run several clients simultaneously.

USAGE

Server Commands
The server runs continuously and doesn't require any input. It displays:

Connection notifications (connected with (IP, Port))

When users join or leave the chat

Client Commands

Type any message and press Enter to send it to all users

Messages appear as: nickname: message

Press Ctrl+C to disconnect from the chat
