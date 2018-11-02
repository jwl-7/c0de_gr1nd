TITLE FizzBuzz

;--------------------
;     Fizz Buzz     ;
;--------------------

; This is written in x86 assembly for MASM.
; This program prints each number from 1 to 100 on a new line.
; For each multiple of 3, it prints 'Fizz' instead of the number.
; For each multiple of 5, it prints 'Buzz' instead of the number.
; For numbers which are multiples of both 3 and 5, it prints 'FizzBuzz' instead of the number.

.386
.MODEL flat, stdcall
.STACK 4096
ExitProcess PROTO,dwExitCode:DWORD

.DATA
    fizz BYTE 'Fizz', 0             ; 'Fizz' string
    buzz BYTE 'Buzz', 0             ; 'Buzz' string
    fizzbuzz BYTE 'FizzBuzz', 0     ; 'FizzBuzz' string

.CODE
main PROC
    mov ecx, 100

fizzy:


    loop fizzy            

    INVOKE ExitProcess, 0
main ENDP
END main