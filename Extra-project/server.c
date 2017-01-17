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

     portNo = 8001;

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
     	if (newSockFD < 0) 
        	error("ERROR!! Unable to accept");
		printf("Server: Got Connection from: %d Port: %d\n",inet_ntoa(clientAddr.sin_addr), ntohs(clientAddr.sin_port));
        m = send(newSockFD,"Welcome my dearest Client.Please provide the parameters!\n",58,0);
		bzero(buffer,256);
		recv(newSockFD,buffer,255,0);
		
		int La = 0; int i;
		for(i=0; buffer[i]!=','; i++){
			La = La*10 + (buffer[i] - '0');
		}
		i++;

		int L = 0;
		for(; buffer[i]!=','; i++){
			L = L*10 + (buffer[i] - '0');
		}
	
		i++;
		int H = 0;
		for(; buffer[i]!=','; i++){
			H = H*10 + (buffer[i] - '0');
		}

		i++;
		int Ha = 0;
		for(; buffer[i]!=','; i++){
			Ha = Ha*10 + (buffer[i] - '0');
		}
		
		i++;
		
		int mode = 0;
		mode = buffer[i] - '0';
		i += 2;
		
		int pump = 0;
		pump = buffer[i] -'0';
		printf("La : %d L : %d H : %d Ha : %d\n",La,L,H,Ha);
		FILE * f = fopen("file.txt", "w");
		fprintf(f,"%d,%d,%d,%d,%d,%d,",La,L,H,Ha,mode,pump);
		fclose(f);
		fclose(sock);
     	close(newSockFD);
     }
     close(sockFD);
     return 0; 
}
