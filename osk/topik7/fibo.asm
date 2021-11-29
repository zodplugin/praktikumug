; fibo.asm
; Meminta user untuk memasukkan suatu nilai n
; dan mengembalikan suku ke-n dari bilangan fibonacci
; 

%include "asm_io.inc"

segment .data

;
; Output strings
;
prompt          db    	"Masukkan n: ", 0

segment .bss
simpan resd 8
x resd 8
y resd 8
total resd 8

segment .text
        global  _main
_main:
        enter   0,0               ; setup routine
        pusha
		;; Kode program Anda di bawah
		
		mov  	eax, prompt
		call	print_string
		call	read_int
		
		; angka yang dimasukkan user berada di eax
		; push angka ini ke stack
		mov [simpan] ,eax
		
			
		
		push          eax	; simpan parameter 1 ke stack
		call	fibo		; panggil subprogram factorial
		add		esp, 4		; bersihkan parameter 1
		
		
		call	print_int	; print hasil
		
		;; Kode program Anda di atas
		;; Jangan modifikasi program di bawah
		popa
        mov     eax, 0            ; return back to C
        leave                     
        ret


;; Subprogram Fibonacci
;
;  int fibonaci(int num) {
;  		int x;
;		// kondisi base
;       if (num == 0) return 0; 
;		if (num == 1) return 1;
;		x = f(num-1);
;		return x + f(num-2);
; 

fibo:
enter 4,0
cmp eax,0
je end
cmp eax,1
je end

mov ebx,1
mov eax,0
mov [x],eax
mov eax,1
mov [y],eax
mulai:
cmp ebx,[simpan]
jae end
mov eax,0
add eax,[x]
add eax,[y]
mov [total],eax
mov eax,0
mov eax,[y]
mov [x],eax
mov eax,0
mov eax,[total]
mov [y],eax
inc ebx
jmp mulai


end:
mov [total],eax
leave 
ret




