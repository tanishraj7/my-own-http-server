#first step is to create a socket 
import socket

USERNAME= 'admin'
PASSWORD= 'ginni26'

server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM) #using ipv4 and TCP protocol as, address family and server type 

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #here we set options like level, option and value 
#reuseaddr to avoid confusions incase of delayed packets delivery
#1- on , 0- off so that we turn on the reuseaddr function
SERVER_HOST= "0.0.0.0"
SERVER_PORT= 2626
server_socket.bind((SERVER_HOST, SERVER_PORT)) #0.0.0.0 so that this server can be accessed by any device with its port number
#port number can be any number between 1024 to 65000
#0-1023 port numbers are assinged for default os
server_socket.listen(5) #server is ready for incoming requests , we can also set the number of connection requests it can hold 
print(f"Listening on port {SERVER_PORT}.. ")

#we need a connection now for our server to show something
while True: #so that we keep on listening for new requests
    print('ran..')
    client_socket, client_add= server_socket.accept() #this gives us the socket and the ip of the requesting client for communication
    print('ran2..')
    
    request= client_socket.recv(1500).decode() #getting the request data with max capacity of 1500 bytes and decoding it into a string
    
    print(request) #the request consists of request line, headers and optional mssg body
    
    #now returning the http response
    #in http 1.1 all requests have the same structure
    #so we use it here
    
    headers= request.split('\n') 
    first_header_components= headers[0].split() #getting the first line components for the request type the url and the protocol
    
    http_method= first_header_components[0] #type of http method
    path= first_header_components[1] #path they are calling for
    
    if http_method == 'GET':
        if path == '/' or path == '/login':
            fin = open('login.html')
        
        elif path == '/book':         #an example of enabling structure script testing/parsing one of the main reason to create your own http server
            fin= open('book.json')
        
        else:
            response = 'HTTP/1.1 404 Not Found\n\nPage not found'
        
        content= fin.read()
        
        response= 'HTTP/1.1 200 OK\n\n' + content
        
    elif http_method== 'POST' and path== '/login':
         # Handle login submission
        body = request.split('\r\n\r\n')[1]  # Get POST body
        params = {key: value for key, value in [param.split('=') for param in body.split('&')]}
        
        if params.get('username')==USERNAME and params.get('password')== PASSWORD:
            fin= open('index.html')
            content= fin.read()
            response= 'HTTP/1.1 200 OK\n\n' + content  #two '\n' are important if we dont do it the parser wont be able to differentitate b/w header and the request content
            
        else:
            response = 'HTTP/1.1 401 Unauthorized\n\nInvalid username or password'
            
  
    else:
        response= 'HTTP/1.1 405 Method Not Allowed\n\nAllow: GET, POST'
        #now we have all the response created only thing to do is to send it to our socket after encoding
        
        
    client_socket.sendall(response.encode()) #sendall handles the re-sending of data that was not successfully sent in one go
    
    #close connection
    client_socket.close()
server_socket.close()
    