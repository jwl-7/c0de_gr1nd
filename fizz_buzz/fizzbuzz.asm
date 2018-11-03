;=====================
;=     Fizz Buzz     =
;=====================

; This is written in x86 assembly for MASM.
; This program prints each number from 1 to 100 on a new line.
; For each multiple of 3, it prints 'Fizz' instead of the number.
; For each multiple of 5, it prints 'Buzz' instead of the number.
; For numbers which are multiples of both 3 and 5, it prints 'FizzBuzz' instead of the number.

TITLE FizzBuzz

.386
.MODEL flat, stdcall
.STACK 4096

ExitProcess PROTO, dwExitCode:DWORD			; ends process and its threads
STD_OUTPUT_HANDLE EQU -11					; standard output device
WriteConsole EQU <WriteConsoleA>
GetStdHandle PROTO,               			; get standard handle
	nStdHandle:DWORD  						; type of console handle
WriteConsole PROTO,							; write a buffer to the console
    handle:DWORD,							; output handle
    lpBuffer:PTR BYTE,						; pointer to buffer
    nNumberOfCharsToWrite:DWORD,			; size of buffer
    lpNumberOfCharsWritten:PTR DWORD,		; number of chars written
    lpReserved:PTR DWORD					; 0 (not used)

.DATA
    fizz BYTE 'Fizz', 0
    buzz BYTE 'Buzz', 0
    fizzbuzz BYTE 'FizzBuzz', 0

.DATA?
	consoleOutHandle dword ?
	bytesWritten dword ?

.CODE
main PROC
    ;mov ecx, 100							; set counter to 100
	INVOKE GetStdHandle,					; get standard handle 
		STD_OUTPUT_HANDLE					; standard output device
	mov consoleOutHandle, eax				; EAX = consoleOutHandle
	INVOKE WriteConsole,					; write buffer to console
		consoleOutHandle,					; output handle	
		OFFSET fizz,						; address of fizz
		LENGTHOF fizz - 1,					; length of fizz
		OFFSET bytesWritten, 0				; address of bytesWriten

;fizzy:

    ;loop fizzy            

    INVOKE ExitProcess, 0	; exit code = 0
main ENDP
END main