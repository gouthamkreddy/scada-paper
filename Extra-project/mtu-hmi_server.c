#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<sys/socket.h>
#include<sys/types.h>
#include <unistd.h>
#include <netinet/in.h>
#include<netdb.h>

void error(const char *msg)
{
    perror(msg);
    exit(1);
}

int main()
{
     // Initializations

     FILE * file;
     int sockFD, newSockFD, portNo,m,n,sz;
     socklen_t clientLen;
     char buffer[256],str[10];
     struct sockaddr_in servAddr, clientAddr;
     
     
     // socket ()
     sockFD =  socket(AF_INET, SOCK_STREAM, 0);
     if (sockFD < 0) 
        error("ERROR!! Unable to open socket");

     portNo = 9000;

     servAddr.sin_family = AF_INET;  
     servAddr.sin_addr.s_addr = INADDR_ANY;  

     servAddr.sin_port = htons(portNo);

     // bind()
     if (bind(sockFD, (struct sockaddr *) &servAddr,
              sizeof(servAddr)) < 0) 
              error("ERROR!! Unable to bind");
     
     // listen()     
     listen(sockFD,5);

     // Keep the Server up forever.

     while(1){

     	// accept() a new client.
     	clientLen = sizeof(clientAddr);
     	newSockFD = accept(sockFD,(struct sockaddr *) &clientAddr, &clientLen);
		FILE * sock = fdopen(newSockFD, "r+");
		FILE * f = fopen("status.txt", "r");
		fgets(buffer, 255, (FILE*)f);
		//printf("####%s\n",buffer);
		m = send(newSockFD,buffer,strlen(buffer),0);
		if(m<=0)
			error("Sending Error\n");
		fclose(f);
		fclose(sock);
     	close(newSockFD);
     }
     close(sockFD);
     return 0; 
}
