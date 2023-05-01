add $s1, $s2, $s3
r1 beq r2 $s3 = $s1 + $s2;
li $s0, 0;
loop_label:
bge $s0, 10;, exit_loop
addi $s0, $s0, 1
j loop_label
exit_loop:
