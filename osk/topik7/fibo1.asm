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
		
		push	eax			; simpan parameter 1 ke stack
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
	mov eax, [ebp+8]
	cmp eax,0
	je kosong;
	cmp eax,1
	je satu;
	jmp next
	

;; Tulis kode untuk subprogram yang menghitung suku ke-n barisan Fibonacci
;; Gunakan subprogram rekursif

next:
	dec eax;
	push eax;
	call fibo;
	mov [ebp - 4],eax;
	mov ebx, [ebp + 8];
	sub ebx, 2;
	push ebx;
	call fibo;
	add esp,4;
	mov ebx,eax;
	add ebx, [ebp - 4];
	mov eax,ebx;
	jmp end;
	
kosong:
	mov eax,0
	jmp end
satu:
	mov eax,1
	jmp end

end:
	leave
	ret
