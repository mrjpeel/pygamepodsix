from PodSixNet.Channel import Channel
from PodSixNet.Server import Server

from time import sleep

#Create the channel to deal with our incoming requests from the client
#A new channel is created every time a client connects
class ClientChannel(Channel):

    #Create a function that will respond to every request from the client
    def Network(self, data):

        #Print the contents of the packet
        print(data)

#Create a new server for our game
def GameServer(Server):

    #Set the channel to deal with incoming requests
    channelClass = ClientChannel

    #Function to deal with new connections
    def Connected(self, channel, addr):
        print("New connection: {}".format(channel))

#Start the server, but only if the file wasn't imported
if __name__ == "__main__":

    print("Server starting on LOCALHOST...\n")

    #Create a server
    s = GameServer()

    #Pump the server at regular intervals (check for new requests)
    while True:
        s.Pump()
        sleep(0.0001)