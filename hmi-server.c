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
    int sockfd, port, n, sz;
    char ch, str[10], buffer[256];
    struct sockaddr_in servAddr;
    struct hostent *server;

    port = 8080;
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockFD < 0) 
        error("ERROR!! Unable to open socket");
    
    server = gethostbyname("10.0.1.10");
    if (server == NULL)
        error("ERROR!! No such host found\n");
    
    bzero((char *) &servAddr, sizeof(servAddr));
    
    servAddr.sin_family = AF_INET;
    
    bcopy((char *)server->h_addr, (char *)&servAddr.sin_addr.s_addr,server->h_length);
    servAddr.sin_port = htons(port);

    if (connect(sockfd, (struct sockaddr *) &servAddr, sizeof(servAddr)) < 0) 
        error("ERROR!! Unable to connect.");


    FILE *sock = fdopen(sockfd, "r+");
    bzero(buffer,256);
    n = recv(sock, buffer, 255, 0);

    if (n < 0)
        error("ERROR!! Unable to read from socket");
    
    printf("SERVER: Current level of water is - %s",buffer);
    
    printf("Enter the water level parameters (La,L,H,Ha,mode,pump)\n");
	
    fclose(sock);
    close(sockfd);
    return 0;
}
