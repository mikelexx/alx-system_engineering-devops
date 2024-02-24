#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * infinite_while - creates an infinite loop.
 * Return: 0 for success, always
 */

int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - creates 5 zombie processes.
 * Return: 0 for success else 1
 */
int main(void)
{
	int i = 0;
	pid_t pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0);
		}
	}
	infinite_while();
	return (0);
}
