%{
#include <stdio.h>
int char_count = 0;
int word_count = 0;
int line_count = 0;
int single_line_comment_count = 0;
int multi_line_comment_count = 0;
int for_count = 0;
int do_count = 0;
int while_count = 0;
%}

%%

"/*"            { ++multi_line_comment_count; }
"*/"            { /* Decrease multi-line comment count only if it's not already zero */ if (multi_line_comment_count > 0) --multi_line_comment_count; }

"//"            { ++single_line_comment_count; }

"for"           { ++for_count; }
"do"            { ++do_count; }
"while"         { ++while_count; }

[a-zA-Z]+       { ++word_count; }

\n              { ++line_count; }

[ \t]+          { /* Do nothing, just skip spaces */ }
.               { ++char_count; }

%%

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <file1> <file2> ... <fileN>\n", argv[0]);
        return 1;
    }
    
    FILE *output_file = fopen("problem4output", "w");
    if (!output_file) {
        printf("Error opening output file.\n");
        return 1;
    }

    for (int i = 1; i < argc; ++i) {
        FILE *file = fopen(argv[i], "r");
        if (!file) {
            printf("Error opening file: %s\n", argv[i]);
            return 1;
        }
        
        char_count = word_count = line_count = single_line_comment_count = multi_line_comment_count = for_count = do_count = while_count = 0;

        yyin = file;
        yylex();

        fprintf(output_file, "File: %s\n", argv[i]);
        fprintf(output_file, "Number of characters: %d\n", char_count);
        fprintf(output_file, "Number of words: %d\n", word_count);
        fprintf(output_file, "Number of lines: %d\n", line_count);
        fprintf(output_file, "Number of single line comments: %d\n", single_line_comment_count);
        fprintf(output_file, "Number of multi line comments: %d\n", multi_line_comment_count);
        fprintf(output_file, "Number of 'for' loops: %d\n", for_count);
        fprintf(output_file, "Number of 'do' loops: %d\n", do_count);
        fprintf(output_file, "Number of 'while' loops: %d\n", while_count);
        fprintf(output_file, "\n");

        fclose(file);
    }

    fclose(output_file);

    return 0;
}
