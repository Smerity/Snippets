#include <stdio.h>
#include <unistd.h>

int main(void)
{
  unsigned count = 0;
  while (1) {
    usleep(8192);
    printf("\r%c", "\\|/-"[++count % 4]);
    fflush(stdout);
  }

  return 0;
}
