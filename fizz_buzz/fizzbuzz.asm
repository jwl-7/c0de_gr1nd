TITLE FizzBuzz

;--------------------
;     Fizz Buzz     ;
;--------------------

; This program prints each number from 1 to 100 on a new line.
; For each multiple of 3, it prints 'Fizz' instead of the number.
; For each multiple of 5, it prints 'Buzz' instead of the number.
; For numbers which are multiples of both 3 and 5, it prints 'FizzBuzz' instead of the number.

.386
.MODEL Flat, STDCALL
.STACK 4096
ExitProcess PROTO,dwExitCode:dword

.CODE
main PROC			

    invoke ExitProcess,0
main ENDP
END main