#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

/**
 * infinite_while - Just runs infinite while loop.
 *
 * Return: 0
 *
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
 * main - creates processes
 *
 * Return: 0
 *
 */

int main(void)
{
	pid_t pid;
	int i = 0;

	for (; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
			printf("Zombie process created, PID: %d\n", pid);
		else
			return (0);
	}

	infinite_while();

	return (0);
}
