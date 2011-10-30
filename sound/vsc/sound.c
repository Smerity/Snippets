#include <stdio.h>
#include <stdlib.h>

void main(void){
  // Open /dev/dsp -- padsp will redirect this appropriately using the PulseAudio OSS Wrapper
  FILE *f = fopen("/dev/dsp", "w");
  if (!f) exit(1);

  unsigned int t;
  for(t=0;;t++) {
    fprintf(f, "%c", (t*((t>>12|t>>8)&63&t>>4)));
  }
}
