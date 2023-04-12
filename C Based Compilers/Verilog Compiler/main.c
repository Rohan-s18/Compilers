#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
  FILE *f;

  if(argc < 2) {
    fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
    return 1;
  }

  f = fopen(argv[1], "r");

  if(!f) {
    fprintf(stderr, "Could not open %s\n", argv[1]);
    return 1;
  }

  yyin = f;

  while(yylex()) {
    printf("Token: %s\n", yytext);
  }

  fclose(f);

  return 0;
}