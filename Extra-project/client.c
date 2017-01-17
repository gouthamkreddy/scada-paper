#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <unistd.h>

void error(const char *msg)
{
    perror(msg);
    exit(0);
}

int main()
{
    // Initializations
    int sockFD, portNo, n,sz;
    char ch,str[10],buffer[256];
    struct sockaddr_in servAddr;
    struct hostent *server;

    // socket ()
    portNo = 8001;
    sockFD = socket(AF_INET, SOCK_STREAM, 0);
    if (sockFD < 0) 
        error("ERROR!! Unable to open socket");
    
    // Locate Server
    server = gethostbyname("10.0.1.10");
    if (server == NULL)
        error("ERROR!! No such host found\n");
    
    bzero((char *) &servAddr, sizeof(servAddr));
    
    servAddr.sin_family = AF_INET;
    
    bcopy((char *)server->h_addr, (char *)&servAddr.sin_addr.s_addr,server->h_length);
    servAddr.sin_port = htons(portNo);

    // connect()
    if (connect(sockFD, (struct sockaddr *) &servAddr, sizeof(servAddr)) < 0) 
        error("ERROR!! Unable to connect.");

    // Receive Welcome Message from Server

    FILE *sock = fdopen(sockFD, "r+");
    bzero(buffer,256);
    n = recv(sockFD, buffer, 255, 0);

    if (n < 0)
        error("ERROR!! Unable to read from socket");
    printf("SERVER:%s",buffer);
    
    printf("Enter the water level parameters (La,L,H,Ha,mode,pump)\n");
    
    char s[30];
    
    scanf("%s", s); // here we will also be sending the mode along with whether the pump is on or not
    
    n = send(sockFD, s, strlen(s), 0);
	
    fclose(sock);
    close(sockFD);
    return 0;
}
